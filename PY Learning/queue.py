import tkinter as tk
from tkinter import messagebox

class Person:
    def __init__(self, name):
        self.name = name
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_queue(self):
        if self.head is None:
            return "The queue is empty."
        current = self.head
        result = []
        length = 0
        while current:
            result.append(current.name)
            current = current.next
            length += 1
        return " -> ".join(result) + f"\nQueue length: {length}"

    def add_person(self, name, friends):
        new_person = Person(name)
        if self.head is None:
            self.head = self.tail = new_person
            return

        current = self.head
        while current:
            for friend in friends:
                if current.name == friend:
                    new_person.next = current.next
                    current.next = new_person
                    if current == self.tail:
                        self.tail = new_person
                    return
            current = current.next

        self.tail.next = new_person
        self.tail = new_person

    def remove_person(self, name):
        if self.head is None:
            return "The queue is empty."

        current = self.head
        previous = None
        while current:
            if current.name == name:
                if previous is None:
                    self.head = current.next
                    if self.head is None:
                        self.tail = None
                else:
                    previous.next = current.next
                    if current == self.tail:
                        self.tail = previous
                return f"{name} has been removed from the queue."
            previous = current
            current = current.next
        return f"Person with the name {name} was not found in the queue."

    def add_vip(self, name):
        new_person = Person(name)
        new_person.next = self.head
        self.head = new_person
        if self.tail is None:
            self.tail = new_person

    def search_person(self, name):
        current = self.head
        while current:
            if current.name == name:
                return f"{name} is in the queue."
            current = current.next
        return f"Person with the name {name} was not found in the queue."

    def reverse_queue(self):
        prev = None
        current = self.head
        self.tail = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        return "Queue order has been reversed."


class QueueApp:
    def __init__(self, root):
        self.queue = Queue()

        self.root = root
        self.root.title("Queue Management")

        self.create_widgets()
        self.current_step = 0
        self.total_steps = 0
        self.steps = [
            self.print_queue,
            self.add_person,
            self.remove_person,
            self.add_vip,
            self.search_person,
            self.reverse_queue
        ]

    def create_widgets(self):
        self.print_button = tk.Button(self.root, text="Print Queue", command=self.next_step)
        self.print_button.pack(pady=5)

        self.print_label = tk.Label(self.root, text="")
        self.print_label.pack(pady=5)

        self.add_name_entry = tk.Entry(self.root)
        self.add_name_entry.pack(pady=5)
        self.add_name_entry.insert(0, "Enter name")

        self.add_friend1_entry = tk.Entry(self.root)
        self.add_friend1_entry.pack(pady=5)
        self.add_friend1_entry.insert(0, "Enter friend 1")

        self.add_friend2_entry = tk.Entry(self.root)
        self.add_friend2_entry.pack(pady=5)
        self.add_friend2_entry.insert(0, "Enter friend 2")

        self.add_friend3_entry = tk.Entry(self.root)
        self.add_friend3_entry.pack(pady=5)
        self.add_friend3_entry.insert(0, "Enter friend 3")

        self.add_button = tk.Button(self.root, text="Add Person", command=self.next_step)
        self.add_button.pack(pady=5)

        self.remove_entry = tk.Entry(self.root)
        self.remove_entry.pack(pady=5)
        self.remove_entry.insert(0, "Enter name to remove")

        self.remove_button = tk.Button(self.root, text="Remove Person", command=self.next_step)
        self.remove_button.pack(pady=5)

        self.vip_entry = tk.Entry(self.root)
        self.vip_entry.pack(pady=5)
        self.vip_entry.insert(0, "Enter VIP name")

        self.vip_button = tk.Button(self.root, text="Add VIP", command=self.next_step)
        self.vip_button.pack(pady=5)

        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack(pady=5)
        self.search_entry.insert(0, "Enter name to search")

        self.search_button = tk.Button(self.root, text="Search Person", command=self.next_step)
        self.search_button.pack(pady=5)

        self.search_label = tk.Label(self.root, text="")
        self.search_label.pack(pady=5)

        self.reverse_button = tk.Button(self.root, text="Reverse Queue", command=self.next_step)
        self.reverse_button.pack(pady=5)

    def next_step(self):
        if self.current_step < self.total_steps:
            self.steps[self.current_step]()
            self.current_step += 1
            if self.current_step == self.total_steps:
                self.current_step = 0

    def print_queue(self):
        self.print_label.config(text=self.queue.print_queue())

    def add_person(self):
        name = self.add_name_entry.get()
        friends = [
            self.add_friend1_entry.get(),
            self.add_friend2_entry.get(),
            self.add_friend3_entry.get()
        ]
        self.queue.add_person(name, friends)
        self.print_queue()

    def remove_person(self):
        name = self.remove_entry.get()
        result = self.queue.remove_person(name)
        messagebox.showinfo("Remove Person", result)
        self.print_queue()

    def add_vip(self):
        name = self.vip_entry.get()
        self.queue.add_vip(name)
        self.print_queue()

    def search_person(self):
        name = self.search_entry.get()
        result = self.queue.search_person(name)
        self.search_label.config(text=result)

    def reverse_queue(self):
        result = self.queue.reverse_queue()
        messagebox.showinfo("Reverse Queue", result)
        self.print_queue()


if __name__ == "__main__":
    root = tk.Tk()
    app = QueueApp(root)
    root.mainloop()
