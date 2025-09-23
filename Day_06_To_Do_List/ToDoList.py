def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def main():
    tasks = []  # list of task descriptions
    done = []   # parallel list: True/False status

    while True:
        show_menu()
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            task = input("Enter new task: ")
            tasks.append(task)
            done.append(False)
            print("Task added.")

        elif choice == '2':
            if not tasks:
                print("No tasks yet.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks):
                    status = "✓" if done[i] else " "
                    print(f"{i+1}. [{status}] {task}")

        elif choice == '3':
            if not tasks:
                print("No tasks to mark.")
            else:
                try:
                    num = int(input("Enter task number to mark as done: "))
                    if 1 <= num <= len(tasks):
                        done[num-1] = True
                        print(f"Task {num} marked as done.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a number.")

        elif choice == '4':
            if not tasks:
                print("No tasks to delete.")
            else:
                try:
                    num = int(input("Enter task number to delete: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num-1)
                        done.pop(num-1)
                        print(f"Removed task: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a number.")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
