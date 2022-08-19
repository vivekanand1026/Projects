
def solution(S):
    temp = [i for i in S.split(',')]
    avg = []
    for i in temp:
        try:
            i = float(i)
            avg.append(i)
        except:
            pass
    if len(avg) == 0:
        return 0
    else:
        result = sum(avg) / len(avg)
        result = int(result)
        return result
		
		

# Online Python - IDE, Editor, Compiler, Interpreter

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')