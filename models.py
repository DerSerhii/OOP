import datetime as dt


class Employee:

	def __init__(self, full_name, salary_day):
		self.full_name = full_name
		self.salary_day = salary_day

	def __lt__(self, other):
		salary_day = self.salary_day < other.salary_day
		return f"by salary per day comparison is {salary_day}"

	def __le__(self, other):
		salary_day = self.salary_day <= other.salary_day
		return f"by salary per day comparison is {salary_day}"

	def __gt__(self, other):
		salary_day = self.salary_day > other.salary_day
		return f"by salary per day comparison is {salary_day}"

	def __ge__(self, other):
		salary_day = self.salary_day >= other.salary_day
		return f"by salary per day comparison is {salary_day}"

	def __eq__(self, other):
		salary_day = self.salary_day == other.salary_day
		return f"by salary per day comparison is {salary_day}"

	def __ne__(self, other):
		salary_day = self.salary_day != other.salary_day
		return f"by salary per day comparison is {salary_day}"

	@staticmethod
	def work():
		return 'I come to the office'

	@staticmethod
	def calculation_business_day():
		""" Calculation of business days including the current day from the beginning of the month """

		current_day = dt.date.today()
		days, bus_days = current_day.day, 0

		# OPTION #1
		# for day in range(1, days + 1):
		#     if dt.datetime(current_day.year, current_day.month, day).weekday() < 5:
		#         bus_days += 1

		# OPTION #2
		while days > 0:
			if current_day.weekday() < 5:
				bus_days += 1
			current_day -= dt.timedelta(days=1)
			days -= 1

		return bus_days

	def check_salary(self, amount_day: int, current_salary: str = None):
		""" Default: defines the salary for the amount of days
			Passing the second argument "cur": defines the salary at the current moment from the beginning of the month
		"""
		if current_salary == "cur":
			return self.salary_day * self.calculation_business_day()
		return amount_day * self.salary_day


class Recruiter(Employee):

	def __str__(self):
		return f"{self.__class__.__name__}: {self.full_name}"

	@staticmethod
	def work():
		return 'I come to the office and start to hiring'


class Programmer(Employee):

	def __init__(self, full_name, salary_day, tech_stack):
		super().__init__(full_name, salary_day)
		self.tech_stack = tech_stack

	def __str__(self):
		return f"{self.__class__.__name__}: {self.full_name}"

	def __add__(self, other):
		if not isinstance(other, Programmer):
			return NotImplemented
		name = 'Alfa' + self.full_name + other.full_name
		salary_day = self.salary_day + other.salary_day
		tech_stack = ', '.join(sorted(set(self.tech_stack.split(', ') + other.tech_stack.split(', '))))
		return Programmer(name, salary_day, tech_stack)

	def __lt__(self, other):
		if not isinstance(other, Programmer):
			return NotImplemented
		salary_day = self.salary_day < other.salary_day
		tech_stack = len(self.tech_stack.split(", ")) < len(other.tech_stack.split(", "))
		return f"by the salary per day comparison is {salary_day} \nby the number of applied technologies comparison: {tech_stack}"

	def __le__(self, other):
		if not isinstance(other, Programmer):
			return NotImplemented
		salary_day = self.salary_day <= other.salary_day
		tech_stack = len(self.tech_stack.split(", ")) <= len(other.tech_stack.split(", "))
		return f"by salary per day comparison is {salary_day} \nby the number of applied technologies comparison: {tech_stack}"

	def __gt__(self, other):
		if not isinstance(other, Programmer):
			return NotImplemented
		salary_day = self.salary_day > other.salary_day
		tech_stack = len(self.tech_stack.split(", ")) > len(other.tech_stack.split(", "))
		return f"by salary per day comparison is {salary_day} \nby the number of applied technologies comparison: {tech_stack}"

	def __ge__(self, other):
		if not isinstance(other, Programmer):
			return NotImplemented
		salary_day = self.salary_day >= other.salary_day
		tech_stack = len(self.tech_stack.split(", ")) >= len(other.tech_stack.split(", "))
		return f"by salary per day comparison is {salary_day} \nby the number of applied technologies comparison: {tech_stack}"

	def __eq__(self, other):
		if not isinstance(other, Programmer):
			return NotImplemented
		salary_day = self.salary_day == other.salary_day
		tech_stack = len(self.tech_stack.split(", ")) == len(other.tech_stack.split(", "))
		return f"by salary per day comparison is {salary_day} \nby the number of applied technologies comparison: {tech_stack}"

	def __ne__(self, other):
		if not isinstance(other, Programmer):
			return NotImplemented
		salary_day = self.salary_day != other.salary_day
		tech_stack = len(self.tech_stack.split(", ")) != len(other.tech_stack.split(", "))
		return f"by salary per day comparison is {salary_day} \nby the number of applied technologies comparison: {tech_stack}"

	@staticmethod
	def work():
		return 'I come to the office and start to coding'


class Candidate:

	def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
		self.full_name = full_name
		self.email = email
		self.technologies = technologies
		self.main_skill = main_skill
		self.main_skill_grade = main_skill_grade


class Vacancy:

	def __init__(self, title, main_skill, main_skill_level):
		self.title = title
		self.main_skill = main_skill
		self.main_skill_level = main_skill_level


