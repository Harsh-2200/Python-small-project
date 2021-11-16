import wikipedia


Quesation = input('Enter Your Quesation to search on wikipedia :  ')


result = wikipedia.page(Quesation)
print(result.summary)



