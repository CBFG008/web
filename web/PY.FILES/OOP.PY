class Car :
    car_type = "new model"


    def __init__(self,brand , color , model , year , speed):
      self.brand = brand
      self.color = color
      self.model = model
      self.year = year
      self.speed = 0

    def engine(self):
        print(f"the engine of {self.brand} {self.model} {self.year} has started")


    def accelerate(self, increase):
      self.speed += increase
      print (f"the {self.color} {self.brand} {self.model} is moving at {self.speed} km/h") 

    def Break (self , decrease):
      self.speed -= decrease
      print(f"the {self.brand} {self.brand} has stopped")

car1 = Car("toyota", "red" ,"corolla", "2007", 0)
car2 = Car("tesla", "blue", "cybertruck", "2024", "0")


car1.engine()
car1.accelerate(50)
car1.accelerate(30)
car1.Break(30)

car2.engine()
car2.accelerate(50)
car2.accelerate(30)
car2.Break(30)








