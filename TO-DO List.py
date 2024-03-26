#Task 1 TO-DO list by CODEWAY 

class Chore:
    def __init__(self, task):
        self.task = task
        self.completed = False

    def finish_chore(self):
        self.completed = True

    def __str__(self):
        return self.task + (" [COMPLETED]" if self.completed else "")

class TaskManager:
    def __init__(self):
        self.chores = []

    def add_chore(self, task):
        self.chores.append(Chore(task))

    def finish_chore(self, chore_number):
        self.chores[chore_number].finish_chore()

    def show_chores(self):
        for i, chore in enumerate(self.chores):
            print(f"{i+1}. {chore}")

def run():
    task_manager = TaskManager()
    while True:
        print("\n1. Add chore\n2. Finish chore\n3. Show chores\n4. Quit")
        option = int(input("Choose an option: "))
        if option == 1:
            chore = input("Enter chore: ")
            task_manager.add_chore(chore)
        elif option == 2:
            chore_number = int(input("Enter chore number to mark as completed: ")) - 1
            task_manager.finish_chore(chore_number)
        elif option == 3:
            task_manager.show_chores()
        elif option == 4:
            print("Goodbye!")
            break

if __name__ == "__main__":
    run()
