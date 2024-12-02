import heapq
from typing import Counter

class DayOne:
   def __init__(self):
      self.list1 = []
      self.list2 = []
      self.ans = 0
      self.ans2 = 0
      self.read_input()

   def read_input(self):
      with open('./Day1/input.txt', 'r') as file:
         lines = file.readlines()
      for line in lines:
         num1, num2 = map(int, line.split())
         self.list1.append(num1)
         self.list2.append(num2)
     
   def Solution(self):
      list1_copy = self.list1[:]
      list2_copy = self.list2[:]
      heapq.heapify(list1_copy)
      heapq.heapify(list2_copy)

      while list1_copy and list2_copy:
         num1 = heapq.heappop(list1_copy)
         num2 = heapq.heappop(list2_copy)
         self.ans += abs(num1 - num2)
   
   def SolutionPartTwo(self):
      list2_frequency = Counter(self.list2)

      for num in self.list1:
         if num in list2_frequency:
            self.ans2 += num * list2_frequency[num]