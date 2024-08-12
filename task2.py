class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Task "{removed_task}" removed.')
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def run(self):
        while True:
            print("\nTo-Do List Application")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Remove Task")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_tasks()
            elif choice == '2':
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == '3':
                try:
                    index = int(input("Enter the task number to remove: ")) - 1
                    self.remove_task(index)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '4':
                print("Exiting the To-Do List Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
