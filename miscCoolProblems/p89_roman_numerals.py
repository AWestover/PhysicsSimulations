# Alek Westover
# reads in a large text file of roman numerals and cconverts them into minimalist form


file_loc = "p89_in.txt"
nums = []
with open(file_loc) as f:
    for row in f:
        nums.append(row.replace('\n', '').replace(' ', ''))

conversions = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# turns a roman numeral number (not nececarily completely reduced) into a decimal number
def roman_to_decimal(roman):
    pass
