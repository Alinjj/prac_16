class Client:
    def __init__(self,name,last_name,city,deposit):
        self.name = name
        self.last_name = last_name
        self.city = city
        self.deposit = deposit

    def display(self):
        print(self.name,self.last_name,self.city,self.deposit)

Ivan = Client('Ivan','Petrov','Moscow','Deposit:50')
Ivan.display()