def calculate(nums):

    # opcode operations
    ops = {
        0: (lambda x: nums[nums[x]]),
        1: (lambda x: nums[x])
        }
    
    index = 0
    while index < len(nums):

        # t is the opcode and all the parameter modes (defaulted to 0)
        t = str(nums[index])
        t = '0' * (5 - len(t)) + t

        opcode = int(t[3:])
        p1 = int(t[2])
        p2 = int(t[1])
        p3 = int(t[0])
        
        if opcode == 99:
            break
        # we use a dict ops to store the operation each mode requires
        # mode 0 is position mode, so we want nums[nums[x]]
        # mode 1 is immediate mode, so we want nums[x]
        elif opcode == 1:
            nums[nums[index + 3]] = ops[p1](index + 1) + ops[p2](index + 2)
            index += 4
        elif opcode == 2:
            nums[nums[index + 3]] = ops[p1](index + 1) * ops[p2](index + 2)
            index += 4
        elif opcode == 3:
            nums[nums[index + 1]] = int(input('Input: '))
            index += 2
        elif opcode == 4:
            out = ops[p1](index + 1)
            print(out)
            index += 2
    return nums

def go():
    s = open('day5_INPUT.txt').read()
    nums = list(map(int, s.split(',')))
    nums = calculate(nums)
