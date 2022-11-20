class Car:

    def __init__(self,year,brand,model):

        self.__year = year
        self.__brand = brand
        self.__model = model
        self.__speed = 0

    def set_year(self,year):
        self.__year = year
    def set_brand(self,brand):
        self.__brand = brand
    def set_model(self,model):
        self.__model = model

    def get_year(self):
        return self.__year
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model

    def __str__(self):
        return f"{self.get_brand()} {self.get_model()} {self.get_year()}"

    def accelerate(self):
        self.__speed += 5
        return self.__speed

    def __le__(self,other):
        if self.__speed <= other.__speed:
            return True
        else:
            return False

c = Car(2016,'Toyota','Highlander')
other = Car(2019,'Toyota','Avanza')

# if c = Car(2016,'Toyota','Highlander')
# the statement print(c) prints out 'Toyota Highlander 2016'

print(c)

# b) define the accelerate function which increments the speed 
# of car object by 5 each time it is called. 

c.accelerate()
c.accelerate()
c.accelerate()
    
# c) override the <= operator that compares 2 car objects. The 
# comparison should be entirely based on the speed of the 2 cars. 

other.accelerate()

print(c<=other)