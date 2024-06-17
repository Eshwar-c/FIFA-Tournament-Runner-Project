import random

teams=["South Korea",  "Japan" ,"Qatar" ,"Saudi", "Arabia ",  "South Africa" , "Morocco",  "Mexico", "United States" ,  "Canada" , "Uruguay"
       , "Brazil", "Chile" , "Argentina", "Brazil", "india" , "russia"]

knockout=[]

roundrobin=[]

semi=[]

finalWinner =""

def groupStage(teams):
   global knockout
   n=0
   while(n<8):
    t1= random.choice(teams)
    t2= random.choice(teams)
    if t1 not in knockout  and t2 not in knockout and t1!=t2:
        team1_value=random.randint(0,5)
        team2_value=random.randint(0,5)
        if team1_value > team2_value:
          knockout.append(t1)
          print("The winners of the 16 team group stage matches are "+ t1 +" : "+ str(team1_value)+ " vs "+ t2 +" : "+ str(team2_value))
        else:
          knockout.append(t2)
          print("The winners of the 16 team group stage matches are "+ t2 +" : "+ str(team2_value) +" vs "+ t1 +" : "+ str(team1_value))
        n=n+1 

def roundtwo(knockout):
   n=0
   while(n<4):
    t1= random.choice(knockout)
    t2= random.choice(knockout)
    if t1 not in roundrobin  and t2 not in roundrobin and t1!=t2:
        team1_value=random.randint(0,5)
        team2_value=random.randint(0,5)
        if team1_value > team2_value:
          roundrobin.append(t1)
          print("The winner of the round robin  stage match are "+ t1 +" : "+ str(team1_value)+ " vs "+ t2 +" : "+ str(team2_value))
        else:
          roundrobin.append(t2)
          print("The winners of the round robin stage matches are "+ t2 +" : "+ str(team2_value) +" vs "+ t1 +" : "+ str(team1_value))
        n=n+1

def semifinal(roundrobin):
  n=0
  while(n<2):
    t1= random.choice(roundrobin)
    t2= random.choice(roundrobin)
    if t1 not in semi  and t2 not in semi and t1!=t2:
        team1_value=random.randint(0,5)
        team2_value=random.randint(0,5)
        if team1_value > team2_value:
          semi.append(t1)
          print("The winner of the semi finals are  are "+ t1 +" : "+ str(team1_value)+ " vs "+ t2 +" : "+ str(team2_value))
        else:
          semi.append(t2)
          print("The winners of the semi finals are "+ t2 +" : "+ str(team2_value) +" vs "+ t1 +" : "+ str(team1_value))
        n=n+1

def final(semi):
      t1= random.choice(semi)
      t2= random.choice(semi)
      team1_value=random.randint(0,5)
      team2_value=random.randint(0,5)
      if team1_value > team2_value:
          print("The winner of FIFA world cup 2024 is "+t1+ " : " +str(team1_value) +" vs " +t2+ " : " +str(team2_value))
      else:
        print("The winner of FIFA world cup 2024 is "+t2+ " : " +str(team2_value) +" vs " +t1+ " : " +str(team1_value))



groupStage(teams)
print()
roundtwo(knockout)
print()
semifinal(roundrobin)
print()
final(semi)