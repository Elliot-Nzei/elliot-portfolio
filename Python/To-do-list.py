# Create an empty list to store our tasks
todo_list = []

while True:
    # Show the menu
    print("\n=== My To-Do List ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    
    # Get user's choice
    choice = input("What would you like to do? (1-4): ")
    
    # Add a task
    if choice == '1':
        task = input("Enter a task: ")
        todo_list.append(task)
        print("Task added!")
    
    # View all tasks
    elif choice == '2':
        if todo_list:  # if list is not empty
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks in your list!")
    
    # Remove a task
    elif choice == '3':
        if todo_list:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
            num = input("Enter the number of task to remove: ")
            if num.isdigit() and 1 <= int(num) <= len(todo_list):
                removed_task = todo_list.pop(int(num) - 1)
                print(f"Removed: {removed_task}")
            else:
                print("Invalid task number!")
        else:
            print("No tasks to remove!")
    
    # Exit the program
    elif choice == '4':
        print("Goodbye!")
        break
    
    # Handle invalid input
    else:
        print("Please enter a number between 1 and 4")