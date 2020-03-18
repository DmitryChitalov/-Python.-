START = int(input("Start\n"))
END = int(input("End\n"))

RESULT = []

def check(result , new_el):

    for el in result:
        if new_el % el == 0:
            return False
    return True


def simple_numbers(start, end):
    global RESULT
    for i in range(start, end + 1):
        if check(RESULT, i):
            RESULT.append(i)

if  START > 2:
    simple_numbers(2, START)
    PR_LEN = len(RESULT)
    simple_numbers(START, END)
else:
    PR_LEN = 0
    simple_numbers(START, END)



print(RESULT[PR_LEN:])