input1 = str(input("Input 1: "))
input2 = str(input("Input 2: "))
#input1 = ""
#input2 = ""
input1dict = []
input2dict = []
inputLarge = []
inputSmall = []

outputCorrect = ""
outputIncorrect = ""
index = 0
for i in input1:
    input1dict.append(str(i))
for i in input2:
    input2dict.append(str(i))
if len(input1dict) != len(input2dict):
    print("The inputs are different sizes - hopefully it isn't too bad")
    
if len(input1dict) < len(input2dict):
    inputLarge = input2dict
    inputSmall = input1dict
    print("Using Input 1 as base for comparison: ")
else:
    inputLarge = input1dict
    inputSmall = input2dict
    print("Using Input 2 as base for comparison: ")
    
for i in inputSmall:
    if i == inputLarge[index]:
        outputCorrect = outputCorrect + i
    else:
        outputCorrect = outputCorrect + "__error found__"
        outputIncorrect = outputIncorrect + "Input 1:" + "'" + i + "'" + "' Input 2:" + "'" + inputLarge[index] + "'"
    index = index + 1
print("Correct:", outputCorrect)
print("Differences:", outputIncorrect)
    