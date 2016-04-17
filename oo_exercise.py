#Student class contains first,last names and addresses

class Student(object):
	"""Prints info of student"""

	def __init__ (self, first_name, last_name, address):
		self.first_name = first_name
		self.last_name = last_name
		self.address = address

#Questions are a question & correct answer

class Question(object):
	"""Questions and answers"""

	def __init__ (self, question, correct_answer):
		self.question = question
		self.correct_answer = correct_answer
		return self.question, self.correct_answer

	def ask_and_evaluate(self, question, correct_answer):
		"""Asks question and checks if answer is correct"""

		answer = raw_input('{} > '.format(question))

		if answer == correct_answer:
			return True 
		else: 
			return False

#Exams contain a body of questions and answers and has a label
class Exam(Question): 
	"""Exam body"""

	def __init__(self, name):
		self.questions = []
		self.name = name 

	def add_question(self, question, correct_answer):
		"""Adds question to exam body"""

		exam_q = super(Exam, self).__init__(question, correct_answer)
		self.questions.append(exam_q)

	def administer(self):
		"""Administers exam and prints score"""

		self.score = 0

		for i in range(len(self.questions)):
			exam_answer = self.ask_and_evaluate(self.questions[i][0],
												self.questions[i][1])

			if exam_answer == True:
				self.score += 1
			else:
				pass

			if i == (len(self.questions)-1):
				return self.score

			i = i+1

class Quiz(Exam):
	"""Quiz body"""

	#Initialize quiz instance with empty questions list and name quiz
	def __init__(self): 
		super(Quiz, self).__init__('Quiz')

	def add_quiz_question(self, question, correct_answer):
		"""Adds quiz questions to quiz body"""

		quiz_q = super(Quiz, self).add_question(question, correct_answer)

	def administer(self):
		"""Administers quiz and returns pass/fail"""
		
		half_of_questions = (len(self.questions) / 2.0)
		score = super(Quiz, self).administer()

		if score >= half_of_questions: 
			print True 
		else: 
			print False 


def take_test(exam, student):
	"""Administers an exam and assigns a score to the student"""

	score = exam.administer()
	student.score = score

def example():
	"""Create an exam and administer the exam to the student"""

	#Exam creation
	exam = Exam('Midterm')
	exam.add_question('What method do you use to add an item to a set?', '.add()')
	exam.add_question('What index number do sequences start at?', '0')
	exam.add_question('Why is the sky blue?', 'IDK!')

	#Student creation
	first_name = raw_input('What is your first name? ')
	last_name = raw_input('What is your last name? ')
	address = raw_input('What is your address? ')

	student = Student(first_name, last_name, address)

	#Administers exam to student
	exam.administer()

example()




















		

