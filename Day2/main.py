class DayTwo:
   def __init__(self):
      self.data = []
      self.ans = 0 
      self.read_input()

   def read_input(self):
      with open('./Day2/input.txt', 'r') as file:
         self.data = [list(map(int, line.split())) for line in file]
   
   def Solution(self):
      # If the number is equal, it is not safe
      # If the numbers difference is > 3 it is not safe

      for level in self.data:
         is_increasing = level[0] < level[1]
         safe = True
      
         for i in range(1, len(level)):
            if is_increasing and level[i] <= level[i-1]:
               safe = False
               break
            elif not is_increasing and level[i] >= level[i-1]:
               safe = False
               break
            elif abs(level[i] - level[i-1]) > 3:
               safe = False
               break
            else:
               continue
         if safe:
            self.ans += 1