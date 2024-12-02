class DayTwo:
   def __init__(self):
      self.data = []
      self.ans = 0 
      self.ans2 = 0
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

   def SolutionPartTwo(self):
      def is_safe_sequence(level):
         is_increasing = level[0] < level[1]
         
         for i in range(1, len(level)):
            if is_increasing and level[i] <= level[i-1]:
               return False
            elif not is_increasing and level[i] >= level[i-1]:
               return False
            elif abs(level[i] - level[i-1]) > 3:
               return False
         return True

      for level in self.data:
         # first check without altering the level
         if is_safe_sequence(level):
            self.ans2 += 1
         else:
            for i in range(len(level)):
               # skip the current number
               if is_safe_sequence(level[:i] + level[i+1:]):
                  self.ans2 += 1
                  break
