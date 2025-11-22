class bank :
    


    def __init__(self,name , balance=0):
      self.name = name
      self.__balance = balance
      self.transactions =[]
      

    def deposit(self, amount):
        if amount > 0 :
         self.__balance += amount
         print(f"the deposit of {self.name} of {amount} is {self.__balancel}  only")
        else:
         print("deposit amount must be greater than 0")

    def withdrawal(self, amount):
      if 0 < amount <= self.__balance:
       self.__balance -= amount
       self.transaction.append(f"withdrew{amount}")
       print (f"the withdrawal of {self.name} of {amount} is {self.__balance}  only") 
      else:
        print(f"sorry{self.name} ,insufficient balance or invalid amount")

    def transactions(self):
      print (f"transaction history for {self.name}:")
      for t in self.transactions:
        print ("-",  t)

    def get_balance(self):
      return self.__balance

acc1 = bank("alex", 1000) 

acc1.deposit(10000)
acc1.withdrawal(6000)
acc1.withdrawal(1000)
print("current balance:" , acc1.get_balance)
acc1.transactions()








