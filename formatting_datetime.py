from datetime import date, time, datetime

def main():
    now = datetime.now() 

    # print(now.strftime("%a, %b, %B, %Y"))

    # print(now.strftime("Local date and time: %c"))
    # print(now.strftime("Local date: %x"))
    # print(now.strftime("Local time: %X"))
    
    print(now.strftime("current time: %I:%M:%S %p"))
    print(now.strftime("24-Hr time: %H:%M %p"))

main()
# time formatting

