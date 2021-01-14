# myfile = open("fruits.txt")
# content = myfile.read()
# print(content)
# print(content)

with open("files/fruits.txt") as myfile:
    content = myfile.read()
    
    
print(content)