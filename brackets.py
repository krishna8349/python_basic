def checkbrackets(n):
    stack = []

    for i in n:
        if i =='(' or i=='{' or i=='[':
            stack.append(i)
        else:
            if not stack:
                print(n,'Invelid')
                return
            else:
                top = stack[-1]
                if i == ')' and top == '(' or i  == '}' and top=='{' or i==']' and top=='[':        
                    stack.pop()
                else:
                    print(n,'Invelid')
                    return
    if not stack:
        print(n,'valid')
    else:
        print(n,'invelid')

n = "{{}}()[]"
checkbrackets(n)