#Database
orders=[]
dishes=["Fries", "Nuggets","Burger"]
next_order=1
# Commands
def hello():
    print("Welcome! The system is running. Current orders: ",orders)
#1
def new():
    global next_order
    print("Available menu: ", dishes)
    choose=input("Enter dish name: ")
    if choose in dishes:
        order= {
            "number": next_order,
            "order": choose
        }
        orders.append(order)
        print("Succes: Order #",next_order, choose, "added to kitchen.")
        next_order+=1
    else:
        print("Error: Dish not found.")
#2
def look():
    if orders==[]:
        print("No active orders at the moment.")
    else:
        print("Active kitchen orders:", orders)
#3
def delete():
    if orders==[]:
        print("No active orders at the moment.")
    else:
        print("Current orders in progress: ", orders)
        found = False 
        choose=int(input("Enter order ID to deliver: "))
        for order in orders:
            if order["number"] == choose:
                found=True
                orders.remove(order)
                print("Succes: order #",choose,"delivered.")
                break
        if found==False:
            print("Error: Order ID not found.")
#4
def close():
    print("Shift ended. Goodbye!")
#--- PROGRAM START ---
hello()
while True:
    action=input("\nSelect an action:\n1)Add new order\n2)View all orders\n" \
    "3)Deliver order\n4)Close shift\n")
    if action=="1":
        new()
    elif action=="2":
        look()
    elif action=="3":
        delete()
    elif action=="4":
        close()
        break
    else:
        print("\nUnknown command. Please try again.\n")
