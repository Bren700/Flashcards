from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Flashcards(Base):
    __tablename__ = 'flashcard'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    box = Column(Integer, default=1)

Base.metadata.create_all(engine)

def main():
    input_1 = input("1. Add flashcards\n2. Practice flashcards\n3. Exit\n")
    if input_1 == '1':
        menu_2()
    elif input_1 == '2':
        practice_flashcards()
    elif input_1 == '3':
        print('\nBye!')
    else:
        print(f'\n{input_1} is not an option\n')
        main()

def menu_2():
    input_2 = input("\n1. Add a new flashcard\n2. Exit\n")
    while input_2 != '1' and input_2 != '2':
        print(f'\n{input_2} is not an option\n')
        input_2 = input("\n1. Add a new flashcard\n2. Exit\n")
    if input_2 == '1':
        print()
        add_flashcard()
    else:
        print()
        main()

def add_flashcard():
    input_question = input('Question: \n')
    if input_question.strip() == '':
        add_flashcard()
    else:
        input_ans = input('Answer: \n')
        while input_ans.strip() == '':
            input_ans = input('Answer: \n')
        new_data = Flashcards(question=input_question, answer=input_ans)
        session.add(new_data)
        session.commit()
        menu_2()

def practice_flashcards():
    result_list = session.query(Flashcards).all()
    if not result_list:
        print('\nThere is no flashcard to practice!\n')
        main()
    else:
        for i in range(len(result_list)):
            while (selection := input(f'\nQuestion: {result_list[i].question}:\n'
                                  f'press "y" to see the answer:\n'
                                      f'press "n" to skip:\npress "u" to update:\n')) not in ('y', 'n', 'u'):
                print(f'\n{selection} is not an option\n')
            if selection == 'n':
                continue
            elif selection == 'y':
                print('\nAnswer:', result_list[i].answer)
                while (correct_incorrect := input('\npress "y" if your answer is correct:\n'
                                                  'press "n" if your answer is wrong:\n')) not in ('y', 'n'):
                    print(f'\n{correct_incorrect} is not an option\n')
                if correct_incorrect == 'n':
                    entry = result_list[i]
                    entry.box = 1
                    session.commit()
                elif correct_incorrect == 'y':
                    entry = result_list[i]
                    if entry.box < 3:
                        entry.box += 1
                        session.commit()
                    elif entry.box == 3:
                        session.delete(entry)
                        session.commit()

            elif selection == 'u':
                while (update_card := input('\npress "d" to delete the flashcard:\n'
                                        'press "e" to edit the flashcard:\n')) not in ('d', 'e'):
                    print(f'\n{update_card} is not an option\n')

                if update_card == 'd':
                    entry = result_list[i]
                    session.delete(entry)
                    session.commit()
                else:
                    new_question = input(f'\ncurrent question: {result_list[i].question}\nplease write a new question:\n')
                    new_ans = input(f'\ncurrent answer: {result_list[i].answer}\nplease write a new answer:\n')
                    if new_question.strip() == '' or new_ans.strip() == '':
                        continue
                    else:
                        entry = result_list[i]
                        entry.question = new_question
                        entry.answer = new_ans
                        session.commit()
        print()
        main()


main()