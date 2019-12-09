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
    nums[1] = 12
    nums[2] = 2
    nums = calculate(nums)
    print(nums[0])
