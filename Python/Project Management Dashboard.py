from datetime import datetime

# Initialize empty lists to store tasks, deadlines, and statuses
tasks = []
deadlines = []
status = []

# Function to add a task
def add_task():
    task_name = input("Enter the task name: ")
    deadline = input("Enter the deadline (YYYY-MM-DD): ")
    task_status = input("Enter the status (Pending/Completed): ")

    try:
        # Validate date format
        datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("Please enter the date in the correct format (YYYY-MM-DD).")
        return

    # Add task details to lists
    tasks.append(task_name)
    deadlines.append(deadline)
    status.append(task_status)

    print(f"Task '{task_name}' added successfully!")

# Function to update task status
def update_status():
    task_index = int(input("Enter the task number you want to update (1-based index): ")) - 1

    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number!")
        return

    new_status = input("Enter the new status (Pending/Completed): ")
    status[task_index] = new_status
    print(f"Task '{tasks[task_index]}' status updated to '{new_status}'.")

# Function to display tasks
def display_tasks():
    if not tasks:
        print("No tasks to display.")
        return

    print("\nTasks List:")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]} | Deadline: {deadlines[i]} | Status: {status[i]}")

# Main program loop
while True:
    print("\nProject Management Dashboard")
    print("1. Add Task")
    print("2. Update Task Status")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        update_status()
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("Exiting the dashboard.")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
