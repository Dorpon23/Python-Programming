def sentencemaker(pharase):
    cap = pharase.capitalize()
    interogatives = ("how" , "what" , "why")
    
    if pharase.startswith(interogatives):
        return "{}?".format(cap)
    else:
        return "{}".format(cap)
    



results = []

while True:
    user_input = input("Say Something :-) ")
    if user_input == "\end":
        break
    else:
        results.append(sentencemaker(user_input))
        
        
print(" ".join(results))