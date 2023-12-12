import re

def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read all lines from the file and strip newline characters
        return [line.strip() for line in file.readlines()]


number_dict = { 
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    } 

#extra function for pt 2
def replace_spelled_numbers(s):
     # Create a regular expression pattern that matches any spelled-out number
    pattern = '|'.join(number_dict.keys())

    # hack to avoid overlap
    def repeat_last_letter(match):
        word = match.group(0)
        return word + word[-1]

    # Modify the string by repeating the last letter of each spelled-out number
    modified_string = re.sub(pattern, repeat_last_letter, s)

    # Replace the spelled-out numbers with digits
    return re.sub(pattern, lambda match: number_dict[match.group(0)], modified_string)


def extract_first_last_digit(s):
    # Regular expression pattern
    # This pattern will find the first digit and the last digit (which could be the same)
    pattern = r'(\d).*?(\d)(?=\D*$)|(\d)'
    match = re.search(pattern, s)
    
    if match.group(3):  # If the third group is matched, it's the case with a single digit
        return int(match.group(3) + match.group(3))
    return int("".join(match.groups()[0:2]))

    
def main():
    file_path = 'day1.txt' 
    input_data = read_input_from_file(file_path)
    
    x = 0
    for n in input_data:
       n = replace_spelled_numbers(n) #pt 2
       n = extract_first_last_digit(n)
       x += n 
    print(x)
if __name__ == "__main__":
    main()
