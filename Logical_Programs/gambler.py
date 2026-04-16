import random 

stake=int(input("Enter name of the stake holder(in $) : "))
goals=int(input("Enter your goals(in $) : "))
trials=int(input("Enter number of trials : "))
win=0
total_bets=0
for i in range(trials):
    amount=stake
    bets=0
    while amount>0 and amount<goals:
        bets+=1
        if random.random()<0.5:
            amount+=1
        else:
            amount-=1
    total_bets+=bets
    if amount==goals:
        win+=1
print(f"How much time Win {win}")
print(f"The percentage of win {win/trials*100}")
print(f"The percentage of loss {(trials-win)/trials*100}")
        
    
                 
                