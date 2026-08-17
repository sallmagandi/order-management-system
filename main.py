# Data
dishes=["Fries", "Nuggets", "Burger"]
import sqlite3
connection=sqlite3.connect("vkit.db")
cursor=connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, dish TEXT)")
connection.commit()
# Commands
def hello():
    print("Welcome! The system is running.")
#1
def new():
    print("Available menu: ", dishes)
    choose=input("Enter dish name: ")
    if choose in dishes:
        cursor.execute("INSERT INTO orders (dish) VALUES (?)", (choose,) )
        connection.commit()
        cursor.execute("SELECT * FROM orders")
        all_orders=cursor.fetchall()
        print(f"Succes! '{choose}' added to kichen.")
    else:
        print("Error: Dish not found.")
#2
def look():
    cursor.execute("SELECT * FROM orders")
    all_orders=cursor.fetchall()
    if all_orders==[]:
        print ("No active orders at the moment.")
    else:   
        for row in all_orders:
            print(f"Order№ {row[0]}: {row [1]}")
#3
def delete():
    cursor.execute("SELECT * FROM orders")
    all_orders=cursor.fetchall()
    for row in all_orders:
        print(f"Order ID: {row[0]}: {row [1]}")
    choose=int(input("Enter order ID to deliver: "))
    cursor.execute("DELETE FROM orders WHERE id = ?", (choose,))
    connection.commit()
    print("Order delivered.")
#4
def clear():
    cursor.execute("DELETE FROM orders")
    connection.commit()
#5
def close():
    print("Shift ended. Goodbye!")
    connection.close()
#--- PROGRAM START ---
hello()
while True:
    action=input("\nSelect an action:\n1)Add new order\n2)View all orders\n" \
    "3)Deliver order\n4)Clear orders\n5)Close shift\n")
    if action=="1":
        new()
    elif action=="2":
        look()
    elif action=="3":
        delete()
    elif action=="4":
        clear()
    elif action=="5":
        close()
        break
    else:
        print("\nUnknown command. Please try again.\n")
