import time
global products
products = [["1","chips",15,"solid","20g",12]]



    
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
    global item_id 
    item_id = int(input("Enter item ID: "))
    global item_name 
    item_name = input("Enter item name: ")
    global item_quantity 
    item_quantity = int(input("Enter item quantity: "))
    global item_type 
    item_type = input("Enter item type: ")
    global item_price 
    item_price = float(input("Enter item price: "))
    
    products.append([item_id,item_name,item_quantity,item_type,item_price])
    
    print("Item added successfully")
    time.sleep(1)
    start()
    

def remove():
    #code to remove item
    print("Enter item name to remove: ")
    remove = input("")
    def search_1 (arr, target):
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if (arr[i][j] == target):
                    del(products[i])
                    print(f"Item {target} removed successfully")
                    start()
        print("Item not found")
    
    # Driver code
    arr = products
    target = remove
    
    search_1(arr, target)
    
    



def print_items():
    #code to print all items
    for i in range(len(products)):
        for j in range(len(products[i])):
            print(products[i][j],end=" | ")
            time.sleep(1)
            start()        
        




start()       


        