import re
import numpy as np
from scipy.spatial.distance import cdist

#going to approach this problem with a set of coordinates
#similar to how minesweeper might work
#anything with distance <2 (really <= sqrt(2)) to a symbol is a valid position


# stuck on this, need to come back
def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read all lines from the file and strip newline characters
        return [line.strip() for line in file.readlines()]

def main():
    filepath = 'Inputs/day3.txt' 
    input_text = read_input_from_file(filepath)
    numRows = len(input_text)
    numCols = len(input_text[0])

    symbol_coordinates = []

    digit_coordinates = []
    digit_value = []

    for row_index, row in enumerate(input_text):
        for col_index, thisChar in enumerate(row):
            if thisChar.isdigit():
                digit_coordinates.append([row_index,col_index])
                digit_value.append(int(thisChar))
            elif thisChar != '.': #if its not a digit, and its not a period, its a symbol (hopefully)
                symbol_coordinates.append([row_index,col_index])

    #convert to numpy array
    digit_coordinates = np.array(digit_coordinates)
    symbol_coordinates = np.array(symbol_coordinates)

    #compute the pairwise euclidian distance and location of values adjacent to a symbol
    distance = cdist(digit_coordinates,symbol_coordinates)
    isValidDigit = np.any(distance < 2, axis = 1)

    #find digit coordinates that are on the same X as a valid digit and abs(diff(Y)) = 1
    
if __name__ == "__main__":
    main()

