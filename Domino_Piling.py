def domino():
    dom = input()
    y = dom.split(' ')
    return (int(y[0]) * int(y[1])) // 2

print(domino())
