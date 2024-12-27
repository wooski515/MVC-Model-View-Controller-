class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks

class TaskView:
    @staticmethod
    def display_tasks(tasks):
        print("\nПоточні завдання:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        if not tasks:
            print("Немає доступних завдань.")

    @staticmethod
    def display_message(message):
        print(f"\n{message}")

class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, task):
        self.model.add_task(task)
        self.view.display_message(f"Завдання '{task}' успішно додано.")

    def remove_task(self, task):
        if task in self.model.get_tasks():
            self.model.remove_task(task)
            self.view.display_message(f"Завдання '{task}' видалено успішно.")
        else:
            self.view.display_message(f"Завдання '{task}' не знайдено.")

    def show_tasks(self):
        tasks = self.model.get_tasks()
        self.view.display_tasks(tasks)

if __name__ == "__main__":
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    while True:
        print("\nОпції:")
        print("1. Додати завдання")
        print("2. Видалити завдання")
        print("3. Переглянути завдання")
        print("4. Вихід")
        
        choice = input("Виберіть варіант: ")

        if choice == "1":
            task = input("Введіть завдання для додавання: ")
            controller.add_task(task)
        elif choice == "2":
            task = input("Введіть завдання для видалення: ")
            controller.remove_task(task)
        elif choice == "3":
            controller.show_tasks()
        elif choice == "4":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Будь ласка, спробуйте ще раз.")
