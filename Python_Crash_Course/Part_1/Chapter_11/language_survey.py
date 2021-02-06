from Python_Crash_Course.Part_1.Chapter_11.survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit")
print()

while True:
    response = input("Languages: ")
    if response == "q":
        break
    else:
        my_survey.store_response(response)

print()
print("Thank you to everyone who participated in the survey!")
my_survey.show_results()
