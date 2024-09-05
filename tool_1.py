questions = []
answers = []

def question_saver():
    print('Question:')
    input_question = input()
    if input_question.strip() == '':
        question_saver()
    else:
        questions.append(input_question)
        answer_saver()

def answer_saver():
    print('Answer:')
    input_answer = input()
    if input_answer.strip() == '':
        answer_saver()
    else:
        answers.append(input_answer)
        print()
        flashcard_menu2()

def flashcard_menu2():
    print("1. Add a new flashcard\n2. Exit")
    input_m1 = input()
    if input_m1 == '1':
        print()
        question_saver()
    elif input_m1 == '2':
        print()
        flashcard_main()
    else:
        print(f'\n{input_m1} is not an option\n')
        flashcard_menu2()

def flashcard_main():
    print("1. Add flashcards\n2. Practice flashcards\n3. Exit")
    input_1 = input()
    if input_1 == '1':
        print()
        flashcard_menu2()

    elif input_1 == '2':
        if not questions:
            print('\nThere is no flashcard to practice!\n')
            flashcard_main()
        else:
            for i in range(len(questions)):
                print(f'\nQuestion: {questions[i]}\n'
                      f'Please press "y" to see the answer or press "n" to skip:')
                ans = input()
                if ans == 'n':
                    continue
                elif ans == 'y':
                    print('\nAnswer:', answers[i])
            print()
            flashcard_main()

    elif input_1 == '3':
        print('\nBye!')
    else:
        print(f'\n{input_1} is not an option\n')
        flashcard_main()


flashcard_main()
