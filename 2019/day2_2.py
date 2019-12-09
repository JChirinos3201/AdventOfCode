def calculate(nums):
    for i in range(0, len(nums) // 4):
        index = i*4
        if nums[index] == 99:
            break
        elif nums[index] == 1:
            nums[nums[index + 3]] = nums[nums[index + 1]] + nums[nums[index + 2]]
        elif nums[index] == 2:
            nums[nums[index + 3]] = nums[nums[index + 1]] * nums[nums[index + 2]]
    return nums

def go():
    s = open('day2_INPUT.txt').read()
    nums = list(map(int, s.split(',')))
    for noun in range(99):
        for verb in range(99):
            temp_nums = nums[::]
            temp_nums[1] = noun
            temp_nums[2] = verb
            temp_nums = calculate(temp_nums)
            if temp_nums[0] == 19690720:
                print(noun, verb)
