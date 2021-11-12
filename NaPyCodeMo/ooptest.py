class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')

    def __add__(self, other):
        newcap = self.capacity + other.capacity
        newname = self.name + "&" + other.name
        return Juice(newname , newcap)


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)