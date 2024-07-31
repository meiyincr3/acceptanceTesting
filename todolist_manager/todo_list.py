class Task:
    def __init__(self, title, description, due_date, priority='Low'):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def edit(self, title=None, description=None, due_date=None, priority=None):
        if title: self.title = title
        if description: self.description = description
        if due_date: self.due_date = due_date
        if priority: self.priority = priority

    def __str__(self):
        status = 'Completed' if self.completed else 'Pending'
        return f"{self.title} [{self.priority}] - {status}\nDue: {self.due_date}\n{self.description}\n"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, priority='Low'):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        print(f'Task "{title}" added to the list.')

    def list_tasks(self):
        if not self.tasks:
            return []
        return [str(task) for task in self.tasks]

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()
                print(f'Task "{title}" marked as completed.')
                return True
        print(f'Task "{title}" not found in the list.')
        return False

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f'Task "{title}" has been removed from the list.')
                return True
        print(f'Task "{title}" not found in the list.')
        return False

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks have been cleared from the list.")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Clear the to-do list")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (Low, Medium, High): ")
            todo_list.add_task(title, description, due_date, priority)
        elif choice == '2':
            tasks = todo_list.list_tasks()
            if tasks:
                print("Tasks:")
                for task in tasks:
                    print(task)
            else:
                print("No tasks in the to-do list.")
        elif choice == '3':
            title = input("Enter the title of the task to mark as completed: ")
            todo_list.mark_task_completed(title)
        elif choice == '4':
            title = input("Enter the title of the task to remove: ")
            todo_list.remove_task(title)
        elif choice == '5':
            todo_list.clear_tasks()
        elif choice == '6':
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()