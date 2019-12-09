import re

def test(num_str):
    for i in range(len(num_str) - 1):
        if num_str[i + 1] < num_str[i]:
            return False
    for i in range(10):
        testing = str(i)
        if re.search(testing + '{2}', num_str) and not re.search(testing + '{3,}', num_str):
            return True
    return False

def go():
    # input is range [172851, 675869]
    count = 0
    for i in range(172851, 675870):
        num_str = str(i)
        if test(num_str):
            count += 1
    return count
