#!/usr/bin/python2
#a=[1,3,5,4,2, 6, 1]
#a = [ -1, 1, 2, 3, 4, 5, 6, 7, 0 ]
#a=[1,0,5,1,234,0,12,1,6,4,10, -1]
#a=[-1,0,5,1,5,234,234,0,12,1,6,4,10,-1]
a = range(6)
#a = [7] + range(1,2) + [0]
#a = [ 1, 2, 3, 2, 4, 1, 5 ]

def max_in_list(numbers, n=2):
  i = 0
  j = 1
  offset = 0

  print numbers
  while i < len(numbers)-1:
    number = numbers[i]

    if i != 0 and number >= numbers[0]:
      # send number to the start of the list 
      # if it is bigger than the first number in the list
      numbers.pop(i)
      numbers.insert(0, number) 
      i += 1
    elif number <= numbers[-1] and i != len(numbers) - 2:
      # move number to the end of the list
      # if it's smaller than the last item in the list
      numbers.pop(i)
      numbers.append(number)
    elif i != 0 and number > numbers[i-1]:
      # move number closer to the beginning of the list
      # if it's bigger than the previous one
      numbers.pop(i)
      numbers.insert(i-1, number) 
      i -= 1
      offset += 1
    else:
      # move to the next position in list
      # if no actions were done
      i += 1 + offset
      offset = 0

  return numbers[:n]

print max_in_list(a, 3)
