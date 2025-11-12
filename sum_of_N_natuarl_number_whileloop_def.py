#sum of first N natural number uding for loop
def sum(x):
  n=int(input("enter number: "))
  add=0
  i=1
  for i in range(n+1):
    add+=i
    i+=1
  return add
sum(n)
