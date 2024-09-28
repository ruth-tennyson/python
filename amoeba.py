# The Research team led by Bernadette Wolowitz at Cal-tech University has discovered a new Amoeba that grows in the order of a Fibonacci series every month. They are exhibiting this amoeba at a national conference. They want to know the size of the amoeba at a particular time instant. If a particular month’s index is given, write a program to display the amoeba’s size.

# For Example, the size of the amoeba in months 1, 2, 3, 4, 5, 6,... will be 0, 1, 1, 2, 3, 5, 8.... respectively.

# Input Format

# The input is an integer that denotes the count of the month.

# Constraints

# NA

# Output Format

# The output is an integer denoting the amoeba size.

# Sample Input 0

# 13
# Sample Output 0

# 144
# Sample Input 1

# 9
# Sample Output 1

# 21
mon=int(input())
fib0=0
fib1=1
count=2
while count<mon:
  temp=fib0+fib1
  fib0=fib1
  fib1=temp
  count=count+1
print(fib1)