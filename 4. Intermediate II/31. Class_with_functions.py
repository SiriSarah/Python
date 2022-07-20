# Creation of new class, called Company
class Company:

    # __ indicates they are meant for internal use only
    def __init__(self, name):
        # self represents the class, we are calling from
        self.name = name
        self.courses = []

    # Interface to user, so they can add courses, without exposing the data structure
    def add_course(self, course):
        self.courses.append(course)

    # Providing an option to user to print the list of courses
    def print_course(self):
        for course in self.courses:
            print (course)
 
c = Company("SiriSarah LLC")
print(c.name)
c.add_course("Python")
# c.print_course()

c.add_course("Data Structures and Algorithms")
c.print_course()

c2 = Company("Google Careers")
print(c2.name)
c2.add_course("Project Management")
# c2.print_course()

c2.add_course("IT Support")
c2.print_course()

# To do: Create a new function, that prints the company name and the available courses in pretty format.