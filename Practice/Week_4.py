# week 4
# sampleSet = {"Yellow", "Orange", "Black"}
# sampleSet.discard("Blue")
# print(sampleSet)

# sampleSet = {"Yellow", "Orange", "Black"}
# sampleSet.discard("Orange")
# print(sampleSet)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z) 

# aSet = {1, 'PYnative', ('abc', 'xyz'), True}
# print(aSet)

# sampleSet = {"Yellow", "Orange", "Black"}
# sampleSet.add("Blue")
# sampleSet.add("Orange")
# print(sampleSet)
# sampleSet = {"Yellow", "Orange", "Black"}
# print(sampleSet[1])

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 10, 30, 40, 80, 20, 50}
# print(set1.issubset(set2))
# print(set2.issuperset(set1))

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.union(y)
# print(z) 

# set1 = {"Yellow", "Orange", "Black"}
# set2 = {"Orange", "Blue", "Pink"}
# set3 = set2.difference(set1)
# print(set3)

# set1 = {10, 20, 30, 40}
# set2 = {50, 20, "10", 60}
# set3 = set1.union(set2)
# print(set3)


# set2 = set1
# print(set2)

# sampleSet = {"Yellow", "Orange", "Black"}
# sampleSet.update(["Blue", "Green", "Red"])
# print(sampleSet)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "facebook"}
# z = x.isdisjoint(y)
# print(z) 

# set1 = {"Yellow", "Orange", "Black"}
# set2 = {"Orange", "Blue", "Pink"}
# set1.difference_update(set2)
# print(set1)

# aSet = {1, 'PYnative', ['abc', 'xyz'], True}
# print(aSet)

# dict1 = {"name": "Mike", "salary": 8000}
# temp = dict1.get("age")
# print(temp)

# dict2 = dict(dict1)
# print(dict2)
# dict2 = dict1
# print(dict2)
# dict2 = dict1.copy()
# print(dict2)

# sampleDict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# sampleDict['class']['student']['marks']['history']
# print(sampleDict)

# dict1 = {"name": "Mike", "salary": 8000}
# temp = dict1.pop("age")
# print(temp)

# sampleDict = dict()
# print(sampleDict)
# sampleDict = {}
# print(sampleDict)



# student = { 
#   "name": "Emma", 
#   "class": 9, 
#   "marks": 75 
# }
# student.clear()
# print(student)


# student = {
#   "name": "Emma",
#   "class": 9,
#   "marks": 75
# }
# m = student.get('marks')
# print(m)

# sampleDict = dict([
#     ('first', 1),
#     ('second', 2),
#     ('third', 3)
# ])
# print(sampleDict)

# student = { 
#   "name": "Emma", 
#   "class": 9, 
#   "marks": 75 
# }
# del student["marks"]
# print(student)
# student.pop("marks")
# print(student)

# student = {1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
#            2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}}
# print(student[1]["age"])

# dick={}
# print(type(dick))

# import time 
# seconds_for_sleep = 4
# name = str(input("Username"))
# time.sleep(int(seconds_for_sleep))
# print("See! This fuction waited", seconds_for_sleep," seconds!`enter code here`")

# class Sales:
#     def __init__(self, id):
#         self.id = id
#         id = 100

# val = Sales(123)
# print (val.id)

# s = "\t\tWelcome\n"
# print(s.strip())

# class Person:
#     def __init__(self, id):
#         self.id = id

# sam = Person(100)
# sam.__dict__['age'] = 49
# print (sam.age + len(sam.__dict__))

# class A:
#     def __init__(self, i = 0):
#         self.i = i

# class B(A):
#     def __init__(self, j = 0):
#         self.j = j

# def main():
#     b = B()
#     print(b.i)
#     print(b.j)

# main()

# class A:
#     def __init__(self):
#         self.calcI(30)
#         print("i from A is", self.i)

#     def calcI(self, i):
#         self.i = 2 * i;

# class B(A):
#     def __init__(self):
#         super().__init__()
        
#     def calcI(self, i):
#         self.i = 3 * i;

# b = B()







