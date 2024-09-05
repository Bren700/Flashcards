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
            print(f'\nQuestion: {result_list[i].question}\n'
                  f'Please press "y" to see the answer or press "n" to skip:')
            ans = input()
            if ans == 'n':
                continue
            elif ans == 'y':
                print('\nAnswer:', result_list[i].answer)
        print()
        main()


main()