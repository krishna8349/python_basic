sentence = "hi my name is krishna"

words = sentence.split()
average = sum(len(word) for word in words)/ len(words)

print(average)