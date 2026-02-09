import sys
import json
import os


class TodoManager:
    def __init__(self, file="tasks.json"):
        self.file = file

    def load_tasks(self):
        if not os.path.exists(self.file):
            return []
        with open(self.file, "r") as f:
            return json.load(f)

    def save_tasks(self, tasks):
        with open(self.file, "w") as f:
            json.dump(tasks, f, indent=2)

    def add_task(self, task):
        if not task.strip():
            print("❌ Task cannot be empty.")
            return

        tasks = self.load_tasks()
        tasks.append(task)
        self.save_tasks(tasks)
        print("✅ Task added.")

    def list_tasks(self):
        tasks = self.load_tasks()

        if not tasks:
            print("No tasks found.")
            return

        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

    def delete_task(self, index):
        tasks = self.load_tasks()

        if index < 1 or index > len(tasks):
            print("❌ Invalid task number.")
            return

        removed = tasks.pop(index - 1)
        self.save_tasks(tasks)
        print(f"🗑 Deleted: {removed}")


def main():
    manager = TodoManager()

    if len(sys.argv) < 2:
        print("Usage: add/list/delete")
        return

    command = sys.argv[1]

    if command == "add":
        task = " ".join(sys.argv[2:])
        manager.add_task(task)

    elif command == "list":
        manager.list_tasks()

    elif command == "delete":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("❌ Provide valid task number.")
            return

        manager.delete_task(int(sys.argv[2]))

    else:
        print("Unknown command.")


if __name__ == "__main__":
    main()
