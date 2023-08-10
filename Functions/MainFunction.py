# Python Main Function
# Main function is like the entry point of a program. However, Python interpreter runs the code
# right from the first line. The execution of the code starts from the starting line and goes 
# line by line. It does not matter where the main function is present or it is present or not.


print("This is a starting Of Code")


def msg(str):
    print(f"Msg is {str}")

msg(" Function Called from out said of __main__ funtion")

if __name__ == "__main__":
    msg(" Call Msg Function from __main__ function")    