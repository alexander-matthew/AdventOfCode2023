import numpy as np
import re

# going to try using object oriented programming again
# got pt 1. Still working on pt2
class Card:
    def __init__(self, game_text):
        self.winningNumbers = []
        self.cardNumbers    = []
        self.parse_game(game_text)

    def parse_game(self, game_text):
        # get rid of the "Card X:"
        game_text = re.sub(r'^[^:]*:', '', game_text).strip()
        
        #then parse into array of integers
        winningNumbers,cardNumbers  = game_text.split('|')

        self.winningNumbers = np.array([int(num) for num in winningNumbers.strip().split()])
        self.cardNumbers    = [int(num) for num in cardNumbers.strip().split()]
    
    def num_matches(value, array):
        return sum(1 for item in array if item == value)
        
    #part 1: compute point value of card
    def value(self):
        N = self.num_matches()
        return 0 if N == 0 else 2 ** (N - 1)
    #part two
    
    
# input is a set of strings, lets turn this into an array of games.
def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read all lines from the file and strip newline characters
        text_data = [line.strip() for line in file.readlines()]
    CardArray = []
    for i in text_data:
        card = Card(i)
        CardArray.append(card)
    return CardArray


def main():
    filepath = 'Inputs/day4.txt'
    CardArray = read_input_from_file(filepath)
    totalValue = 0
    total_power = 0
    for index, card in enumerate(CardArray): #enumerate starting at one
        totalValue += card.value()
        

    print(f"The answer to part 1 is: {totalValue}")
    #print(f"The answer to part 2 is: {total_power}")

if __name__ == "__main__":
    main()
