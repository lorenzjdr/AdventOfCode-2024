import re

class DayThree:
   def __init__(self):
      self.ans = 0
      self.ans2 = 0
      self.matches = []
      self.matches2 = []
      self.pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
      self.read_input()

   def read_input(self, do_rule=False):
      with open('./Day3/input.txt', 'r') as file:
         data = file.read()
           
      if do_rule:
         # anything after a dont() but before a do() is replaced with -
         # (.|\n)*? match any char or newline * times
         data = re.sub(r"don't\(\)(.|\n)*?do\(\)", "-", data)
          
      for line in data.splitlines():
         match = re.findall(self.pattern, line)
         if match:
            for i in match:
               numbers = (int(i[0]), int(i[1])) # numbers inside the pattern
               if do_rule:
                  self.matches2.append(numbers)
               else:
                  self.matches.append(numbers)
   
   def Solution(self):
      for j in self.matches:
         self.ans += j[0] * j[1]
   
   def SolutionPartTwo(self):
      self.read_input(do_rule=True)
      for x in self.matches2:
         self.ans2 += x[0] * x[1]
