# awestover

"""
A common security method used for online banking is to ask the user for three random characters from a
passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the
expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the
shortest possible secret passcode of unknown length.
"""



nums = []

trys = []
file_loc = 'p79_keylog.txt'
txt_file = open(file_loc)
for row in txt_file:
    trys.append(row.replace('\n', '').replace(' ', '').split(''))
txt_file.close()

print(trys)

for atry in trys:
    lowest_index_allowed = 0
    for el in atry:
        for i in range(0, len(nums)):
            pass
