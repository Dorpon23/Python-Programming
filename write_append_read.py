with open("files/vegetables.txt", "a+") as myfile:
    myfile.write("\nOkra")
    myfile.seek(0)
    content = myfile.read()
    
    
print(content)