age=int(input())
yop=int(input())
i=int(input())
supply=int(input())
score=float(input())
att=float(input())
if age>=18 and age<21:
  if yop>=2021:
    if i<=200000:
      if supply<=2:
        if score>=60 and att>=80:
          print("Eligible")
        else:
          print("Not Eligible")
      else:
        if score>=80 and att>=90:
          print("Partially Eligible")
        else:
          print("Not Eligible")
    elif i>200000 and i<250000:
      if supply<=2:
        if score>=60 and att>=80:
          print("Partially Eligible")
        else:
          print("Not Eligible")
      else:
        if score>=80 and att>=90:
          print("Partially Eligible")
        else:
          print("Not Eligible")
    else:
      print("Not Eligible")
  else:
    print("Not Eligible")
else:
  print("Not Eligible")