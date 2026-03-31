class Task:
    def __init__(self, title, description, status="To Do"):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.title} | {self.description} | {self.status}"


class TaskModel:
    def __init__(self):
        self._tasks = []  

    def add_task(self, task):
        self._tasks.append(task)

    def get_tasks(self):
        return self._tasks

    def update_task(self, index, title=None, description=None, status=None):
        if 0 <= index < len(self._tasks):
            if title:
                self._tasks[index].title = title
            if description:
                self._tasks[index].description = description
            if status:
                self._tasks[index].status = status
            return True
        return False

    def delete_task(self, index):
        if 0 <= index < len(self._tasks):
            self._tasks.pop(index)
            return True
        return False



class TaskView:
    @staticmethod
    def display_tasks(tasks):
        if not tasks:
            print("\nNo tasks.")
            return
        print("\nTasks:")
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def get_task_info():
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        status = input("Enter task status (To Do / In Progress / Completed): ")
        return title, description, status

    @staticmethod
    def get_task_index():
        return int(input("Enter task index: "))



class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self):
        title, description, status = self.view.get_task_info()
        task = Task(title, description, status)
        self.model.add_task(task)
        self.view.display_message("Task added successfully!")

    def view_tasks(self):
        tasks = self.model.get_tasks()
        self.view.display_tasks(tasks)

    def update_task(self):
        self.view_tasks()
        index = self.view.get_task_index()
        title = input("Enter new title (press enter to skip): ")
        description = input("Enter new description (press enter to skip): ")
        status = input("Enter new status (press enter to skip): ")
        success = self.model.update_task(
            index,
            title if title else None,
            description if description else None,
            status if status else None,
        )
        if success:
            self.view.display_message("Task updated successfully!")
        else:
            self.view.display_message("Invalid task index!")

    def delete_task(self):
        self.view_tasks()
        index = self.view.get_task_index()
        success = self.model.delete_task(index)
        if success:
            self.view.display_message("Task deleted successfully!")
        else:
            self.view.display_message("Invalid task index!")



def main():
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    while True:
        print(
            """
Task Manager:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
"""
        )
        choice = input("Choose an option: ")
        if choice == "1":
            controller.add_task()
        elif choice == "2":
            controller.view_tasks()
        elif choice == "3":
            controller.update_task()
        elif choice == "4":
            controller.delete_task()
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
