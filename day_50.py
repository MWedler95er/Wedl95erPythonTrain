"""Linked List"""


class Seiten:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.url = f"www.{name.lower()}.com"


class GoogleSeiten(Seiten):
    def __init__(self):
        super().__init__("Google")


class WikipediaSeiten(Seiten):
    def __init__(self):
        super().__init__("Wikipedia")


class GitHubSeiten(Seiten):
    def __init__(self):
        super().__init__("GitHub")


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def suche_seite(self, start_node, seiten_name):
        current = start_node
        while current:
            if current.value == f"www.{seiten_name.lower()}.com":
                return True
            current = current.next
        return False


linked_list = LinkedList()
linked_list.head = Node(GoogleSeiten().url)
linked_list.head.next = Node(WikipediaSeiten().url)
linked_list.head.next.next = Node(GoogleSeiten().url)
linked_list.head.next.next.next = Node(WikipediaSeiten().url)
linked_list.head.next.next.next.next = Node(GitHubSeiten().url)
linked_list.head.next.next.next.next.next = Node("testString")

print(linked_list.suche_seite(linked_list.head, "GitHub"))

print("Linked List:")
linked_list.print_list()
