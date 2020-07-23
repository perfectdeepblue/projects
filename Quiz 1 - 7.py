import random

class QA:
    def __init__(self, question, correctAnswer, otherAnswers):
        self.question = question
        self.corrAnsw = correctAnswer
        self.otherAnsw = otherAnswers

random_list = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
ran_list_1_7 = ['False', 'None', 'True', 'and', 'as', 'assert', 'async']

shuffle_truffle = random.shuffle(ran_list_1_7)

qaList = [QA(f"They are the results of comparison operations or logical (Boolean) operations in Python.", "True, False", shuffle_truffle)]

random.shuffle = qaList

corr_count = 0

for qaItem in qaList:
    print(qaItem, qaList)

print("Possible answers are:")
possible = qaItem.otherAnsw + [qaItem.corrAnsw]
random.shuffle(possible)
count = 0
while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1


