import time
import mine
import rover


# Main function
def main():

    print("************************************************************")
    print("*                       Sequential                         *")
    print("************************************************************\n")

    # Rover Path Creation
    start = time.time()
    for i in range(1,11):
        roverObj = rover.Rover(i)
    end = time.time()
    print("Rover Path Creation\ncomputation time: ", (end-start), "seconds\n")

    # Mine Disarm 
    start = time.time()
    for i in range(1,5):
        mineObj = mine.Mine(i)
    end = time.time()
    print("Mine Disarm\ncomputation time: ", (end-start), "seconds\n")
   
main()
