
global products
products = [[]]



    
#menu for navigation
def start():
    print("Welcome to Inventory Manager")
    print("Enter 1 to view items")
    print("Enter 2 to add an item")
    print("Enter 3 to remove an item")
    print("Enter 4 to update an item")
    print("Enter 5 to search an item")
    print("Enter 6 to exit")
    
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print_items()
    elif choice == 2:
        add()
    elif choice == 3:
        remove()
    elif choice == 4:
        update()
    elif choice == 5:
        search()
    elif choice == 6:
        print("Thank you for using Inventory Manager")
        
        
def add():
    #code to add item

    
    

def remove():
    #code to remove item

def update():
    #code to update item

def search():
    #code to search item

def print_items():
    #code to print all items    
        
        




start()       


        