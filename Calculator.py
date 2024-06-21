def sum(a,b):
  c=a+b
  print(c)
def dif(a,b):
  c=a-b
  print(c)
def muil(a,b):
  c=a*b
  print(c)
def div(a,b):
  c=a/b
  print(c)
def rem(a,b):
  c=a%b
  print(c)
print("1.sum\n2.Difference\n3.mulipication\n4.division\n5.reminder")
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
ch=int(input("Enter the choice:"))
if ch==1:
  sum(a,b)
elif ch==2:
  dif(a,b)
elif ch==3:
  muil(a,b)
elif ch==4:
  div(a,b)
elif ch==5:
  rem(a,b)
