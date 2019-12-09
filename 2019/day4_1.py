def test(num_str):
    ident_adj = False
    for i in range(len(num_str) - 1):
        if num_str[i + 1] < num_str[i]:
            return False
        if num_str[i] == num_str[i + 1]:
            ident_adj = True
    return ident_adj

def go():
    # input is range [172851, 675869]
    count = 0
    for i in range(172851, 675870):
        num_str = str(i)
        if test(num_str):
            count += 1
    return count
