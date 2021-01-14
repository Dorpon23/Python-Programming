temps = [ 222, 231, 233, -999, 234]
new_temps1 = [temp  /10 for temp in temps if temp !=-999]
new_temps2 = [temp / 10 if temp !=-999 else 0 for temp in temps]
print(new_temps1)
print(new_temps2)