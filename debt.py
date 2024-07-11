# Leena wanted to start a business and she was looking for a venture capitalist. Through her friend, she met a construction company owner Meena, who was interested in investing in an emerging business. Looking at the business proposal, the owner was very much impressed with Leena's work. So she decided to invest in Leena's business and hence gave a green signal to go ahead with the project. Leena got a loan of Rs. X for a period of Y years from the owner at R% interest per annum. Find the rate of interest and the total amount to be returned by Leena to the owner. The owner was impressed by the proper repayment of the financed amount and decides to give a special offer of a 2% discount on the total interest at the end of the settlement. Find the discount amount and also find the total amount given back by Leena.

X=float(input())
Y=float(input())
R=float(input())
SI=float(X*Y*R)/100
a=float(SI+X)
d=float((SI*2)/100)
r=float(a-d)
print("%.2f"%SI)
print("%.2f"%a)
print("%.2f"%d)
print("%.2f"%r)