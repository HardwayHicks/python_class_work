class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

kenwood = Kettle("kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamliton = Kettle('hamilton', 15.99)
print(hamliton.make)
print(hamliton.price)

print("models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamliton.make, hamliton.price))

print('models: {0.make} = {0.price}, {1.make} = {1.price}'.format(kenwood, hamliton))

"""
Class: template for creating objects
Object: an instance of a class
Instantiate: create and instance of a class (object)
Method: a function defined in a class
Attribute: a variable bound to an instance of a class
"""

print(hamliton.on)
hamliton.switch_on()
print(hamliton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

print("*" * 56)

kenwood.power = 1.5
print(kenwood.power)

print("switch to atomic power!")
Kettle.power_source = 'atomic'
print(Kettle.power_source)
print('switch kenwood to gas!')
kenwood.power_source = 'gas'
print(kenwood.power_source)
print(hamliton.power_source)
