# EXPENSE TRACKER

import pandas as pd
import time

exp=pd.read_csv("expenses.csv")

print('WELCOME!')
name=(input('Enter your name to continue : '))
sal=float(input("Enter your monthly salary: "))
sv=float(input("Enter saving %: "))
save=(sv*0.01)*sal
print("Savings = Rs.",save)
bal=sal-save
print("Remaining amount = Rs.",bal)

def menu():
  while True:
    time.sleep(1)
    print('''
    __________________________________________________________________
                               EXPENSE TRACKER
    __________________________________________________________________

         ************************** MENU **************************


    1. View Expense
    2. View Monthly Expenses
    3. Add Expense
    4. Search Expense
    5. Total Expense
    6. Total Expenses by Category
    7. Delete Expense
    8. Exit
    ''')

    z=int(input('Enter your choice : '))
    print()
    if z==1:
        view()
    elif z==2:
        monthly()
    elif z==3:
        add()
    elif z==4:
        search()
    elif z==5:
        total()
    elif z==6:
        category()
    elif z==7:
        delete()   
    elif z==8:
        print('''
    __________________________________________________________________
                               THANK YOU !!!
    __________________________________________________________________''')
        break
    else:
        print('Invalid choice!')


# View expenses       
def view():
    print('* VIEW EXPENSES *')
    print()
    print(exp)

# View monthly expenses
def monthly():
    print('* VIEW MONTHLY EXPENSES *')
    exp["DATE"] = pd.to_datetime(exp["DATE"], format="%d-%m-%Y")
    month = int(input("Enter month (1-12): "))
    data = exp[exp["DATE"].dt.month == month]
    e=data["AMOUNT"].sum()
    print("Total Expenses = Rs.",e)
    if e > (sal-save):
    print("WARNING: Budget exceeded!")
    bal-=e
    print("Remaining amount = Rs.",bal)
    
# Add expenses
def add():
    print('* ADD EXPENSES *')
    print()
    date1=input('Enter the date: ')
    cat1=input('Enter the category: ')
    des1=input('Enter the description: ')
    amt1=float(input('Enter the amount: '))
    row={"DATE": date1,"CATEGORY": cat1,"DESCRIPTION": des1,"AMOUNT": amt1}
    exp.loc[len(exp)] = row
    exp.to_csv("expenses.csv", index=False)
    print('Expense added successfully!')
    
# Search expenses by category
def search():
    print('* SEARCH EXPENSES BY CATEGORY *')
    print()
    cat1=input('Enter the category to search: ')
    print()
    if cat1 not in (list(exp['CATEGORY'])):
        print(cat1,'expenses not found!')
    else:
        e=exp[exp["CATEGORY"].str.lower() == cat1.lower()]
        print(e)
# Total expenses
def total():
    print('* TOTAL EXPENSES *')
    total=exp["AMOUNT"].sum()
    print("Total = Rs.", total)

# Total expenses by category    
def category():
    print('* TOTAL EXPENSES BY CATEGORY *')
    print(exp.groupby("CATEGORY")["AMOUNT"].sum())
    
# Delete expenses
def delete():
    print('* DELETE EXPENSES *')
    print()
    row = int(input("Enter row number to delete: "))
    exp = exp.drop(row)
    exp = exp.reset_index(drop=True)
    exp.to_csv("expenses.csv", index=False)
    print('Expense deleted successfully!')
        

menu()


