import json
from datetime import datetime
from pathlib import Path


DATA_FILE = Path(__file__).parent / "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""

    try:
        with open(
            DATA_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Warning: tasks.json contains invalid JSON.")
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""

    with open(
        DATA_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            tasks,
            file,
            indent=4
        )


def get_next_id(tasks):
    """Generate the next available task ID."""

    if not tasks:
        return 1

    return max(
        task["id"]
        for task in tasks
    ) + 1


def add_task(tasks, title):
    """Create and add a new task."""

    if not title.strip():
        raise ValueError(
            "Task title cannot be empty."
        )

    task = {
        "id": get_next_id(tasks),
        "title": title.strip(),
        "completed": False,
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    tasks.append(task)

    save_tasks(tasks)

    return task


def view_tasks(tasks):
    """Display all tasks."""

    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n========== TASKS ==========")

    for task in tasks:

        status = (
            "✓"
            if task["completed"]
            else " "
        )

        print(
            f'{task["id"]}. '
            f'[{status}] '
            f'{task["title"]}'
        )

        print(
            f'   Created: {task["created_at"]}'
        )

    print("===========================")


def complete_task(tasks, task_id):
    """Mark a task as completed."""

    for task in tasks:

        if task["id"] == task_id:

            if task["completed"]:
                return False

            task["completed"] = True

            save_tasks(tasks)

            return True

    return None


def update_task(tasks, task_id, new_title):
    """Update the title of an existing task."""

    if not new_title.strip():
        raise ValueError(
            "Task title cannot be empty."
        )

    for task in tasks:

        if task["id"] == task_id:

            task["title"] = new_title.strip()

            save_tasks(tasks)

            return True

    return False


def delete_task(tasks, task_id):
    """Delete a task."""

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            save_tasks(tasks)

            return True

    return False