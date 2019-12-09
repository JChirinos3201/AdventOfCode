def calculate(mass):
    return mass // 3 - 2

def go():
    with open('day1_INPUT.txt') as f:
        nums = f.read()
        total = 0
        for num in nums.split():
            total += calculate(int(num))
    print(total)
