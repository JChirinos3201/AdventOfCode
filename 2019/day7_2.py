# NOTE: I was too into the problem to remember to make a new file for day7_2, so day7_1 and day7_2
#       are unfortunately identical

#Intcode Computer 3.0

PRINT = 0
RETURN = 1

def calculate(nums, inp=None, output_type=PRINT, index=0):

    # opcode operations
    ops = {
        0: (lambda x: nums[nums[x]]),
        1: (lambda x: nums[x])
        }

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
            return inp[0], None, True
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
            if inp:
                nums[nums[index + 1]] = int(inp[0])
                inp = inp[1:]
            else:
                nums[nums[index + 1]] = int(input('Input: '))
            index += 2
        elif opcode == 4:
            out = ops[p1](index + 1)
            if output_type == PRINT:
                print(out)
                index += 2
            elif output_type == RETURN:
                index += 2
                return out, nums, index
        elif opcode == 5:
            if ops[p1](index + 1) != 0:
                index = ops[p2](index + 2)
            else:
                index += 3
        elif opcode == 6:
            if ops[p1](index + 1) == 0:
                index = ops[p2](index + 2)
            else:
                index += 3
        elif opcode == 7:
            if ops[p1](index + 1) < ops[p2](index + 2):
                nums[nums[index + 3]] = 1
            else:
                nums[nums[index + 3]] = 0
            index += 4
        elif opcode == 8:
            if ops[p1](index + 1) == ops[p2](index + 2):
                nums[nums[index + 3]] = 1
            else:
                nums[nums[index + 3]] = 0
            index += 4
        else:
            index += 1

def perm(l):
    if len(l) <= 1:
        yield l
    else:
        for p in perm(l[1:]):
            for i in range(len(l)):
                yield p[:i] + l[0:1] + p[i:]


class Amplifier:

    def __init__(self, instructions, computer):
        self.instructions = instructions
        self.computer = computer
        self.index = 0

    def calc(self, inp=None, output_type=PRINT):
        if output_type==RETURN:
            out, new_instructions, new_index = self.computer(self.instructions, inp, output_type, self.index)
            self.instructions = new_instructions
            self.index = new_index
            return out, new_index
        else:
            self.computer(self.instructions, inp, output_type)

def go():
    s = list(map(int, open('day7_INPUT.txt').read().strip().split(',')))
    out_dict = {}
    perms = perm((5, 6, 7, 8, 9))
    for p in perms:
        inp = 0
        perm_index = 0
        a, b, c, d, e = [Amplifier(s, calculate) for i in range(5)]
        l = [a, b, c, d, e]
        done = False
        while done != True:
            for i in range(5):
                if perm_index < 5:
                    inp, done = l[i].calc([p[perm_index], inp], RETURN)
                    perm_index += 1
                else:
                    inp, done = l[i].calc([inp], RETURN)
        out_dict[p] = inp
    out_list = list(out_dict.items())
    out_list = sorted(out_list, key=lambda x: x[1], reverse=True)
    print(out_list[0])
