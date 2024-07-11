# During the weekend, Ross Geller has decided to conduct some team games. He wants to split his friends into equal-sized teams. In some cases, some friends may be left out of the teams, and he wanted to use the left-out friends to assist him in conducting the team games. For instance, if there are 50 friends and they have to be divided into 7 equal-sized teams, then there will be 7 in each team and 1 friend will be left out. Ross asks for your help to automate this team-splitting task. Can you please help him out?

a=int(input())
b=int(input())
print("The number of friends in each team is",(a//b),"and left out is",a%b)