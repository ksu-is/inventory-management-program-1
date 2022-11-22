def view_action():
    if dashboard_choice == 1:
        print("\n\n"+ f"{'***** View your inventory below! *****': ^65}"+ "\n\n")
        data = open("inventory.txt","r")
        item_list = data.readline()
    
    while item_list:
    
        item_list = item_list.split(',')
        for word in item_list:
            print(f"{word:20}", end="")
        print("\n")
        item_list = data.readline().rstrip("\n")