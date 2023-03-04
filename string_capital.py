name = 'my name is krishna'
words = name.split(' ')
print(words)
cap_word = []
for i in words:
    title = i[0].upper()+i[1:]
    cap_word.append(title)

output = ' '.join(cap_word) 

print(output)
# print(name.title())