class DayOne:
   def __init__(self):
      self.list1 = []
      self.list2 = []
      self.ans = 0
      self.read_input()

   def read_input(self):
      with open('./Day1/input.txt', 'r') as file:
         lines = file.readlines()
      for line in lines:
         num1, num2 = map(int, line.split())
         self.list1.append(num1)
         self.list2.append(num2)
   
   def Solution(self):
      pass