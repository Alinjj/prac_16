class Guests:
    def __init__(self, name,last_name,city):
        self.name = name
        self.last_name = last_name
        self.city = city

    def display(self):
        print(self.name,self.last_name,self.city)
g1 = Guests('Ivan','Petrov','Moscow')
g2 = Guests('Micle','Petrov','St.Peterburg')
clients = [g1,g2]
for client in clients:
    if client in clients:
        print(client.display())
    else:
        print("------")