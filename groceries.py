itemsList = []

# For ebt param - F: SNAP eligible not taxed, B: SNAP eligible taxed, T: Taxable (not SNAP eligible)
def addItem(itemName, quantity, cost, owners, ebt):
    itemDict = dict(item = itemName, quantity = quantity, cost = cost * quantity, owners = owners, snapEligible = ebt)
    itemsList.append(itemDict)
    print(itemDict)
    

addItem("Cream Cheese", 2, 4.69, ['A', 'R', 'M'], "F")
addItem("Rice", 1, 3.69, ['R'], "T")
print(itemsList)

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
    



calculateDebts()
