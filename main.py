str = 'My name is Krihna'
split_val = []
temp = ''
for i in str:
    if i == ' ':
        split_val.append(temp)
        temp = ''
    else:
        temp+=i

if temp:
    split_val.append(temp)


def reverse(str):
    strs = ''
    for i in str:
        print(i)
        strs = i+strs
    return strs 

print(reverse(str))    
print(split_val)