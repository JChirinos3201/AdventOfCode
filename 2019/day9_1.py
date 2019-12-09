# Day 2 just required a new user input, not a new file

# Intcode Computer 4.0

PRINT = 0
RETURN = 1

def calculate(nums, inp=None, output_type=PRINT, index=0):

    relative_base = 0

    # opcode operations as functions rather than lambdas in a dict
    # because I needed setters not just getters
    
    def mode_set(mode, index, val):
        nonlocal nums
        nonlocal relative_base
        
        if mode == 0:
            check_size(nums[index])
            nums[nums[index]] = val
        elif mode == 1:
            check_size(index)
            nums[index] = val
        elif mode == 2:
            check_size(relative_base + nums[index])
            nums[relative_base + nums[index]] = val

    def mode_get(mode, index):
        nonlocal nums
        nonlocal relative_base

        if mode == 0:
            check_size(nums[index])
            return nums[nums[index]]
        elif mode == 1:
            check_size(index)
            return nums[index]
        elif mode == 2:
            check_size(relative_base + nums[index])
            return nums[relative_base + nums[index]]

    def check_size(index):
        nonlocal nums

        if index > len(nums) - 1:
                nums += [0]*(index - len(nums) + 1)

    while index < len(nums):

        # t is the opcode and all the parameter modes (defaulted to 0)
        t = str(nums[index])
        t = '0' * (5 - len(t)) + t

        opcode = int(t[3:])
        p1 = int(t[2])
        p2 = int(t[1])
        p3 = int(t[0])

        # when it halts, it returns the input and True as the index and just breaks i guess
        if opcode == 99:
            return
        # we use a dict ops to store the operation each mode requires
        # mode 0 is position mode, so we want nums[nums[x]]
        # mode 1 is immediate mode, so we want nums[x]
        elif opcode == 1:
            val = mode_get(p1, index + 1) + mode_get(p2, index + 2)
            mode_set(p3, index + 3, val)
            index += 4
        elif opcode == 2:
            val = mode_get(p1, index + 1) * mode_get(p2, index + 2)
            mode_set(p3, index + 3, val)
            index += 4
        elif opcode == 3:
            if inp:
                val = int(inp[0])
                mode_set(p1, index + 1, val)
                inp = inp[1:]
            else:
                val = int(input('Input: '))
                mode_set(p1, index + 1, val)
            index += 2
        elif opcode == 4:
            out = mode_get(p1, index + 1)
            if output_type == PRINT:
                print(out)
                index += 2
            elif output_type == RETURN:
                index += 2
                return out, nums, index
        elif opcode == 5:
            if mode_get(p1, index + 1) != 0:
                index = mode_get(p2, index + 2)
            else:
                index += 3
        elif opcode == 6:
            if mode_get(p1, index + 1) == 0:
                index = mode_get(p2, index + 2)
            else:
                index += 3
        elif opcode == 7:
            if mode_get(p1, index + 1) < mode_get(p2, index + 2):
                mode_set(p3, index + 3, 1)
            else:
                mode_set(p3, index + 3, 0)
            index += 4
        elif opcode == 8:
            if mode_get(p1, index + 1) == mode_get(p2, index + 2):
                mode_set(p3, index + 3, 1)
            else:
                mode_set(p3, index + 3, 0)
            index += 4
        elif opcode == 9:
            relative_base += mode_get(p1, index + 1)
            index += 2
        else:
            print('wack')
            return
        

def go():
    s = open('day9_INPUT.txt').read().strip()
    s = s.split(',')
    s = list(map(int, s))
    calculate(s)
