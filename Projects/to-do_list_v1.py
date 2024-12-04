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
    protective_counter = 0
    which_task = int(input("ID of the task to be updated \n>"))
    if which_task <= 0:
        print("Not valid")
        return
    #I'm tired so I'm going to do the lame way :)
    for item in to_do_list:
        if item["ID"] == which_task:
            print(f'''ID: {item["ID"]}
                    Task: {item["Description"]}
                    Status: {item["Status"]}
                    Created at {item["CreatedAt"]}
                    Last updated at {item["UpdatedAt"]}
                --------------------------------------''')
            option = int(input("update to:\n 1. In progress\n 2. Done\n>"))
            if option == 1 or option == 2:
                if option == 1:
                    item["Status"] = "In Progress"
                elif option == 2:
                    item["Status"] = "Done"
                item["UpdatedAt"] = today
            else:
                print("Not Valid")
            break
            protective_counter += 1
        if protective_counter > len(to_do_list):
            print("Couldnt find the id")
    

def show_to_do_list():
    #Function to show the dictionary, pretty bad way of doing it but could't think on other way of doing
    for n in range(len(to_do_list)):
        print(f'''ID: {to_do_list[n]["ID"]}
                        Task: {to_do_list[n]["Description"]}
                        Status: {to_do_list[n]["Status"]}
                        Created at {to_do_list[n]["CreatedAt"]}
                        Last updated at {to_do_list[n]["UpdatedAt"]}
                --------------------------------------''')
    
def show_some(stat):
    if stat == 1:
        show = "todo"
    elif stat == 2:
        show = "In Progress"
    elif stat == 3:
        show = "Done"
    for item in to_do_list:
        if item["Status"] == show:
            print(f'''ID: {item["ID"]}
                    Task: {item["Description"]}
                    Status: {item["Status"]}
                    Created at {item["CreatedAt"]}
                    Last updated at {item["UpdatedAt"]}
                --------------------------------------''')

def delete():
    id_to_delete = int(input("Enter the ID of the task you want to delete:"))
    protective_counter = 0
    if id_to_delete <= 0:
        print("not valid")
        return
    for item in to_do_list:
        if item["ID"] == id_to_delete:
            print(f'''ID: {item["ID"]}
                    Task: {item["Description"]}
                    Status: {item["Status"]}
                    Created at {item["CreatedAt"]}
                    Last updated at {item["UpdatedAt"]}
                --------------------------------------''')
            last_chance = str(input("Type 'yes' if you're really sure you want to delete it: "))
            if last_chance == "yes":
                to_do_list.remove(item)
                return
        protective_counter += 1
        if protective_counter > len(to_do_list):
            print("Couldnt find the ID")
while True:
    choice = input(">")
    if choice == "add":
        add_item()
    elif choice == "update":
        update_status()
    elif choice == "show":
        show_to_do_list()
    elif choice == "show.todo":
        show_some(1)
    elif choice == "show.inp":
        show_some(2)
    elif choice == "show.done":
        show_some(3)
    elif choice == "del":
        delete()
    elif choice == "quit":
        with open("data.json","w") as f:
            json.dump(to_do_list, f, indent=2)
        break
    else:
        print("not a valid command")
