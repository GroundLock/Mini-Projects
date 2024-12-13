# To-Do List Application

This is a simple Python-based command-line To-Do List application. It allows users to manage tasks by adding, updating, displaying, and deleting items from a task list. The data is stored persistently in a `data.json` file.

## Features
- Add new tasks to the to-do list.
- Update the status of tasks (e.g., In Progress, Done).
- View all tasks or filter tasks by status.
- Delete tasks from the list.
- Save tasks persistently in a JSON file.

## How to Use
1. Clone or download the repository.
2. Ensure you have Python installed on your system.
3. Run the program with the command:

   ```bash
   python to_do_list.py
   ```

4. Use the following commands to interact with the to-do list.

## Commands

| Command        | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `add`          | Add a new task to the list.                                                 |
| `update`       | Update the status of an existing task. Options: `In Progress`, `Done`.      |
| `show`         | Display all tasks.                                                         |
| `show.todo`    | Display tasks with the status `todo`.                                       |
| `show.inp`     | Display tasks with the status `In Progress`.                                |
| `show.done`    | Display tasks with the status `Done`.                                       |
| `del`          | Delete a task by entering its ID.                                           |
| `quit`         | Save all tasks to the `data.json` file and exit the program.                |

## Example Interaction
```plaintext
> add
Enter the item you want to be added to the list: Finish homework
> show
ID: 1
Task: Finish homework
Status: todo
Created at: 2024-12-13
Last updated at: 2024-12-13
--------------------------------------
> update
ID of the task to be updated 
> 1
update to:
 1. In progress
 2. Done
> 1
> show.inp
ID: 1
Task: Finish homework
Status: In Progress
Created at: 2024-12-13
Last updated at: 2024-12-13
--------------------------------------
> quit
```

## Requirements
- Python 3.x
- `data.json` file (created automatically if not found).

## Notes
- If the `data.json` file does not exist, it will be created automatically when the program starts.
- Ensure the `data.json` file is in the same directory as the script.

## License
This project is open-source and free to use.
