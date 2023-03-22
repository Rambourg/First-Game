print ("Welcome to my first game")
name = input("what is your name? ")
age = int(input("what is your age? "))

health = 10

if age >= 18:
    print("You are old enough to play")

weapon = input("Pick a weapon(sword/baton/):")
if weapon == "sword":
    print("Keep going baby")
else:
    print("choose again")

wants_to_play = input("Do you want to play? ").lower()
if wants_to_play == "yes":
     print("You are starting with 10 health" )
     print("Let's play.")

     left_or_right = input("First choice... Left or right? ")
     if left_or_right == "left":
        ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)?")

        if ans == "around":
           print("You went around and reached the other side of the lake")

        elif ans == "across":
             print("You managed to get across, but were bit by a fish and lost 5 health")
             health -= 5

        ans = input("You noticed a house and a river, wich do you go to (river/house)? ")
        if ans == "house":
           print("You go to the house and are greeted by the owner and he does not like you and you lose 5 health")
           health -=5

           if health <= 0:
            print("You have 0 health and you lost the game baby...")
  
           else:
            print("You survived, well done you won the game")
            
        else:
            print("you fell down and lost")
  
else:
      print("You are not old enough to  play")
  
