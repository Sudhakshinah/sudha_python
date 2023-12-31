# Import date and time

from datetime import datetime

# Finding the current date and time
current_timestamp = datetime.now()
formatted = current_timestamp.strftime("%Y-%m-%d %H-%M-%S")


# function to create a file with name as timestamp and write content as timestamp
def file_as_timestamp():
    f1 = open(current_timestamp.strftime("%Y-%m-%d %H-%M-%S")+".txt", "w")
    f1.write(formatted)


file_as_timestamp()


# function to read the file
def readfile1():
    content = open(current_timestamp.strftime("%Y-%m-%d %H-%M-%S")+".txt", "r")
    print(content.read())


readfile1()









