while True :
 age = int(input("input any age"))
 if age <= 12:
   print("your are a child")
 elif age > 12 and age <= 18 :
   print("you are a teenager")
 elif age > 18 and  age <= 30 :
   print ("you are youth")
 elif age > 38 and age <=50 :
   print("you are an adult")
 else :
   print("you are old asf")
    
 again = input("do yu want to check again")
 if again == "no":
    print("thanks , now you know your age bracket")
    break
