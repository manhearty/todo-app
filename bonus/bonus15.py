import json

with open("questions.json") as file:
    content = file.read()

data = json.loads(content)


for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)

    user_choice = int(input("Enter your Answer: "))
    question["user_choice"] = user_choice

score = 0

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct!"
    else:
        result = "Incorrect!"

    message = (f"{index + 1} {result} - Your Answer is: {question['user_choice']}"
               f" Correct Answer is: {question['correct_answer']}")
    print(message)

print(score, "/", len(data))
