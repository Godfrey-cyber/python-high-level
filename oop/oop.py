# se1 = ["Godfrey", "Max", 20, "Junior", 5000]
# se1 = ["Lisa", "Max", 25, "Senior", 7000]

# a classs is a blueprint of 

class SoftwareEngineer:
	def __init__(self, name, age, level, salary):
		self.name = name
		self.age = age
		self.level = level
		self.salary = salary

	def code(self):
		print(f"Hello {self.name}")

	def code_in_languages(self, language):
		print(f"{self.name} is coding in {language}")

	# def infor(self):
	# 	info = f"name = {self.name}, age = {self.age}, level = {self.level}"
	# 	return info

	def infor(self):
		info = f"name = {self.name}, age = {self.age}, level = {self.level}"
		return info

se1 = SoftwareEngineer("Godfrey", 20, "Junior", 5000)
se2 = SoftwareEngineer("Lisa", 24, "Senior", 7000)

print(f"{se1.name} is a {se1.level} software Engineer with a salary of {se1.salary}")
print(f"{se2.name} is a {se2.level} software Engineer with a salary of {se2.salary}")

se1.code()
se2.code()
se1.code_in_languages("Python")
se2.code_in_languages("C")
print(se2.infor())
print(se1.infor())
# print(se2)