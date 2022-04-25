questions = [
    {
        "nums": [1, 2],
        "answer": 3,
        "modifier": "plus"
    },
    {
        "nums": [3, 4],
        "answer": 7,
        "modifier": "plus"
    },
    {
        "nums": [9, 9],
        "answer": 81,
        "modifier": "multiplied"
    }
]

score = 0
for question in questions:
    num1 = question["nums"][0]
    num2 = question["nums"][1]
    modifier = question["modifier"]
    answer = int(input(f"What is {num1} {modifier} {num2}? "))
    if answer == question["answer"]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
percent = (score / len(questions)) * 100
print(
    f"You got {score} correct out of {len(questions)} questions. Your score is {int(percent)} %")
