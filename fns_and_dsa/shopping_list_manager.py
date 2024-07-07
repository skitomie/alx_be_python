
from prompt_toolkit import prompt

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")     
   

def main():
    shopping_list = []   

    while True:
        display_menu()
        
        choice = input("Enter your choice: ")

        if choice == '1':
            
            item = prompt("Enter the item to add:")
            shopping_list.append(item)
            print(f"{item} has been added to your Shopping List!!!")
        elif choice == '2':
             item = prompt("Remove an item from your List:")
             if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from your Shopping List!!!")
             else: 
                print("Item not found on your Shopping List")
        elif choice == '3':
            if shopping_list:
                print("Your Shopping List:")
            for items  in shopping_list:
                print(f" {items}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    Ola@dapo1055