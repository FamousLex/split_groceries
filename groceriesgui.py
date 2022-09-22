import tkinter as tk
from tkinter import *
import os


root = tk.Tk()
root.geometry("850x850")

entryFrame = tk.Frame(root, bg="#263D42")
entryFrame.place(relwidth=1, relheight=1)


itemLabel = tk.Label(entryFrame, text="Item")
itemLabel.grid(row=0, column=0)
itemEntry = tk.Entry(entryFrame, width=25)
itemEntry.grid(row=0, column=1)

quantityLabel = tk.Label(entryFrame, text="Quantity")
quantityLabel.grid(row=1, column=0)
quantityEntry = tk.Entry(entryFrame, width=25)
quantityEntry.grid(row=1, column=1)

costLabel = tk.Label(entryFrame, text="Cost")
costLabel.grid(row=2, column=0)
costEntry = tk.Entry(entryFrame, width=25)
costEntry.grid(row=2, column=1)

ownersLabel = tk.Label(entryFrame, text="Owners")
ownersLabel.grid(row=3, column=0)
ownersEntry = tk.Entry(entryFrame, width=25)
ownersEntry.grid(row=3, column=1)

ebtLabel = tk.Label(entryFrame, text="SNAP Eligible?")
ebtLabel.grid(row=4, column=0)
ebtEntry = tk.Entry(entryFrame, width=25)
ebtEntry.grid(row=4, column=1)

itemsList = []

buttonFrame = tk.Frame(root, bg="red")
buttonFrame.place(x=0, y=150)

# For ebt param - F: SNAP eligible not taxed, B: SNAP eligible taxed, T: Taxable (not SNAP eligible)
def addItem(itemName, quantity, cost, owners, ebt):
    itemDict = dict(item = itemName, quantity = quantity, cost = cost * quantity, owners = owners, snapEligible = ebt)
    itemsList.append(itemDict)
    print(itemDict)
    print(itemsList)
    itemsLabel = tk.Label(buttonFrame, text=itemDict)
    itemsLabel.pack()
    itemEntry.delete(0, END)
    quantityEntry.delete(0, END)
    costEntry.delete(0, END)
    ownersEntry.delete(0, END)
    ebtEntry.delete(0, END)

def calculateDebts():
    ownerDebtA = 0
    ownerDebtR = 0
    ownerDebtM = 0
    for i in itemsList:
        # print(len(i['owners']))
        # print(i['cost'])
        itemCost = 0
        if i['snapEligible'] == 'F' or i['snapEligible'] == 'B':
            # print('snap eligible')
            # print(len(i['owners']))
            itemCost = i['cost'] / 3
            # print(itemCost)
            if 'A' in i['owners']:
                ownerDebtA = ownerDebtA + (itemCost / len(i['owners']))
            if 'R' in i['owners']:
                ownerDebtR = ownerDebtR + (itemCost / len(i['owners']))
            if 'M' in i['owners']:
                ownerDebtM = ownerDebtM +(itemCost / len(i['owners']))
        else:
            itemCost = i['cost']
            if 'A' in i['owners']:
                ownerDebtA = ownerDebtA + (itemCost / len(i['owners']))
            if 'R' in i['owners']:
                ownerDebtR = ownerDebtR + (itemCost / len(i['owners']))
            if 'M' in i['owners']:
                ownerDebtM = ownerDebtM +(itemCost / len(i['owners']))
    print("Alex's debt: ",round(ownerDebtA, 2))
    print("Rashik's debt:",round(ownerDebtR, 2))
    print("Matt's debt:",round(ownerDebtM, 2))

# addItem("Cream Cheese", 2, 4.69, ['A', 'R', 'M'], "F")
# addItem("Rice", 1, 3.69, ['R'], "T")
# print(itemsList)

addItemButton = tk.Button(buttonFrame, text="Add Item", padx=50, pady=5, command=lambda: addItem(itemEntry.get(), int(quantityEntry.get()), round(float(costEntry.get()), 2), ownersEntry.get().split(), ebtEntry.get()))
addItemButton.pack()

calculateButton = tk.Button(buttonFrame, text="Calculate", command=lambda: calculateDebts())
calculateButton.pack()

root.mainloop()