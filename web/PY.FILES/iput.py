while True :
 nom_1= float(input("any number"))
 operator = (input("any operator (+,-,/,%)"))
 num_2 = float(input("any number"))

 if operator == "+" :
   print("result:" ,  nom_1 + num_2)
 elif operator == "-" :
   print("result:" ,  nom_1 - num_2)
 elif operator == "/" :
   if num_2 != 0 :
     print ("result", nom_1 / num_2)
   else :
     print ("not divisible by 0")
 elif operator == "*" :
   print("result:" ,  nom_1 * num_2)
 else :
   print ("invalid operator")

   #loop
 again = input("do yu want to check again")
 if again == "no":
    print("thanks , now you know your age bracket")
    break

