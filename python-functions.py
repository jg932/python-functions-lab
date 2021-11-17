
# Challenge #1
def sum_to(n):
  sum = 0
  for n in range(1, n +1):
    sum += n
  return sum

print(sum_to(6))



# Challenge #2
def largest(list):
  list.sort()
  return list[-1]

print(largest([2,111,5,9,22,45,68]))



# Challenge #3
def occurances(string, string2):
  return string.count(string2)

print(occurances("This is a normal sentence", "e"))


# Challenge #4

def product(*nums):
  product = 1
  for num in nums:
    product *= num
  return product

print(product(2,2,10,3))