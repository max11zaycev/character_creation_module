class Human:
    def __init__(self, name):
        self.name = name

    # ответ по умолчанию для всех одинаковый, можно 
    # доверить его родительскому классу
    def answer_question(self, question):
        print("«Очень интересный вопрос! Не знаю.»")


class Student(Human):
    def  __init__(self, name):
        super().__init__(name)
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос; 
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        # напечатайте на экран вопрос в нужном формате
        print(f'{someone.name}, {question}')
        # запросите ответ на вопрос у someone
        someone.answer_question(someone.name, question)

        print()  # этот print выводит разделительную пустую строку	


class Curator(Human):
    def answer_question(self, question):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        if question == 'мне грустненько, что делать?':
        # если да - ответить на него
            print('Держись, всё получится. Хочешь видео с котиками?')
        # если нет - вызвать метод answer_question() у родительского класса
        else:
            print(super().answer_question)
# объявите и реализуйте классы CodeReviewer и Mentor

class CodeReviewer(Human):
    def answer_question(self, question):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        if question == 'мне грустненько, что делать?':
        # если да - ответить на него
            print('Держись, всё получится. Хочешь видео с котиками?')
        # если нет - вызвать метод answer_question() у родительского класса
        else:
            print(super().answer_question)
            
class Mentor(Human):
    def answer_question(self, question):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        if question == 'мне грустненько, что делать?':
        # если да - ответить на него
            print('Отдохни и возвращайся с вопросами по теории.')
        # если нет - вызвать метод answer_question() у родительского класса
        else:
            print(super().answer_question)


# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
#reviewer = CodeReviewer('Евгений')
#friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
#student1.ask_question(reviewer.name, 'когда каникулы?')
#student1.ask_question(reviewer.name, 'что не так с моим проектом?')
#student1.ask_question(friend.name, 'как устроиться на работу питонистом?')
#student1.ask_question(mentor.name, 'как устроиться работать питонистом?')