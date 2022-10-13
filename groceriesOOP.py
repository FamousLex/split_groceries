class item():
    def __init__(self, itemName, quantity, cost, owners, ebtEligible):
        self.itemName = itemName
        self.quantity = quantity
        self.cost = cost
        self.owners = owners
        self.ebtEligible = ebtEligible

    def showInfo(self):
        print('Item Name: ', self.itemName)

oItem1 = item('Cream cheese', 1, 3.29, ['A', 'R', 'M'], 'F')
oItem1.showInfo()