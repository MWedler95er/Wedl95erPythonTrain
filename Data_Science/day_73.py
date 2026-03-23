# pylint: skip-file

import torch
import torch.nn as nn

# Beispiel-Daten: Stunden gelernt -> Punkte im Test
x = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0], [6.0]])  # Form: (6, 1)

y = torch.tensor([[50.0], [55.0], [65.0], [70.0], [75.0], [85.0]])  # Form: (6, 1)


# 1. Modell definieren: kleines neuronales Netz
class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(1, 8)  # 1 Eingang -> 8 Neuronen
        self.output = nn.Linear(8, 1)  # 8 Neuronen -> 1 Ausgang

    def forward(self, x):
        x = torch.relu(self.hidden(x))  # Aktivierungsfunktion
        x = self.output(x)
        return x


model = SimpleNet()

# 2. Loss-Funktion und Optimizer
criterion = nn.MSELoss()  # mean squared error
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# 3. Training
EPOCHS = 500
for epoch in range(EPOCHS):
    # Vorwärtsdurchlauf
    y_pred = model(x)

    # Loss berechnen
    loss = criterion(y_pred, y)

    # Gradienten zurücksetzen
    optimizer.zero_grad()

    # Backpropagation
    loss.backward()

    # Gewichte aktualisieren
    optimizer.step()

    # Optional: alle 100 Epochen etwas ausgeben
    if (epoch + 1) % 100 == 0:
        print(f"Epoch {epoch + 1}/{EPOCHS}, Loss: {loss.item():.4f}")

# 4. Vorhersage für 7 Stunden Lernen
x_new = torch.tensor([[7.0]])
with torch.no_grad():  # im Inferenzmodus keine Gradienten berechnen
    y_new = model(x_new)

print(
    f"Vorhersage des neuronalen Netzes für 7 Stunden Lernen: {y_new.item():.2f} Punkte"
)
