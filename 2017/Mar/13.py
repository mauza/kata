import json

with open('quizData.json', 'r') as file:
	quiz_json = json.load(file)

message = "TASC Quiz\n\n"
for id, question in quiz_json['quiz']['questions'].iteritems():
	message = message + "{0}\nAnswer:{1}\n\n".format(question['question'], quiz_json['responses'][0]['questions'][id]['text'])

print(message)