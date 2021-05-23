class Order:
    def __init__(self,name):
        self.name = name
        self.products=[]

    def setorder(self,products):
        self.products=products
    
    def getorder(self):
        print(self.products)
    