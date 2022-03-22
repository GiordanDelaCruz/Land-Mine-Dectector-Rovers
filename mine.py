import hashlib

class Mine:

    def __init__(self, number):
        self.number = number
        self.mine_info = self.get_mine_info()
        self.serial_num = self.get_serial_num()
        self.location = self.get_loocation()
        self.hash_value = self.get_hash_value()
        self.disarm_flag = False

    # Read mine file
    def get_mine_info(self):
        mine_info = []
        file = open("mines.txt", "r")

        for line in file:

            # Rertrive correct mine info
            if(True):
                mine_info.append(line.split())
        # print(mine_info)
        # print("Mine Number: {}".format(mine_info[self.number - 1][0]))
        # print("x-location: {}".format(mine_info[self.number - 1][1]))
        # print("y-location: {}".format(mine_info[self.number - 1][2]))
        # print("Hash-Value: {}".format(mine_info[self.number - 1][3]))

        return mine_info

    # get serial number
    def get_serial_num(self):
        return self.mine_info[self.number - 1][0]

    # get location of mine
    def get_loocation(self):
        location = [self.mine_info[self.number - 1][1], self.mine_info[self.number - 1][2] ]
        return location

    # get hash_value
    def get_hash_value(self):
         return self.mine_info[self.number - 1][3]

    # disarm a mine
    def disarm_mine(self):

        # Temporary to disarm mine
        temp_mine_key = self.serial_num + self.hash_value

        while True:
            # Encoding str using encode(), then sending to SHA256()
            output = hashlib.sha256(temp_mine_key.encode())
            # print( output.hexdigest()[0])

            # Determining if hash value starts at 0
            if( output.hexdigest()[0] == "0"):

                # Save result
                result = output

                # Update mine disarm flag
                self.disarm_flag = True

                # Printing the equivalent hexadecimal value.
                print("Mine #{}: The hexadecimal equivalent of SHA256 is\n{}\n".format(self.number, result.hexdigest()))
                break
            temp_mine_key += "1"


# ---------------------------------------------------------------
# --                TESTING & DEBUGGING                        --
# ---------------------------------------------------------------
# Main function
def main():
    # mineObj = Mine(3)
    # mineObj.get_mine_info
    # print("Mine Number: {}".format(mineObj.number))
    # print("Serial Number: {}".format(mineObj.serial_num))
    # print("Location: {}".format(mineObj.location))
    # print("Hash Value: {}".format(mineObj.hash_value))

    # Disarm all the mines
    for i in range(1, 5):
        mineObj = Mine(i)
        mineObj.disarm_mine()

# main()