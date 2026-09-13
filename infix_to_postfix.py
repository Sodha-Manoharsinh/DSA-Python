from stack import Stack


infix = input() + ')'
stack = Stack(len(infix)*2)
stack.push("(")
polish = ""
rank = 0
next_index = 0
next = infix[next_index]

def stack_priority(x):
    priority = 0

    if x in ('+','-'):
        priority =  2
    elif x in ('*','/'):
        priority = 4
    elif x == "^":
        priority = 5
    elif x.isalnum():
        priority = 8
    elif x == '(':
        priority = 0

    return priority
    
def input_priority(x):
    priority = 0

    if x in ('+','-'):
        priority =  1
    elif x in ('*','/'):
        priority = 3
    elif x == "^":
        priority = 6
    elif x.isalnum():
        priority = 7
    elif x == '(':
        priority = 9
    elif x == ')':
        priority = 0

    return priority

def char_rank(x):
    if x in ('+','-','*','/','^'):
        return -1
    elif x.isalnum():
        return 1
    else:
        return 0

def next_char():
    global next_index
    next_index += 1
    try:
        return infix[next_index]
    except:
        return " "


while next != ' ':
    if stack.top < 0:
        print("Invalid")
        break
    while stack_priority(stack.stack[stack.top]) > input_priority(next):
        temp = stack.pop()
        polish = polish+temp
        rank += char_rank(temp)
        if rank < 1:
            print("Invalid")
            break

    if stack_priority(stack.stack[stack.top]) != input_priority(next):
        stack.push(next)
    else:
        stack.pop()

    next = next_char()

if stack.top != -1 or rank != 1 :
    print("Invalid")
else:
    print("Valid")

print(polish)