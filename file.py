#my_file = open("first class txt")
#print(my_file.read())
#my_file.close()

with open("first class.txt","r") as my_file:
  text = my_file.read()
  print(text)