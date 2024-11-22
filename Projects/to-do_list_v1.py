to_do_list = []

def add_item():
    item_to_be_added = input("Enter the item you want to be added to the list: ")
    to_do_list.append(item_to_be_added)

def complete_task():
    taks_to_be_completed = int(input("Insert the number of the task you want to be completed:  "))
    if taks_to_be_completed > len(to_do_list) or taks_to_be_completed < len(to_do_list):
        print("Number not valid")
    else:
        to_do_list.remove(to_do_list[taks_to_be_completed-1])

def show_to_do_list():
    counter = 0
    for item in to_do_list:
        counter += 1
        print(f"{counter}. {item}")
