def calculate(mass):
    return mass // 3 - 2

def go():
    with open('day1_INPUT.txt') as f:
        nums = f.read()
        total = 0
        stack = []
        working_stack = list(map(int, nums.split()))
        while working_stack != []:
            for num in working_stack:
                fuel = calculate(num)
                if fuel > 0:
                    total += fuel
                    stack.append(fuel)
            working_stack = stack[::]
            stack = []
    print(total)
