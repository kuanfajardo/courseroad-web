from Graph import *

subjectMap = {
    "name": str,
    "number": str,
    "units": int
}

class Subject():
	entity_map = {
		"name": str,
		"number": str,
		"units": int
	}

	def __init__(self, name:str, number:str):
		self.name = name
		self.number = number

	# @staticmethod
	# def entity_map():
	# 	return subjectMap




g = Graph("TestGraph")

g.register_class(Subject)
# g.register_entity("subject", subjectMap)

def clause(classNumber, className):
	print(className, classNumber)
	def inner_clause(entity):
		print(entity.__dict__)
		return entity.number == classNumber and entity.name == className

	return inner_clause
	# return entity.number == "6.006"


def callback(satisfied):
	print(satisfied)

g.register_constraint("subject number", "Subject", clause)


#
# d = {
# 	"name": "Algorithms",
# 	"number": "6.006"
# }


s = Subject("Algorithms", "6.006")
subject = g.create_entity("Subject", s)


args = ("6.006", "Algorithms")
constraint = g.create_constraint("subject number", *args, callback=callback)

print(constraint.satisfied)
print(subject.name + subject.number)
