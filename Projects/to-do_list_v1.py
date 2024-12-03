from datetime import date
import json

try:
    with open("data.json") as f:
        to_do_list =  json.load(f)
        id_counter = len(to_do_list)
except:
    to_do_list = []
    id_counter = 0

counter = 0
today = str(date.today())

def add_item():
    global id_counter
    id_counter += 1
    item_to_be_added = input("Enter the item you want to be added to the list: ")
    to_do_list.append({
    "ID" : id_counter ,
    "Description" : item_to_be_added ,
    "Status" : "todo" ,
    "CreatedAt" : today ,
    "UpdatedAt" : today
    })


def update_status():
    which_task = int(input("ID of the task to be updated \n>"))
    if which_task > len(to_do_list) or which_task <= 0:
        print("Not valid")
        return
    #I'm tired so I'm going to do the lame way :)
    update_counter = 0
    for n in range(len(to_do_list)):
        if update_counter == which_task-1:
            print(f'''ID: {to_do_list[n]["ID"]}
                    Task: {to_do_list[n]["Description"]}
                    Status: {to_do_list[n]["Status"]}
                    Created at {to_do_list[n]["CreatedAt"]}
                    Last updated at {to_do_list[n]["UpdatedAt"]}
                --------------------------------------''')
        update_counter+=1
    option = int(input("update to:\n 1. In progress\n 2. Done\n>"))
    if option == 1 or option == 2:
        if option == 1:
            to_do_list[which_task-1]["Status"] = "In Progress"
        elif option == 2:
            to_do_list[which_task-1]["Status"] = "Done"
        to_do_list[which_task-1]["UpdatedAt"] = today
    else:
        print("Not Valid")
    

def show_to_do_list():
    #Function to show the dictionary, pretty bad way of doing it but could't think on other way of doing
    for n in range(len(to_do_list)):
        print(f'''ID: {to_do_list[n]["ID"]}
                        Task: {to_do_list[n]["Description"]}
                        Status: {to_do_list[n]["Status"]}
                        Created at {to_do_list[n]["CreatedAt"]}
                        Last updated at {to_do_list[n]["UpdatedAt"]}
                --------------------------------------''')
    

while True:
    show_to_do_list
    choice = input(">")
    if choice == "add":
        add_item()
    elif choice == "update":
        update_status()
    elif choice == "show":
        show_to_do_list()
    elif choice == "quit":
        with open("data.json","w") as f:
            json.dump(to_do_list, f, indent=2)
        break
    else:
        print("not a valid command")
