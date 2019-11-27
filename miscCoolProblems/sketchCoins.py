# libraries
import pprint
import numpy as np
import time
import pdb

# functions


# reverses a string
def reverse_string(a_string):
    return a_string[::-1]


# takes a number from base b and turns it in to a decimal number
def base_b_to_decimal(base_b_num: str, base_b: int) -> int:
    dec_num = 0
    for i in range(0, len(base_b_num)):
        dec_num += int(base_b_num[-1-i]) * base_b**i  # multiply the ith place from the end by b**i so 0th place is b**0, etc
    return dec_num


# turns a decimal number into base b
def dec_to_base_b(dec_num: int, base_b):
    base_b_num = ''
    left_overs = dec_num
    while left_overs > 0:
        # note, the function int() truncates (like floor)
        base_b_num += str(left_overs % base_b)
        left_overs = int(left_overs/base_b)
    return reverse_string(base_b_num)


# puts padding zeros on a number until it is a certain length, or truncates the number if it is too long
def pad_num(a_num: str, req_len: int) -> str:
    if len(a_num) >= req_len:
        return a_num[0:req_len+1]
    else:
        return '0' * (req_len - len(a_num)) + a_num
    
    
# inverts one of the ternary states, switching 1 and 2 and leaving 0 alone
def invert_ter_state(ter_state: str) -> str:
    out_ter_state = ''
    for ci in ter_state:
        if ci == "1":
            out_ter_state += "2"
        elif ci == "2":
            out_ter_state += "1"
        else:
            out_ter_state += "0"
    return out_ter_state


# checks if the number of an element in a column (not as easy to call as a row) is equal to a value
def col_count_val_check(the_matrix: list, col_index: int, element_to_count, the_value) -> bool:
    c_col = [cur_row[col_index] for cur_row in the_matrix]
    return c_col.count(element_to_count) == the_value


# makes sure that the col_count_val_check returns True for every column in the matrix
def check_el_count_mat(the_matrix: list, element_to_count, the_value):
    try:
        for col in range(0, len(the_matrix[0])):
            if not col_count_val_check(the_matrix, col, element_to_count, the_value):
                return False
        return True
    except:
        pdb.set_trace()
        

# a general coin problem solver

x = 3  # number of possible states (heavy, light, ot normal with only one bad coin, generalize later if it makes sense) 
n = 3#12  # number of coins
w = 2#3  # number of weighs

possible_outcomes = []

# generates all the possible states (001, 002 etc)
for c_num in range(1, x**w):
    possible_outcomes.append(pad_num(dec_to_base_b(c_num, x), x))
        
        
# gets an appropriate number of coin state assignments with no duplicates and inversions count!

# THIS IS FLAWED, THIS IS WRONG THIS IS VERY WRONG

states_to_use = []
for coin in range(0, n):
    for c_state in possible_outcomes:
        if c_state not in states_to_use and invert_ter_state(c_state) not in states_to_use:
            states_to_use.append(c_state)
            break        
          
            
# star bellied sneeches
# randomly flips inversions for non inversions until we have 4 of each entry in every row

ct = 0

while not check_el_count_mat(states_to_use, '1', int(n/3)):  # int floors
    coin_to_invert = np.random.randint(0, n)
    states_to_use[coin_to_invert] = invert_ter_state(states_to_use[coin_to_invert])

    if ct == 1000:
        print("WaRNING this is sketchy")
        print(states_to_use)
        
    if ct > 1000:
      states_to_use[coin_to_invert] = np.random.choice(possible_outcomes)
      
    ct += 1
  

print("states", states_to_use)
print("Chosen coin to invert", coin_to_invert)
print("Num coins", len(states_to_use))






        
        
        