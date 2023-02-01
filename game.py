from art import logo,vs
from game_data  import data
import random
from os import system,name

def clear():
    if name=='nt':
        _=system('cls')
    else:
        _=system('clear')

def max_fun(a,b):
    if(a>b):
        return 'A'
    else:
        return 'B'

def check(a,b,d):
    while a==b:
        b=random.randint(0,d-1)

d=len(data)


a=random.randint(0,d-1)


again=True

score=0

while(again):
    print(logo)
    print(f"your current score is : {score}")
    print("compare A : "+data[a]['name']+", a "+data[a]['description']+", from "+data[a]['country'])
    b=random.randint(0,d-1)
    if(a==b):
        check(a,b,d)
    print(vs)
    print("Against B : "+data[b]['name']+", a "+data[b]['description']+", from "+data[b]['country'])
    ans=max_fun(data[a]['follower_count'],data[b]['follower_count'])
    guess=input("who has more follower ? type 'A' , 'B' : ")
    if(guess==ans):
        again=True
        score += 1
        a=b
        clear()
    else:
        again=False
        clear()
        print(logo)
        print(f"you are wrong, your final score is {score} ")



