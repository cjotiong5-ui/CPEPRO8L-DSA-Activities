CAPACITY = 10

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        if self.is_full():
            print("Overflow: Stack is full.")
            return False
        self.stack += [item]
        return True

    def pop(self):
        if self.is_empty():
            print("Underflow: Stack is empty.")
            return None
        val = self.stack[-1]
        del self.stack[-1]
        return val

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) >= CAPACITY

    def size(self):
        return len(self.stack)

    def display(self):
        return self.stack

class Stack_menu:
    def show_stack_menu(self):
        my_stack = Stack()
        while True:
            print("\n====== STACK MENU ======")
            print("1. Push")
            print("2. Pop ")
            print("3. Peek (Top)")
            print("4. Display Stack")
            print("5. Check if Empty")
            print("6. Check if Full")
            print("7. Back to Main Menu")

            choice = input("Choose 1-7: ")

            if choice == "1":
                students = input("Enter student name: ")
                if my_stack.push(students):
                    print(f"{students} pushed to stack.")

            elif choice == "2":
                result = my_stack.pop()
                if result is not None:
                    print(f"Popped: {result}")

            elif choice == "3":
                result = my_stack.peek()
                print(f"Top: {result}")

            elif choice == "4":
                print(f"Stack: {my_stack.display()}")
                print(f"Elements: {my_stack.size()} / {CAPACITY}")

            elif choice == "5":
                print("Empty" if my_stack.is_empty() 
                    else "Not Empty")
                
            elif choice == "6":
                print("Full" if my_stack.is_full() 
                    else "Not Full")
                
            elif choice == "7":
                break
            else:
                print("Invalid choice.")

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        if self.is_full():
            print("Overflow: Queue is full.")
            return False
        self.queue += [item]
        return True

    def dequeue(self):
        if self.is_empty():
            print("Underflow: Queue is empty.")
            return None
        val = self.queue[-1]
        del self.queue[-1]
        return val

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= CAPACITY

    def size(self):
        return len(self.queue)

    def display(self):
        return self.queue

class Queue_menu:
    def show_queue_menu(self):
        my_queue = Queue()
        while True:
            print("\n====== QUEUE MENU ======")
            print("1. Enqueue ")
            print("2. Dequeue  ")
            print("3. Peek  (Front)")
            print("4. Display queue")
            print("5. Check if Empty")
            print("6. Check if Full")
            print("7. Back to Main Menu")

            choice = input("Choose 1-7: ")

            if choice == "1":
                students = input("Enter student name: ")
                if my_queue.enqueue(students):
                    print(f"{students} enqueued.")

            elif choice == "2":
                result = my_queue.dequeue()
                if result is not None:
                    print(f"Dequeued: {result}")

            elif choice == "3":
                result = my_queue.peek()
                print(f"Front: {result}")

            elif choice == "4":
                print(f"Queue: {my_queue.display()}")
                print(f"Elements: {my_queue.size()} / {CAPACITY}")

            elif choice == "5":
                print("Empty" if my_queue.is_empty() 
                    else "Not Empty")

            elif choice == "6":
                print("Full" if my_queue.is_full() 
                    else "Not Full")

            elif choice == "7":
                break

            else:
                print("Invalid choice.")

class main_menu:
    def show_main_menu(self):
        while True:
            print("\n====== MAIN MENU ======")
            print("1. Stack Operations (LIFO)")
            print("2. Queue Operations (FIFO) ")
            print("3. Exit")

            choice = input("Choose 1-3: ")

            if choice == "1":
                obj = Stack_menu()
                obj.show_stack_menu()
            elif choice == "2":
                obj = Queue_menu()
                obj.show_queue_menu()
            elif choice == "3":
                print("Program ended.")
                break
            else:
                print("Invalid choice.")

obj = main_menu()
obj.show_main_menu()
