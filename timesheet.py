sun=int(input())
mon=int(input())
tue=int(input())
wed=int(input())
thu=int(input())
fri=int(input())
sat=int(input())
if mon>8:
  m=(mon*100)+((mon-8)*15)
else:
  m=mon*100
if tue>8:
  t=(tue*100)+((tue-8)*15)
else:
  t=tue*100
if wed>8:
  w=(wed*100)+((wed-8)*15)
else:
  w=wed*100
if thu>8:
  th=(thu*100)+((thu-8)*15)
else:
  th=thu*100
if fri>8:
  f=(fri*100)+((fri-8)*15)
else:
  f=fri*100
if sat>8:
  sa=(8*125)+((sat-8)*15)
else:
  sa=sat*125
if sun>8:
  su=(8*150)+((sun-8)*15)
else:
  su=sun*150
print(int(m+t+w+th+f+sa+su))