from enum import Enum
from turtle import update
import requests
import json
import time
import mine

# Global variables
BASE_LINK = "https://coe892.reev.dev/lab1/rover/"

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    
class Rover:

    # __int__ function
    def __init__(self):
        self.move_sequence = ""
        self.location = [0, 0] #current location of rover represented by [x,y]
        self.direction = Direction.SOUTH  #initial direction for rover
        self.map_2d_list = []
        self.successful_flag = True

    # Initialize Rovers
    def start_rover(self):

        self.move_sequence = self.get_rover_moves() #save rover's sequence of moves
        self.map_2d_list = self.generate_map_list() #create 2d list that will save the map layout

        for move in self.move_sequence:
            # Terminate moves if successful Flag is False
            if( self.successful_flag == False):
                # Mine explodes the move after the rover leaves it
                self.set_direction(move)
                print("Terminate")
                break
            else:
                self.set_direction(move)

        self.generate_path()

    # Retrieve rover moves from API
    def get_rover_moves(self, rover_number):
        # 1. Read rover data from API
        api_link = BASE_LINK + str(rover_number)
        response = requests.get(api_link)

        # 2. Save sequence of moves
        self.move_sequence = response.json()['data']['moves']
        # self.move_sequence = 'LMDM'
        # print("\nRover {}\nmove_seq = {}".format(self.rover_number, self.move_sequence))  
        # print("Move type: {type}".format( type = type(self.move_sequence[0])) )

        return self.move_sequence

    # Determine the new direction of the rover, based on the move in move_sequence
    def set_direction(self, move):
        #Move
        if(move == 'M'):
            self.set_location()

            # Attempt to write path in map_2d_list
            self.update_path(move)
            return
        #Dig    
        if(move == 'D'):
            # Attempt to write path in map_2d_list
            self.update_path(move)
            return
        
        # Based off current direction of rover, determine the new direction of the rover if the
        # next move is either 'R' or 'L'
        # North direction case
        if self.direction == Direction.NORTH:
            if move == 'R':
                self.direction = Direction.EAST
                return
            elif move == 'L':
                self.direction =  Direction.WEST
                return
        # East direction case
        elif self.direction == Direction.EAST:
            if move == 'R':
                self.direction = Direction.SOUTH
                return
            elif move == 'L':
                self.direction =  Direction.NORTH
                return
        # South direction case
        elif self.direction == Direction.SOUTH:
            if move == 'R':
                self.direction = Direction.WEST
                return
            elif move == 'L':
                self.direction =  Direction.EAST
                return
        # West direction case
        elif self.direction == Direction.WEST:
            if move == 'R':
                self.direction = Direction.NORTH
                return
            elif move == 'L':
                self.direction =  Direction.SOUTH
                return

    # Updates location of rover
    def set_location(self):

        # Get row and col
        row = len(self.map_2d_list)
        col = len(self.map_2d_list[0])

        # Note: location[0] = x-coordinate, location[1] = y-coordinate
        if (self.direction == Direction.NORTH and self.location[1] > 0):
            self.location[1] -= 1

        if (self.direction ==  Direction.EAST and self.location[0] < col -1):
            self.location[0] += 1

        if (self.direction ==  Direction.SOUTH and self.location[1] < row -1):
            self.location[1] += 1

        if (self.direction ==  Direction.WEST and self.location[0] > 0):
            self.location[0] -= 1

        # DEBUG
        # print("location {}:".format(self.location))
        # self.map_2d_list[self.location[1]][self.location[0]] = '*'

    # Update path in map_2d_list
    def update_path(self, move):
        # Checkif a mine is dectected, and always disarm it
        if(self.map_2d_list[self.location[0]][self.location[1]] == "1"):

                    
            # Disarm correct mine
            for i in range(1, 5):
                mineObj = mine.Mine(i)
                # print("Mine {} Location: {}".format(mineObj.number, mineObj.location))
                # print("Rover {} Location: {}\n".format(self.rover_number, self.location))

                if(int(mineObj.location[0]) == self.location[0] and int(mineObj.location[1]) == self.location[1]):
                    # print("inside")
                    mineObj.disarm_mine()
                    break

            # print("[+] MINE DISARM SUCCESSFUL\n")
                  
        self.map_2d_list[self.location[1]][self.location[0]] = '*'

    # Create map_2d_list from map.txt file
    def generate_map_list(self):
        
        # 1. Declare map_2d_list
        self.map_2d_list  = []

        text_file = "map.txt"
        with open(text_file) as file:
            firstline = file.readline()
            # save number of row & columns
            row = int( firstline.split(' ')[0] )
            col = int ( firstline.split(' ')[1] )

        # 2. Initialize values for map_2d_list
        self.map_2d_list = [[0 for i in range(col)] for j in range(row)]
        colIdx = 0
        rowIdx = 0

        # save map data
        file = open(text_file, "r")
        next(file) # Skip first line in file

        for line in file:
            for char in line:
                # Save data about map
                if char.isalnum():
                    self.map_2d_list[rowIdx][colIdx] = char
                    # DEBUG
                    # print("Row: {rowIdx}, Col: {colIdx}, element: {char}".format(rowIdx= rowIdx, colIdx = colIdx, char = char))
                    colIdx += 1
            rowIdx += 1
            colIdx = 0

        # 3. Creat starting point 
        self.map_2d_list[0][0] = '*'

        return self.map_2d_list
        
    # Write path into rover text files
    def generate_path(self, rover_number):
        text_file = 'rover-data/path_{}.txt'.format(rover_number)
        with open(text_file, 'w') as file:
            for i in self.map_2d_list:
                for j in i:
                    file.write(j)
                file.write('\n')

    # Determine if the rover successfully implemented all moves 
    def get_successful_flag(self):
        return self.successful_flag


# ---------------------------------------------------------------
# --                TESTING & DEBUGGING                        --
# ---------------------------------------------------------------
# Main function
def main():
    # start = time.time()
    # for i in range(1,11):
    #     Rover(i)
    # end = time.time()
    # print("************************************************************")
    # print("*                       Sequential                         *")
    # print("************************************************************\n")
    # print("The computation time was: ", (end-start), "seconds\n")

    for i in range(1, 11):
        # i = 1
        roverObj = Rover(i)
        print("Rover {} moves: {}".format(roverObj.rover_number, roverObj.move_sequence))
        print("Rover {} map: {}".format(roverObj.rover_number, roverObj.map_2d_list))
        print("Rover {} successFlag: {}".format(roverObj.rover_number, roverObj.successful_flag))
        print("Rover {} location: {}\n".format(roverObj.rover_number, roverObj.location))

# main()
