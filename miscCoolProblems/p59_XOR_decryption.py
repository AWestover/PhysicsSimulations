# something is wrong with this, I am not sure what though

"""
A modern encryption method is to
take a text file,
convert the bytes to ASCII,
then XOR each byte with a given value,
taken from a secret key.

The key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security,
but short enough to be memorable.

The encryption key consists of three lower case characters.

Using cipher.txt,
a file containing the encrypted ASCII codes,
and the knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.

"""

# Alek westover
# interesting notes:
# XOR is commutative (order of application does not matter) ie. a XOR b = b XOR a
# a XOR a = 0 since all bitwise digits line up so it is gaurenteed never to get a 1
# b XOR 0 = b because all digits of 0 are 0 so whenever b has zero in its binary representation so does the XOR, and all other times b and the XOR have 1s
# a XOR (b XOR a) = b XOR a XOR a = b


# libraries
import itertools
from nltk.corpus import wordnet
from nltk.corpus import words
print(len(words.words())) # an ordered list of all english words

from tkinter import messagebox
import tkinter as tk
import pdb

root = tk.Tk()
root.withdraw()

# checks if something is a real word
# this is really pretty slow...
def is_english_word(word):
    return len(wordnet.synsets(word)) > 0

# performs xor on to binary strings
def xor(num1, num2):
    return ''.join(map(lambda z: xor_bits(z[0], z[1]), zip(list(pad_num(num1, len(num2))), list(pad_num(num2, len(num1))))))

# returns the XOR of two bits
# exclusive or means that they must be different
def xor_bits(bit1, bit2):
    if bit1 != bit2:
        return '1'
    else:
        return '0'

# turns a decimal number into base 2 by repeated division and noting remainders
def dec_to_binary(num):
    binary_num = ''
    while num > 0:
        res = divmod(num, 2)
        binary_num = str(res[1]) + binary_num
        num = res[0]
    return binary_num

# turns a binary string into a decimal number
def binary_to_dec(binary):
    dec = 0
    for i in range(0, len(binary)):
        dec += int(binary[i])*2**(len(binary)-i-1)
    return dec

# turns an ascii phrase into a list of binary comma seperated values
def to_ascii(word):
    # apply ord() to each character to find its ascii value, and then combine them with commas
    return ','.join(map(lambda x: str(ord(x)), list(word)))

# pads a number up to the right length with padding zeros
def pad_num(a, leng):
    return '0'*(leng-len(a)) + a

# does a decimal xor without showing you all those nasty binary numbers
def dec_xor(a, b):
    return binary_to_dec(xor(dec_to_binary(a), dec_to_binary(b)))

# figures out whether a particular binary value is between two ascii values that are english letters
def valid_char(binary):
    db = binary_to_dec(binary)
    return (97 <= db <= 122) or (65 <= db <= 90) or db == 32 or db == 33 or db == 46


# here is what has been done

# Euler made a plain text file
# txt file bytes -> ascii codes
# ascii codes XORED with password (which is an ascii code for a word)


# reads in the text file
ascii_transs = []
file_loc = 'p59_cipher.txt'
txt_file = open(file_loc)
for row in txt_file:
    ascii_transs += row.replace('\n', '').replace(' ', '').split(',')
txt_file.close()
ascii_transs = [dec_to_binary(int(ascii_trans)) for ascii_trans in ascii_transs]


# for every password guess
# XOR each thing with the guess
# if the first word in the doc is now english add it to a list that we will output to a text file
# look at the list

# constants and things to loop over
password_length = 3
possible_binary_nums = [dec_to_binary(num) for num in range(97, 123)]
all_combos = set(itertools.permutations(possible_binary_nums, password_length))
flags = []


# something sketch happens, get the marked legit ones and then investigate those...
for password in all_combos:
    out_message = []
    for i in range(0, len(ascii_transs)):
        # password ascii values cycled through message, use a different value of password everytime, but does repeat
        out_message.append(xor(password[i % password_length], ascii_transs[i]))
        if not valid_char(out_message[-1]):
            break
        elif i == len(ascii_transs) - 1:
            flags.append(password)
            print("asdf")
            messagebox.showinfo(password, ''.join(map(chr, map(binary_to_dec, out_message))))


# does not seem practical ...
