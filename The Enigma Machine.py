#disk 3 has characteristics to a plugboard. Plugboard characteristics are explained below
starting_position_disk1 = [26, 25, 20, 15, 24, 16, 18, 23, 17, 14, 19, 22, 21, 10,
                            4, 6, 9, 7, 11, 3, 13, 12, 8, 5, 2, 1]

starting_position_disk2 = [16, 14, 19, 18, 24, 22, 17, 26, 21, 23, 20, 25, 15, 2, 
                           13, 1, 7, 4, 3, 11, 9, 6, 10, 5, 12, 8]

starting_position_disk3 = [16, 14, 21, 23, 15, 24, 18, 19, 22, 25, 20, 26, 17, 2,
                            5, 1, 13, 7, 8, 11, 3, 9, 4, 6, 10, 12]

current_position_disk1 = starting_position_disk1.copy()
current_position_disk2 = starting_position_disk2.copy()
current_position_disk3 = starting_position_disk3.copy()

#plugboard parameters: "if the n-th number is m, then the m-th number is n".
plugboard = [16, 21, 25, 14, 23, 17, 26, 24, 19, 15, 18, 20, 22, 4, 10, 1, 6, 
             11, 9, 12, 2, 13, 5, 8, 3, 7]

wire_reversal_config = [23, 20, 16, 26, 14, 17, 15, 21, 18, 22, 19, 25, 24,
                         5, 7, 3, 6, 9, 11, 2, 8, 10, 1, 13, 12, 4]

def pass_thru_disk(num, disk):
    num = disk[num-1]
    return num

def pass_thru_plgbrd(num,plugboard = plugboard):
    num = plugboard[num-1]
    return num

def rotate_disks():
    def rotate(disk):
        disk.append(disk[0])
        del disk[0]
        for i in range(26):
            disk[i] -= 1
            if disk[i] == 0:
                disk[i] = 26
        return disk
    
    global current_position_disk1, current_position_disk2, current_position_disk3

    current_position_disk1 = rotate(current_position_disk1)
    if current_position_disk1 == starting_position_disk1:
        current_position_disk2 = rotate(current_position_disk2)
        if current_position_disk2 == starting_position_disk2:
            current_position_disk3 = rotate(current_position_disk3)

def char_charnum_interchanger(item):
    if isinstance(item, str):
        #in the system, a=1 but ord('a')=97.Similarly for the rest of the alphabets and hence below.
        outpt = ord(item) - 96
    else:
        outpt = chr(item+96)
    return outpt

while True:
    inpt = input('Input :').lower()
    print('Output:', end = '')

    for char in inpt:
        if not char.isalpha():
            print(char, end = '')
            continue 
        else: 
            rotate_disks()    

            char_num = char_charnum_interchanger(char)
            char_num = pass_thru_disk(char_num, current_position_disk1)
            char_num = pass_thru_disk(char_num, current_position_disk2)
            char_num = pass_thru_disk(char_num, current_position_disk3)
            char_num = pass_thru_disk(char_num, wire_reversal_config)
            char_num = pass_thru_disk(char_num, current_position_disk3)
            char_num = pass_thru_disk(char_num, current_position_disk2)
            char_num = pass_thru_disk(char_num, current_position_disk1)
            char = char_charnum_interchanger(char_num)

            print(char, end = '')
    print()