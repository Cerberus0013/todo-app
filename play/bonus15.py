import json

with open("questions.json", "r") as file:
    content = file.read()

print(content)

data = json.loads(content)

print(data)

score = 0

for question in data:
    print(question["question_text"])
    for index, alt in enumerate(question["alternatives"]):
        print(index + 1, "-", alt)

    user_answer = int(input("Enter Answer: "))
    question["user_choice"] = user_answer
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1

for question in data:
    message = f"Your answer was: {question['user_answer']}, Correct Answer was questions {question['correct_answer']}"

print("Your score is", score, "/", len(data))
