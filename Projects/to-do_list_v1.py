to_do_list = []
counter = 0

def add_item():
    item_to_be_added = input("Enter the item you want to be added to the list: ")
    to_do_list.append(item_to_be_added)

def complete_task():
    taks_to_be_completed = int(input("Insert the number of the task you want to be completed:  "))
    try:
        to_do_list.remove(to_do_list[taks_to_be_completed-1])
    except:
        print("an error in deleting the item has occured")

def show_to_do_list():
    counter = 0
    for item in to_do_list:
        counter += 1
        print(f"{counter}. {item}")

while True:
    if counter == 0:
        add_item()
        counter += 1
    else:
        show_to_do_list
        choice = input("")
        if choice == "add.item":
            add_item()
        elif choice == "complete.item":
            complete_task()
        elif choice == "show.list":
            show_to_do_list()
        elif choice == "quit":
            exit()
        else:
            print("not a valid command")
