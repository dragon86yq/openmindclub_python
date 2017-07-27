print ("You enter a dark room with two doors. Do you go throug door #1 or door #2 or door #3?")

door = input(">")

if door == "1" :
    print( "There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print ("2. Scream at the bear.")	
    bear = input(">")	
    if bear == "1" :
        print("The bear eats your face off. Good job!")
    elif bear == "2" :
        print("The bear eats your leg off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away."%bear)	
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Buleberries.")
    print("2. Yellow jacket clothspins.")
    print("3. Understand revolvers yelling meldies.")
    insanity = input(">")
    if insanity == "1" or insanity == "2":
    	print("Your body survives powered by a mind of jello. Good job!")
    else:
    	print("The insanity rots your eyes into a pool of muck.")
elif door == "3":
    print("There is a surprise")
    finite = input("You enter finite cycle:")
    finite = int(finite)
    for i in range(1,finite):
        print(i)
else:
    print("You stumble around and fall on a knife and die. Good job.")