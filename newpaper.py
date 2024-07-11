# Each Saturday, The Herald sells 'a' copies of a special edition newspaper for Rs. b per copy. The cost to him for printing each newspaper is Rs. c. He pays a fixed cost of Rs.100 per Saturday for storage, delivery, and so on. He wants to calculate the profit which it obtains only on Saturdays. Can you please help him out by writing a program to compute the profit if a, b, and c are given?

# Input Format

# Input consists of 3 integers: a, b, and c. a is the number of copies sold, b is the cost per copy and c is the cost The Herald spends per copy.

a=int(input())
b=int(input())
c=int(input())
profit=(a*b)-(a*c)-100
print(profit)
      
