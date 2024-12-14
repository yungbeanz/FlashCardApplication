#!/usr/bin/python
import random
import json
from colorama import Fore

# The purpose of this program is to provide Chris with a more interactive way to study, as traditional methods are quite nail-on-chalboard.
class FlashCardApplication:
	# Import JSON file containing flashcard data.
	with open('data.json') as f:
		output_data = json.load(f)

	# Get unit names.
	unitNames = output_data["units"]
	print(' Unit names are : ')
	for i in unitNames:
		print('' + i)
	selectedUnit = ''
	while selectedUnit not in unitNames:
		selectedUnit = input(' Please Choose a Unit: ')
		if selectedUnit in unitNames:
			print(f' Valid selection, you have selected: {selectedUnit}')
			break
		else:
			print(' Please select a valid Unit.')

	answers = output_data[selectedUnit]["answers"]
	questions = output_data[selectedUnit]["questions"]

	# Logic
	# The logic will consist of picking a random question, assigning 4 answers, having atleast one being correct.
	# The game will continue until the number of guesses is equal to the total number of answers.
	guesses = 0
	correctAnswers = 0
	totalAnswers = 0

	# Find number of total answers.
	for i in range(0, len(answers)):
		for j in range(0, len(answers[i])):
			totalAnswers += 1
	# Print out title of loaded module.
	print('\n ' + Fore.RED + selectedUnit + Fore.WHITE)
	# Collect username.
	userName = input(' Please enter your name: \n ')

	# Main logic loop.
	while guesses < totalAnswers:
		usedAnswers = []
		# Pick a random question.
		currentQuestionNum = random.randrange(0, len(questions))
		correctAnswer = ''

		# Generate 3 answers, atleast one correct.
		randomCorrectAnswerNum = random.randrange(0, 4)
		createdQuestions = 0
		while createdQuestions < 4:
			# Avoid repeats of the same correct answer.
			randomAnswerNum = random.randrange(0, len(answers))
			while randomAnswerNum == currentQuestionNum:
				randomAnswerNum = random.randrange(0, len(answers))
			# Find random correct answer out of list of correct answers for currentQuestion.
			if createdQuestions == randomCorrectAnswerNum:
				correctAnswer = answers[currentQuestionNum][random.randrange(0,len(answers[currentQuestionNum]))]
				usedAnswers.append(correctAnswer)
				createdQuestions += 1
			# Fill the other three answers with random incorrect answers. Also logic for avoiding repeats of answers.
			elif randomAnswerNum != randomCorrectAnswerNum:
				randomAnswer = answers[randomAnswerNum][random.randrange(0,len(answers[randomAnswerNum]))]
				while randomAnswer in usedAnswers:
					for i in range(0, len(answers[randomAnswerNum])):
						randomAnswer = answers[randomAnswerNum][random.randrange(0,len(answers[randomAnswerNum]))]
						if randomAnswer not in usedAnswers:
							break
						elif  i == len(answers[randomAnswerNum]) - 1:
							randomAnswerNum = random.randrange(0, len(answers))
							continue
				usedAnswers.append(randomAnswer)
				createdQuestions += 1

		# Printing score and questions/answers..
		print(Fore.MAGENTA + '-------------------------------------------------------------' + Fore.WHITE)
		print(' ' + userName + ', Score: ' + str(correctAnswers) + ' / ' + str(totalAnswers))
		print(f' {questions[currentQuestionNum]}\n 1. {usedAnswers[0]}\n 2. {usedAnswers[1]}\n 3. {usedAnswers[2]}\n 4. {usedAnswers[3]}')
		print('------------------------------')

		# Input logic, and playerguess logic.
		try:
			playerGuessNum = int(input(" What's your answer? (1-4)\n "))
			if playerGuessNum > 4 or playerGuessNum < 0:
				print(Fore.RED + ' Please enter a valid number (1-4)!' + Fore.WHITE)
				playerGuessNum = int(input(' '))
		except ValueError:
			print(Fore.RED + ' Please enter a valid number (1-4)!' + Fore.WHITE)
			playerGuessNum = int(input(' '))
		finally:
			# Incrementing guesses, changing playerGuessNum to accurately compare to correct answer.
			guesses += 1
			playerGuessNum -= 1

			# Logic for player's answer.
			print('------------------------------')
			print(f' You guessed: {usedAnswers[playerGuessNum]}')
			if playerGuessNum == randomCorrectAnswerNum:
				print(Fore.GREEN + ' Congratulations!' + Fore.YELLOW + ' +1 Score' + Fore.WHITE)
				correctAnswers += 1
			else:
				print(Fore.RED + ' Incorrect,' + Fore.WHITE + ' the correct answer was: ')
				print(' ' + Fore.BLUE + correctAnswer + Fore.WHITE)
			continue
