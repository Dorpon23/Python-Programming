def mean(u):
    if type(u) == dict:
        the_mean = sum(u.values())/len(u) 
    else:
        the_mean = sum(u) / len(u)
    return the_mean


student_grades = {"Marry":9.8, "jhon":2.1, "Kayle":6.5}
mondey_temparature = [2,3,54,48,48,57]
print('This is a mean of a Dictonary',mean(student_grades))
print('This is a mean of a list',mean(mondey_temparature))