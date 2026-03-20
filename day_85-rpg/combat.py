"""
combat.py — Rundenbasiertes Kampfsystem (Pokemon-Style)

Ablauf pro Runde:
  1. Statuseffekte aller Charaktere verarbeiten (Gift, Feuer, Regen...)
  2. Spielerzug: Skill wählen → auf Ziel anwenden
  3. Gegnerzüge (jeder lebende Gegner): zufälliger Skill → auf Spieler anwenden
  4. Prüfen ob Kampf beendet (alle Gegner tot ODER Spieler tot)
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field

from character import Character, Companion, Enemy, Player
from display import Color, ask_choice, health_bar, print_separator
from items import Item, get_random_loot
from skills import Effect, EffectType, Skill, SkillType

# ─── Kampfergebnis ───────────────────────────────────────────────────────────


@dataclass
class CombatResult:
    victory: bool
    xp: int = 0
    loot: list[Item] = field(default_factory=list)


# ─── Skill anwenden ──────────────────────────────────────────────────────────


def _apply_debuff(skill: Skill, target: Character, messages: list[str]) -> None:
    """Wendet einen Debuff-Effekt (Gift, Feuer, Betäubung, Schwächung) auf das Ziel an."""
    if not (skill.effect and skill.effect.type in _DEBUFF_TYPES):
        return
    if skill.effect.type == EffectType.STUN:
        if random.random() < 0.30:
            target.add_effect(skill.effect)
            messages.append(f"{target.name} ist betäubt!")
    else:
        target.add_effect(skill.effect)
        messages.append(f"{target.name} ist {skill.effect.type.value}!")


def _apply_damage(
    skill: Skill, user: Character, target: Character, messages: list[str]
) -> None:
    """Schaden, Lifesteal und Debuff — nur für Angriffs-Skills."""
    total_dmg = 0
    for _ in range(skill.hits):
        raw = int(skill.get_total_damage() * user.atk / 10)
        actual = target.take_damage(raw, skill.ignore_defense_pct)
        total_dmg += actual
        if skill.hits > 1:
            messages.append(f"  Treffer: {actual} Schaden.")

    if skill.hits == 1:
        messages.append(
            f"{user.name} trifft {target.name} mit {skill.name} → {total_dmg} Schaden."
        )
    else:
        messages.append(
            f"{user.name} trifft {target.name} {skill.hits}× → {total_dmg} Gesamtschaden."
        )

    if skill.lifesteal_pct and total_dmg > 0:
        stolen = user.heal(int(total_dmg * skill.lifesteal_pct))
        messages.append(f"{user.name} stiehlt {stolen} Lebenspunkte.")

    _apply_debuff(skill, target, messages)


def _apply_skill(user: Character, target: Character, skill: Skill) -> list[str]:
    """
    Wendet einen Skill an und gibt Beschreibungs-Nachrichten zurück.

    Reihenfolge:
      1. Schild/Verteidigung am User
      2. Heilung am User
      3. Buff-Effekte am User
      4. Schaden, Lifesteal, Debuffs am Ziel
      5. Speziallogik (Special Tags)
    """
    messages: list[str] = []

    if skill.defense:
        shield_val = skill.get_total_defense()
        user.add_effect(Effect(EffectType.SHIELD, shield_val, 2))
        messages.append(f"{user.name} erhält {shield_val} Schildpunkte (2 Runden).")

    if skill.heal:
        healed = user.heal(skill.get_total_heal())
        messages.append(f"{user.name} heilt sich um {healed} HP.")

    if skill.effect and skill.effect.type in (EffectType.STRENGTHEN, EffectType.REGEN):
        user.add_effect(skill.effect)
        messages.append(
            f"{user.name} ist {skill.effect.type.value} ({skill.effect.duration} Runden)."
        )

    if skill.damage and skill.skill_type != SkillType.DEFENSE:
        _apply_damage(skill, user, target, messages)

    _apply_special_tag(user, target, skill, messages)

    return messages


_DEBUFF_TYPES = (EffectType.WEAKEN, EffectType.POISON, EffectType.BURN, EffectType.STUN)


def _apply_special_tag(
    user: Character, target: Character, skill: Skill, messages: list[str]
) -> None:
    """Verarbeitet spezielle Skill-Tags (Einmal-Effekte, Rassen-Fähigkeiten)."""
    tag = skill.special_tag

    if skill.name == "Volles Internet":
        roll = random.random()
        if roll < 0.33:
            healed = user.heal(30)
            messages.append(f"5G-Signal! Magische Heilung: +{healed} HP.")
        elif roll < 0.66:
            user.add_effect(Effect(EffectType.STRENGTHEN, 50, 2))
            messages.append("Volle Bandbreite! ATK massiv erhöht für 2 Runden!")
        else:
            target.add_effect(Effect(EffectType.STUN, 0, 1))
            messages.append("Lag-Spike! Gegner überspringt die nächste Runde!")

    elif tag == "elf_besinnung":
        user.base_atk += 8
        messages.append(f"{user.name} konzentriert sich — ATK dauerhaft +8!")

    elif tag == "zwerg_trunk":
        healed = user.heal(int(user.max_hp * 0.40))
        messages.append(f"{user.name} trinkt — +{healed} HP und 28 Rüstung!")

    elif tag == "mensch_befreiung":
        before = len(user.effects)
        user.effects = [e for e in user.effects if e.type not in _DEBUFF_TYPES]
        if removed := before - len(user.effects):
            messages.append(f"{user.name} befreit sich von {removed} Debuff(s)!")
        messages.append("...und kontert sofort!")

    elif tag == "remove_debuffs":
        user.effects = [e for e in user.effects if e.type not in _DEBUFF_TYPES]
        messages.append(f"{user.name} entfernt alle Debuffs!")


# ─── Status anzeigen ─────────────────────────────────────────────────────────


def _print_combat_status(
    player: Player, enemies: list[Enemy], planned: "dict[int, Skill] | None" = None
) -> None:
    """
    Zeigt HP-Balken + Effekte aller Kampfteilnehmer.
    planned: vorausgewählte Gegner-Skills {enemy_index: skill} — wird als
             Aktions-Telegraph unter jedem Gegner angezeigt.
    """
    print_separator()
    fx = player.get_effect_summary()
    suffix = f"  {Color.CYAN}{fx}{Color.RESET}" if fx else ""
    print(
        f"  {Color.BOLD}{Color.GREEN}{player.name}{Color.RESET} "
        f"{health_bar(player.hp, player.max_hp)}{suffix}"
    )
    print_separator()

    alive_idx = 0
    for e in enemies:
        if not e.is_alive:
            continue
        fx = e.get_effect_summary()
        suffix = f"  {Color.CYAN}{fx}{Color.RESET}" if fx else ""
        print(
            f"  {Color.BOLD}{Color.RED}{e.name}{Color.RESET} "
            f"{health_bar(e.hp, e.max_hp)}{suffix}"
        )

        # ── Aktions-Telegraph ────────────────────────────────────────────
        if planned and alive_idx in planned:
            skill = planned[alive_idx]
            if e.is_stunned:
                intent = f"{Color.DIM}💤 Betäubt — kein Angriff{Color.RESET}"
            elif skill.damage > 0:
                intent = f"{Color.RED}⚔  plant: {skill.name}  (Schaden ~{skill.damage * skill.hits}){Color.RESET}"
            elif skill.defense > 0:
                intent = f"{Color.YELLOW}🛡  plant: {skill.name}  (Schild ~{skill.defense}){Color.RESET}"
            else:
                intent = f"{Color.MAGENTA}✨ plant: {skill.name}{Color.RESET}"
            print(f"     {intent}")

        alive_idx += 1

    print_separator()


# ─── Spieler- und Gegnerzug ──────────────────────────────────────────────────


def _player_turn(player: Player, enemies: list[Enemy]) -> None:
    """Spieler wählt Skill (und ggf. Ziel). Inkl. Tränke + Rassen-Fähigkeit."""
    alive = [e for e in enemies if e.is_alive]

    # Optionen aufbauen
    extra_options: list[str] = []

    # Trank?
    potions = list(player.inventory)
    if potions:
        extra_options.append(
            f"🧪 Trank benutzen ({', '.join(i.name for i in potions)})"
        )

    # Rassen-Fähigkeit verfügbar?
    racial = player.racial_skill
    if racial and not player.racial_skill_used:
        extra_options.append(
            f"⚡ RASSEN-FÄHIGKEIT: {racial.name} — {racial.description}"
        )

    print(f"\n{Color.BOLD}Deine Skills:{Color.RESET}")
    skill_labels = [str(s) for s in player.skills]
    all_options = extra_options + skill_labels

    idx = ask_choice(all_options, "Wähle Aktion")

    # Trank?
    if idx == 0 and potions and extra_options[0].startswith("🧪"):
        potion_idx = ask_choice([i.name for i in potions], "Welchen Trank")
        msg = player.use_potion(potions[potion_idx])
        print(f"  {Color.GREEN}{msg}{Color.RESET}")
        return

    # Rassen-Fähigkeit?
    racial_option_idx = 1 if potions else 0
    if (
        racial
        and not player.racial_skill_used
        and idx == racial_option_idx
        and extra_options[racial_option_idx].startswith("⚡")
    ):
        player.racial_skill_used = True
        print(f"\n  {Color.MAGENTA}⚡ {racial.name} aktiviert!{Color.RESET}")
        # Defensiv-Skills auf Spieler selbst; Schaden-Skills auf Gegner
        target: Character = alive[0] if racial.damage > 0 and alive else player
        for msg in _apply_skill(player, target, racial):
            print(f"  {Color.MAGENTA}{msg}{Color.RESET}")
        return

    # Normaler Skill
    chosen_skill = player.skills[idx - len(extra_options)]

    target = alive[0]
    if len(alive) > 1 and chosen_skill.damage > 0:
        print(f"\n{Color.BOLD}Welchen Gegner angreifen?{Color.RESET}")
        target = alive[ask_choice([e.name for e in alive], "Ziel")]

    for msg in _apply_skill(player, target, chosen_skill):
        print(f"  {msg}")


def _enemy_turn(enemy: Enemy, player: Player, skill: Skill) -> None:
    """Führt den vorausgewählten Gegner-Skill aus."""
    print(f"\n  {Color.RED}{enemy.name} setzt {skill.name} ein!{Color.RESET}")
    for msg in _apply_skill(enemy, player, skill):
        print(f"  {Color.RED}{msg}{Color.RESET}")


# ─── Haupt-Kampffunktion ─────────────────────────────────────────────────────


def _print_companion_status(companion: Companion) -> None:
    fx = companion.get_effect_summary()
    suffix = f"  {Color.CYAN}{fx}{Color.RESET}" if fx else ""
    print(
        f"  {Color.BOLD}{Color.BLUE}[NPC] {companion.name}{Color.RESET} "
        f"{health_bar(companion.hp, companion.max_hp)}{suffix}"
    )


def _run_enemy_turns(
    alive_enemies: list[Enemy], player: Player, planned: "dict[int, Skill]"
) -> None:
    """Führt die Züge aller lebenden Gegner mit vorab gewählten Skills aus."""
    for i, enemy in enumerate(alive_enemies):
        if not player.is_alive:
            break
        for msg in enemy.process_effects():
            print(f"  {Color.MAGENTA}{msg}{Color.RESET}")
        if not enemy.is_alive:
            continue
        if enemy.is_stunned:
            print(f"  {Color.CYAN}{enemy.name} ist betäubt!{Color.RESET}")
            enemy.effects = [e for e in enemy.effects if e.type != EffectType.STUN]
            continue
        _enemy_turn(enemy, player, planned[i])


def _run_single_round(
    player: Player,
    enemies: list[Enemy],
    companion: "Companion | None",
    planned: "dict[int, Skill]",
) -> None:
    """Führt eine einzelne Kampfrunde durch (Status → Spieler → Companion → Gegner)."""
    _print_combat_status(player, enemies, planned)
    if companion:
        _print_companion_status(companion)

    for msg in player.process_effects():
        print(f"  {Color.MAGENTA}{msg}{Color.RESET}")
    if companion:
        for msg in companion.process_effects():
            print(f"  {Color.BLUE}[NPC] {msg}{Color.RESET}")
    if not player.is_alive:
        return

    if player.is_stunned:
        print(f"{Color.RED}{player.name} ist betäubt!{Color.RESET}")
        player.effects = [e for e in player.effects if e.type != EffectType.STUN]
    else:
        _player_turn(player, enemies)

    if companion and any(e.is_alive for e in enemies):
        c_skill, c_target = companion.act(enemies, player)
        print(
            f"\n  {Color.BLUE}[NPC] {companion.name} setzt {c_skill.name} ein!{Color.RESET}"
        )
        for msg in _apply_skill(companion, c_target, c_skill):
            print(f"  {Color.BLUE}[NPC] {msg}{Color.RESET}")

    _run_enemy_turns([e for e in enemies if e.is_alive], player, planned)


def _collect_victory_rewards(enemies: list[Enemy]) -> CombatResult:
    """Berechnet XP und würfelt Loot nach gewonnenem Kampf."""
    total_xp = sum(e.template.xp_reward for e in enemies)
    loot: list[Item] = [
        item
        for e in enemies
        if random.random() < e.loot_chance
        for item in [get_random_loot(include_relics=True)]
        if item
    ]
    print(f"\n{Color.GREEN}Sieg! Du erhältst {total_xp} XP.{Color.RESET}")
    return CombatResult(victory=True, xp=total_xp, loot=loot)


def run_combat(
    player: Player, enemies: list[Enemy], companion: "Companion | None" = None
) -> CombatResult:
    """
    Führt einen vollständigen Kampf durch.

    Args:
        player:    Spielercharakter
        enemies:   Liste der Gegner
        companion: Optionaler NPC-Begleiter

    Returns:
        CombatResult mit victory=True/False, XP und Loot-Liste
    """
    names = ", ".join(e.name for e in enemies)
    print(f"\n{Color.RED}{Color.BOLD}⚔  KAMPF BEGINNT! ⚔{Color.RESET}")
    print(f"Gegner: {Color.RED}{names}{Color.RESET}")
    if companion:
        print(f"Begleiter: {Color.BLUE}{companion.name}{Color.RESET}\n")

    player.racial_skill_used = False
    round_num = 1

    while player.is_alive and any(e.is_alive for e in enemies):
        print(f"\n{Color.YELLOW}── Runde {round_num} ──{Color.RESET}")
        alive_enemies = [e for e in enemies if e.is_alive]
        planned: dict[int, Skill] = {
            i: e.choose_skill() for i, e in enumerate(alive_enemies)
        }
        _run_single_round(player, enemies, companion, planned)
        round_num += 1

    if player.is_alive:
        return _collect_victory_rewards(enemies)
    print(f"\n{Color.RED}Du wurdest besiegt...{Color.RESET}")
    return CombatResult(victory=False)
