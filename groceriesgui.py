import tkinter as tk
from tkinter import *
import os
import itertools

#grid and layout
root = tk.Tk()
root.geometry("650x850")

entryFrame = tk.Frame(root, bg="#263D42", height=500)
entryFrame.grid(row=0, column=0, sticky='ew')
root.grid_columnconfigure(0, weight=1)
entryFrame.grid_columnconfigure(0, weight=1)

itemLabel = tk.Label(entryFrame, text="Item")
itemLabel.grid(row=0, column=0)
itemEntry = tk.Entry(entryFrame, width=30)
itemEntry.grid(row=0, column=1)

quantityLabel = tk.Label(entryFrame, text="Quantity")
quantityLabel.grid(row=1, column=0)
quantityEntry = tk.Entry(entryFrame, width=30)
quantityEntry.grid(row=1, column=1)

costLabel = tk.Label(entryFrame, text="Cost")
costLabel.grid(row=2, column=0)
costEntry = tk.Entry(entryFrame, width=30)
costEntry.grid(row=2, column=1)

ownersLabel = tk.Label(entryFrame, text="Owners")
ownersLabel.grid(row=3, column=0)
ownersEntry = tk.Entry(entryFrame, width=30)
ownersEntry.grid(row=3, column=1)

ebtLabel = tk.Label(entryFrame, text="SNAP Eligible?")
ebtLabel.grid(row=4, column=0)
ebtEntry = tk.Entry(entryFrame, width=30)
ebtEntry.grid(row=4, column=1)

whoPaidLabel = tk.Label(entryFrame, text="Who Paid?")
whoPaidLabel.grid(row=5, column=0)
whoPaidEntry = tk.Entry(entryFrame, width=30)
whoPaidEntry.grid(row=5, column=1)

buttonFrame = tk.Frame(root, bg="red")
buttonFrame.place(x=100, y=150)

itemsList = [] 
ownersDebtsDict = {}

def getDebtPerms(ownersList):
    for i in itertools.permutations(ownersList, 2):
        ownersDebtsDict[i[0] + i[1]] = 0
    # print(ownersDebtsDict.keys())

# arm = ['A', 'R', 'M']
# getDebtPerms(arm)

# For ebt param - F: SNAP eligible not taxed, B: SNAP eligible taxed, T: Taxable (not SNAP eligible)

def addItem(itemName, quantity, cost, owners, ebt, whoPaid):
    itemDict = dict(item = itemName, quantity = quantity, cost = cost * quantity, owners = owners, snapEligible = ebt, whoPaid = whoPaid)
    itemsList.append(itemDict)
    print(itemsList)
    itemsLabel = tk.Label(buttonFrame, text=itemDict)
    itemsLabel.pack()
    itemEntry.delete(0, END)
    quantityEntry.delete(0, END)
    costEntry.delete(0, END)
    ownersEntry.delete(0, END)
    ebtEntry.delete(0, END)
    whoPaidEntry.delete(0, END)
    getDebtPerms(owners)

def deleteLastItem():
    itemsList.pop()
    packSlaves = buttonFrame.pack_slaves()
    packSlaves[-1].destroy()

def calculateDebts():
    for i in itemsList:
        itemCost = 0
        if i['snapEligible'] == 'F' or i['snapEligible'] == 'B':
            itemCost = i['cost'] / 3
        else:
            itemCost = i['cost']
        itemCost = itemCost / len(i['owners'])
        ownersKeysList = ownersDebtsDict.keys()
        for j in i['owners']:
            for k in ownersKeysList:
                if j == k[0] and i['whoPaid'] == k[1]:
                    ownersDebtsDict[k] = ownersDebtsDict[k] + itemCost            
    print(ownersDebtsDict)

addItemButton = tk.Button(buttonFrame, text="Add Item", padx=50, pady=5, command=lambda: addItem(itemEntry.get(), int(quantityEntry.get()), round(float(costEntry.get()), 2), ownersEntry.get().split(), ebtEntry.get(), whoPaidEntry.get()))
addItemButton.pack()

deleteLastItemButton = tk.Button(buttonFrame, text="Delete Last Item", padx=50, pady=5, command=lambda: deleteLastItem())
deleteLastItemButton.pack()

calculateButton = tk.Button(buttonFrame, text="Calculate", padx=50, pady=5, command=lambda: calculateDebts())
calculateButton.pack()

root.mainloop()