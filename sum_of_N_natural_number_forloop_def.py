#sum of first N natural numbers using while loop
def sum(x):
  n=int(input("enter number: "))
  add=0
  i=1
  while i<=n:
    add+=i
    i+=1
  return add
sum(n)
