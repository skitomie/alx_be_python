
def display_menu():
    print("Shopping List Manager")     
    Shopping_List_Manager = [
                        "1. Add Item", 
                        "2. Remove Item",
                        "3. View List",
                        "4. Exit"]
    for option in Shopping_List_Manager:
                print(option) 


def add_item(shopping_list):
    item = input(f"Add an item to your List:").strip()
    shopping_list.append(item)
    print(f"{item} has been added to your Shopping List!!!")


def remove_item(shopping_list):
    item = input(f"Remove an item from your List:").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your Shopping List!!!")
    else: 
         print("Item not found on your Shopping List")
    

def display_list(shopping_list):
    if shopping_list:
         print("Your Shopping List:")
    for items  in shopping_list:
        print(f" {items}")

def main():
    shopping_list = []   

    while True:
        display_menu()
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            dispaly_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    Ola@dapo1055