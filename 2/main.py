import requests

def get_input():
    input = []
    with open('input.txt', 'r') as file:
        while True:
            line = file.readline()
            if line:
                input.append(line.replace('\n', ''))
            else: 
                break
    return input

def split_input_row(row):
    row_arr = row.split(" ")
    min_max = row_arr[0].split('-')
    first_num = int(min_max[0])
    second_num = int(min_max[1])
    character = row_arr[1][0]
    password = row_arr[2]
    return (first_num, second_num, character, password)

def policy_one(input):
    n_correct_passwords = 0
    for i in input:
        (minimum, maximum, character, password) = split_input_row(i)
        if minimum <= password.count(character) <= maximum:
            n_correct_passwords += 1
    return n_correct_passwords

def policy_two(input):
    n_correct_passwords = 0
    for i in input:
        (first, second , character, password) = split_input_row(i)
        first -= 1 # minus 1 because they start from index 1 and not 0
        second -= 1 # minus 1 because they start from index 1 and not 0
        if bool( password[first] == character ) ^ bool( password[second] == character ): # XOR the two boolean expressions.
            n_correct_passwords += 1
    return n_correct_passwords

if __name__ == "__main__":
    input = get_input()
    print("Number of Correct passwords (1. policy): ", policy_one(input))
    print("Number of Correct passwords (2. policy): ", policy_two(input))

