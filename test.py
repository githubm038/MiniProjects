while True :
    p1=input("palyer 1 enter rock paper or sissor:")
    p2=input("player 2 enter rock paper or sissor:")
    if p1==p2:
        print("tie")
    elif p1=='rock':
        if p2=='sissor':
            print("rock won")
        else:
            print("paper won")
    elif p1=='sissor':
        if p2=='paper':
            print("sissor  won ")
        else:
            print("rock won")
    elif p1=='paper':
        if p2=='rock' :
            print("paper  won")
        else:
            print("sissor won")
    else:
        print("invalid")