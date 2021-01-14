# import time
# import sys


# # while True:
# #     with open("files/vegetables.txt") as myfile:
# #         content = myfile.read()
# #         time.sleep(5)
# #         print(content)
# #         time.sleep(5)

# print(sys.prefix)
import time
import os

while True:
    s = "files/vegetables.txt"
    if os.path.exists(s):
        with open(s) as file:
            content = file.read()
            print(content)
    else:
        print("files dosen't exists")

    time.sleep(5)