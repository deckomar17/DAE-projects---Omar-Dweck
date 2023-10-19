# Task Manager Application

# List to store tasks
tasks = []

# Function to add a task to the list
def add_task(task_name, due_date, priority):
    task = {
        'task_name': task_name,
        'due_date': due_date,
        'priority': priority,
        'completed': False
    }
    tasks.append(task)
    print(f'Task "{task_name}" added successfully!')

# Function to mark a task as completed
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f'Task "{tasks[task_index]["task_name"]}" marked as completed!')
    else:
        print('Invalid task index.')

# Function to list all tasks
def list_tasks():
    if not tasks:
        print('No tasks to display.')
    else:
        print('Tasks:')
        for i, task in enumerate(tasks):
            status = 'Completed' if task['completed'] else 'Incomplete'
            print(f'{i + 1}. Task: {task["task_name"]}, Due Date: {task["due_date"]}, Priority: {task["priority"]}, Status: {status}')

# Main program loop
while True:
    print('\nTask Manager Menu:')
    print('1. Add Task')
    print('2. Mark Task as Completed')
    print('3. List Tasks')
    print('4. Exit')
    
    choice = input('Enter your choice: ')
    
    if choice == '1':
        task_name = input('Enter task name: ')
        due_date = input('Enter due date: ')
        priority = input('Enter priority: ')
        add_task(task_name, due_date, priority)
    elif choice == '2':
        task_index = int(input('Enter the task index to mark as completed: '))
        complete_task(task_index - 1)  # Subtract 1 to match the 0-based list index
    elif choice == '3':
        list_tasks()
    elif choice == '4':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Please try again.')
