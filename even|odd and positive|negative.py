#even/odd and positive/negative
x=int(input("enter the number"))
if x<0 and x%2==0:
  print("the number is even and negative")
elif x<0 and x%2!=0:
  print("the number is odd and negative")
elif x>0 and x%2==0:
  print("the number is even and positive")
else:
  print("the number is odd and positive")
