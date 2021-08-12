def main():
    #Open a file
    f1 = open("Stocks.txt", "r") # "w+" / "a" / "r"

    # Case1- Open a file writing a text in it or create a file if it doesn't exist
    """for i in range(10):
       f1.write("AMZN,APPLE,GOGL,FCBK,TCS,CINFRA "+ str(i) + "\n")
    """

    #Case2- Read a pre-existed file,a nd Append the text/phrase at the end in that file
    """ for i in range(1):
        f1.write("market closed " + "\n")
    """

    # Case3- read file
    if f1.mode == "r":
        content = f1.read()
        print(content)

# always close a file when done manupulating 
    f1.close() 

if  __name__ == "__main__":
    main()







