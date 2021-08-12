import os
from os import path
from datetime import date, time, datetime
from posixpath import realpath
import time

def main():
    name, extension = os.path.splitext("Stocks.txt")

    #/ Check for the item existance 
    print("\n" + "Check for the item existance")
    print("File exist:", str(path.exists("Stocks.txt")))
    print("is it a File?")
    if path.isfile("Stocks.txt") == True:
        print("Yes, it is a " + "\'" + str(extension) + "\'" + " type file.")

    print("is it a Directory?")
    if path.isdir("Stocks.txt") == True:
        print("Yes, it is a directory")
    else:
        print("No, it is not")

    #/ Work with file paths
    print("\n" + "Work with file paths")
    print("item path:", str(realpath("Stocks.txt")))
    print("item path:", str(path.split(realpath("Stocks.txt"))))

    #/ know the file modification time
    print("\n" + "know the file modification time")
    t = time.ctime(path.getmtime("Stocks.txt"))
    print("Modification time:", t)
    cv = datetime.fromtimestamp(path.getmtime("Stocks.txt"))
    print(cv)

    #/ calc how long ago the maodification is done
    print("\n" + "calc how long ago the maodification is done")
    ago = datetime.now() - cv
    print("it has been", ago, "since the file was created") 
    print("OR ", str(ago.total_seconds()), " seconds ago")


if __name__ == "__main__":
    main()
