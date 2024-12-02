from datetime import date

to_do_list = {
    "ID" : [] ,
    "Description" : [] ,
    "Status" : [] ,
    "CreatedAt" : [] ,
    "UpdatedAt" : []
}

id_counter = 0
counter = 0

def add_item():
    global id_counter
    id_counter += 1
    item_to_be_added = input("Enter the item you want to be added to the list: ")
    to_do_list["ID"]+=[id_counter]
    to_do_list["Description"]+=[item_to_be_added]
    to_do_list['Status']+=["todo"]
    to_do_list['CreatedAt']+=[date.today()]
    to_do_list["UpdatedAt"]+=[date.today()]


def update_status():
    which_task = int(input("ID of the task to be updated \n>"))
    if which_task > len(to_do_list["ID"]) or which_task <= 0:
        print("Not valid")
        return
    #I'm tired so I'm going to do the lame way :)
    update_counter = 0
    for n in range(len(to_do_list["ID"])):
        if update_counter == which_task-1:
            print(f'''ID: {to_do_list["ID"][n]}
                    Task: {to_do_list["Description"][n]}
                    Status: {to_do_list["Status"][n]}
                    Created at {to_do_list["CreatedAt"][n]}
                    Last updated at {to_do_list["UpdatedAt"][n]}
                --------------------------------------''')
        update_counter+=1
    option = int(input("update to:\n 1. In progress\n 2. Done\n>"))
    if option == 1 or option == 2:
        if option == 1:
            to_do_list["Status"][which_task-1] = "In Progress"
        elif option == 2:
            to_do_list["Status"][which_task-1] = "Done"
        to_do_list["UpdatedAt"][which_task-1] = date.today()
    else:
        print("Not Valid")
    

def show_to_do_list():
    #Function to show the dictionary, pretty way of doing it but could't think on other way of doing
    for n in range(len(to_do_list["ID"])):
        print(f'''ID: {to_do_list["ID"][n]}
                Task: {to_do_list["Description"][n]}
                Status: {to_do_list["Status"][n]}
                Created at {to_do_list["CreatedAt"][n]}
                Last updated at {to_do_list["UpdatedAt"][n]}
              --------------------------------------''')
    

while True:
    if counter == 0:
        add_item()
        counter += 1
    else:
        show_to_do_list
        choice = input(">")
        if choice == "add":
            add_item()
        elif choice == "update":
            update_status()
        elif choice == "show":
            show_to_do_list()
        elif choice == "quit":
            break
        else:
            print("not a valid command")
