import todo


def get_task_id():
    """Get a valid task ID from the user."""

    try:
        return int(
            input("Enter task ID: ")
        )

    except ValueError:
        print("Task ID must be a number.")
        return None


def display_menu():
    """Display the main menu."""

    print("\n")
    print("╔════════════════════════════╗")
    print("║        CLI TODO APP        ║")
    print("╚════════════════════════════╝")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")


def main():

    tasks = todo.load_tasks()

    while True:

        display_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":

            title = input(
                "Enter task title: "
            )

            try:

                task = todo.add_task(
                    tasks,
                    title
                )

                print(
                    f'Task "{task["title"]}" '
                    "added successfully."
                )

            except ValueError as error:

                print(f"Error: {error}")

        elif choice == "2":

            todo.view_tasks(tasks)

        elif choice == "3":

            task_id = get_task_id()

            if task_id is None:
                continue

            result = todo.complete_task(
                tasks,
                task_id
            )

            if result is True:

                print(
                    "Task marked as completed."
                )

            elif result is False:

                print(
                    "Task is already completed."
                )

            else:

                print("Task not found.")

        elif choice == "4":

            task_id = get_task_id()

            if task_id is None:
                continue

            new_title = input(
                "Enter new task title: "
            )

            try:

                result = todo.update_task(
                    tasks,
                    task_id,
                    new_title
                )

                if result:

                    print(
                        "Task updated successfully."
                    )

                else:

                    print("Task not found.")

            except ValueError as error:

                print(f"Error: {error}")

        elif choice == "5":

            task_id = get_task_id()

            if task_id is None:
                continue

            result = todo.delete_task(
                tasks,
                task_id
            )

            if result:

                print(
                    "Task deleted successfully."
                )

            else:

                print("Task not found.")

        elif choice == "6":

            print("\nGoodbye!")
            break

        else:

            print(
                "Invalid choice. "
                "Please select 1-6."
            )


if __name__ == "__main__":
    main()