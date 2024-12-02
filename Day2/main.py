class DayTwo:
   def __init__(self):
      self.data = []

   def read_input(self):
      with open('./Day2/input.txt', 'r') as file:
         self.data = [list(map(int, line.split())) for line in file]
   
   def Solution(self):
      pass 
