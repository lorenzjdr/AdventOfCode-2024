import re

class DayThree:
   def __init__(self):
      self.ans = 0
      self.matches = []
      self.pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
      self.read_input()

   def read_input(self):
      with open('./Day3/input.txt', 'r') as file:
         for line in file:
            match = re.findall(self.pattern, line)
            if match:
               for i in match:
                  numbers = (int(i[0]), int(i[1])) # numbers inside the pattern
                  self.matches.append(numbers) 
   
   def Solution(self):
      for j in self.matches:
         self.ans += j[0] * j[1]
   
   def SolutionPartTwo(self):
      pass