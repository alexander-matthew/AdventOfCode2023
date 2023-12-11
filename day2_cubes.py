import re

# define some global variables
file_path = 'day2.txt'
R = 12
G = 13
B = 14


# going to try using object oriented programming to structure this problem
# each game will be a class with 3 n length number arrays
# we want to get the max of each array
class Game:
    def __init__(self, game_text):
        self.red = []
        self.green = []
        self.blue = []

        self.parse_game(game_text)

    def parse_game(self, game_text):
        draws = game_text.split(';')
        for draw in draws:
            red, green, blue = self.extract_colors(draw.strip())
            self.red.append(red)
            self.green.append(green)
            self.blue.append(blue)

    # get the number before each (singular) instance of a color. Default to zero.
    def extract_colors(self, draw):
        red_count   = int(re.search(r'(\d+)\s*red'  , draw).group(1)) if 'red'   in draw else 0
        green_count = int(re.search(r'(\d+)\s*green', draw).group(1)) if 'green' in draw else 0
        blue_count  = int(re.search(r'(\d+)\s*blue' , draw).group(1)) if 'blue'  in draw else 0
        return red_count, green_count, blue_count
    
    #part 1: max values are < limits
    def is_possible(self, R, G, B):
        return \
            max(self.red)   <= R and \
            max(self.green) <= G and \
            max(self.blue)  <= B
    #part two
    def power(self):
        return max(self.red) * max(self.blue) * max(self.green)
    
# input is a set of strings, lets turn this into an array of games.
def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read all lines from the file and strip newline characters
        text_data = [line.strip() for line in file.readlines()]
    GameArray = []
    for i in text_data:
        game = Game(i)
        GameArray.append(game)
    return GameArray


def main():
    GameArray = read_input_from_file(file_path)
    x = 0
    total_power = 0
    for i, game in enumerate(GameArray,1): #enumerate starting at one
        if game.is_possible(R,G,B):
            x += i
        total_power += game.power()

    print(f"The answer to part 1 is: {x}")
    print(f"The answer to part 2 is: {total_power}")

if __name__ == "__main__":
    main()
