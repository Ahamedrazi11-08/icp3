class Employee:

   EmpCount = 0
   totalsalary=0

   def __init__(self, name,family,salary,department):
      self.name = name
      self.family=family
      self.salary = salary
      self.department=department
      Employee.EmpCount += 1
      Employee.totalsalary=Employee.totalsalary+salary





print("Employees are:")
class fulltimeemp(Employee):

    def display(self):
        print("Name:",self.name,"Family: ",self.family,"salary:",self.salary,"Department: ",self.department)

    def salary_average(self):
        self.averagesalary = (Employee.totalsalary / Employee.EmpCount)
        print("average salary is", self.averagesalary)
class Creation:
 emp1=fulltimeemp("john","A",100,"sales")
 emp1.display()

 emp2=fulltimeemp("rock","A",200,"sales")
 emp2.display()
 emp3=fulltimeemp("ravvi","A",300,"sales")
 emp3.display()
 emp3.salary_average()

