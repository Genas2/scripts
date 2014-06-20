#!/usr/bin/python
a=[1,0,5,1,234,0,12,1,6,4,10]

def max_in_list(numbers, n=2):
  result = [float("-inf")]

  for number in numbers: 
    if number > result[0]:
      result.insert(0, number) 
    else:
      i = 0
      while i < len(result):
        if result[i] <= number:
          result.insert(i, number)
          break
        i += 1

  result.pop()
  return result[:n]

print max_in_list(a, 15)
