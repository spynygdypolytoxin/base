# Iterate array and return true if even 
 
def iterate_even(arr): 
  even = [] 
  for num in arr: 
    even.append(True if (num % 2 == 0) else False) 
  return even 
 
# Call function and print result 
sample = [5, 8, 12, 7, 13, 29, 58, 28, 30] 
print(iterate_even(sample))
