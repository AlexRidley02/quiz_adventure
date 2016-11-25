# An adventure game
from time import time

name = ""

def namescreen():
    global name

    name = input("Enter your name: ")
    room1()


def room1():
    
    print("You find the dungeon enterance. Do you")
    print("A. Go through the door")
    print("B. Find another entrance")
    print("C. Go home")
    answer = input("What will you do: ")

    if answer.upper() == "A":
        room2()

    elif answer.upper() == "B":
        print("""You go round the side of the dungeon hoping to find another entrance.
    You carry on runnuing past only to bumb into a strong monster you have never seen before.
    It swings its sword hitting you and destroying you. You are dead.""")
        room1()

    elif answer.upper() == "C":
              print("""You go home. You regret this decision because you wanted an adventure but you just left because you were scared.
                    You return to the dungeon to try again""")
              room1()

def room2():
    global hp

    print("""you go through the door to see a long corridor. The sound of the door creaking echos through out it.
    There are two doors, one to the left and one at the end of the corridor.Do you""")
    print("A. Leave the dungeon")
    print("B. Go to the door on the left")
    print("C. Go to the end of the corridor")
    answer = input("What will you do: ")

    if answer.upper() == "A":
        print("""You leave the dungeon and go home. You regret this decision because you wanted an adventure.
    You return to the dungeon to try and best it again""")
        room1()
              
    elif answer.upper() == "B":
        print("""You aproach the door to the left. You open it and walk in.
    Its dark and you can't see anything. You can hear a noice.It sounds like laughing.
    Suddenly you are attacked by a group of skeletons. The Group were to strong and you couldn't defend your self. You die""")
        room1()      
              
    else:
         print("""You walk to the end of the corridor.The armour intimidates you.
    You pick up the pace and get to the end of the corridor in no time.
    As you aproach the door you become aware that the door has a face.""")
         doorconversation()

def doorconversation():
   global hp

   print("""You say hello to the door. It replies with a riddle of sorts.
            To all thoes who seek to pass tell me what is the sword for.
            Which of these is your reply""")         
   print("A. The sword is used to intimidate and show you power over others.")
   print("B. The sword is used an extention of the arm. It is your battle partner and should only be used when needed.")
   print("C. useless. there is no need for such a tool.")
   answer = input("What will you do: ")

   if answer.upper() == "B":
       print("The correct choice young worrior. You may proceed")
       room3()
    
   elif answer.upper() == "C":
       print("The door tells you that the ruins are no place for a pacifist and that you shoud go home")
       home()

   else:
       room1()
    
def home():

    print("""You go home happy to be safe and not in the ruins anymore.
          You no longer feel guilty because you sort of went on an adventure.
          You stay in your village forevermore and get married.
          You'r forever happy""")

def room3():
    global name

    print("""You walk through the door. Words flash before your eyes.
           You struggle to see it but your read out "This has all been a trial".
           This is the last. My final battle you could call it.
           Nobody has made it this far. you are the first.
           You will be my sucessor. Get ready, """, name, "." ".")

    print("A. Go back to the armour in the corridor and take it to use.")
    print("B. Go back to the door to ask for help.")
    print("C. Proceed forward to find the mysterios thing that is calling out to you.")
    answer = input("How will you react: ")

    if answer.upper() == "A":
        print("""You go back to the armour and try and take it but it turns out it there was a monster hiding behind it.
                 It attaks you and you flee.You feel like this may affect you later on but you still go back.
                 whilst going back you realise the door has closed and you cant go back through.
                 the door calles you a coward and tells you you dont have what it takes to take 'it' on after all.""")
        roomx()

    elif answer.upper() == "B":
        print("You ask the door for help but it refuses.It tells you that you have to do this on your own")

        room3()

    elif answer.upper == "C":
        print("""You proceed through the room and you start to notice strange words on the walls.
                 they do not look at all famuiliar to you. You leave them alone. You see a door at the end of the corridor and rush to it""")

        room4()
                 
           
def roomx():
    global name
    print("""You walk through the door. Words flash before your eyes.
           You struggle to see it but your read out "This has all been a trial".
           This is the last. My final battle you could call it.
           Nobody has made it this far. You are the first.
           You will be my sucessor. Get ready, """, name, ".")
  
    print("A. Go back to the door to ask for help.")
    print("B. Proceed forward to find the mysterios thing that is calling out to you.")
    answer = input("How will you react: ")

    if answer.upper() == "A":
        print("You ask the door for help but it refuses.It tells you that you have to do this on your own")

        roomx()

    elif answer.upper == "B":
        print("""You proceed through the room and you start to notice strange words on the walls.
                 they do not look at all famuiliar to you. You leave them alone. You see a door at the end of the corridor and rush to it""")

        roomZ()
                 
def room4():
    global name

    print("""You enter the room to find a skeleton holding a long sword looking the other way.
          You see a wall you could hide behind and sneak over to it. Looking from the wall you can see a book rested on a pedestal.
          you recognise it and you now know it is a spell tome.
          you could go and get it but it may be hard.""")
          
    print("A.Try and sneak to the pedestal and get the spell")
    print("B.Retreat for now until you have a plan")
    print("C.Try and attack the skeleton with your fists")
    answer = input("What will you do: ")

    if answer.upper() == "A":
        print("""You sneak over to the pedestal and get the spell. You had found the invisibility tome. You used the spell and get back to the wall.
              You wait for a while until you can use the spell again and think of a plan""")

        finalstage()

    elif answer.upper() == "B":
        print("""You retreat back to the room with the strange words. You acidentaly step on something you didnt before and the floor opens up.
              you fall to your death. You are dead""")

        room4()

    elif answer.upper() == "C":
        print("""You run at the skeleton and punch it in the skull.It yelps but then turns around and slices you with its balde.
              You are injured but you can still go on. You run back to the room withe strange words but it follows you.
              It raises its sword and throws it at you. It hits you right in the back and you lose the last of your energy.
              You cannot go on.""")

        room4()              

def roomz():

    print("""You enter the room to find a skeleton holding a long sword looking the other way.
          You see a wall you could hide behind and sneak over to it. Looking from the wall you can see a book rested on a pedestal.
          you recognise it and you now know it is a spell tome.
          you could go and get it but it may be hard.""")

    print("A.Try and sneak to the pedestal and get the spell")
    print("B.Retreat for now until you have a plan")
    print("C.Try and attack the skeleton with your fists")
    answer = input("What will you do: ")

    if answer.upper() == "A":
        print("""You sneak over to the pedestal and get the spell. You had found the invisibility tome. You used the spell and get back to the wall.
              You wait for a while until you can use the spell again and think of a plan.
              Picking up the book seams to fill you with health again. You are fully healed.""")

        finalstage()

    elif answer.upper() == "B":
        print("""You retreat back to the room with the strange words. You acidentaly step on something you didnt before and the floor opens up.
              you fall to your death. You are dead""")

        room4()

    elif answer.upper() == "C":
        print("""You run at the skeleton and punch it in the skull.It yelps but then turns around and swings at you you with its balde.
              You remember that the monster armour had hurt you previoucly and that you were still weak.
              The sword slices you and you lose the resdt oy your energy. As you fade the monster tells you that he is the boss of the ruins>
              He tells you that you cant just go back this time and that you will have to start again.""")

        namescreen()
          
            
def finalstage():
    global name
    

    print("""You can now use the spell again and you have 3 plans that might work. You think about it over and over. It seams like forrever since you got back to the wall.
          you hear a noice all of a sudden and you look iover the wall to see that the skeleton is coming you way. You need to do something and fast""")
    start_time = time()

    print("A. Go invisible and dteal the sword from the skeleton")
    print("B. Go to the skeleton and barguin.The sword for the sword")
    print("C. Look around the room first in search for something that may help")
    answer = input("What will you do: ")
    time_taken = time() - start_time
    
    if time_taken > 10:
        print("""you took to long and the skeleton found you.It swang out you with its sword like never before and managed to take out all your energy.
              you die. The skelton calls out to as you die.There is no easy way to get back to me.Start again it said in your final moment""")
        


    elif answer.upper == "A" and time_taken <= 10:
        print("""you use the invisibility spell to sneak up to the skeleton.You steal its sword right from its hands and it to turns invisible
          you retreat back to the wall and brace your self for the skeletons arival.The skeleton is coming your way.
          it anticipated your swing of the sword and jumps on it disarming you.It strangels you to death.You are dead.
          as you lose your last bit of health it says to you.There is no easy way to get back to me.Start again.""")

    elif answer.upper == "B" and time_taken <= 10:
        print("""You aproach the skeleton and it notices you. It turns around and strikes you with is sword.You are dead.In your final moments it said to you.
              There is no easy way to get back to me.Start again.""") 


    elif answer.upper == "C" and time_taken <= 10:
        print("""You use the spell and go looking for something that may help you.Luckely and to your suprise you found a bow and a quiver with a few arrows left.
              You return to the wall with your new found weapon and prepare for the battle""")

        TheEnd()   

def TheEnd():
    global name

    print("""You aim your bow at the skelton and your ready to shoot but you also knoice a fire lamp hanging form the ceiling and the gasoline on the ground.
          You have two options.""")

    print("A.Shoot down the lantern")
    print("B.Shoot the skeleton")
    answer = input("What do you do: ")

    if answer.upper() == "A":
        print("""You shoot down the lanturn and the whole floor goes alight.The skeleton resists the flames but you do not. You did from the flames.
              The words from the other room glow and the glow flows to you.You have the feeling that non of that was worth it""")
        namescreen()
        
    else:
        print("""You shoot the skeleton and it falls to the ground.It looks at you and says.I am the skeleton lord.None have been able to beat me but you have succeded>
              congratulations you have become the draugr(Skeleton lord).You will rule this dungeon forever""")
    
        creditscene()

def creditscene():
    global name

    print("Congrats you have beat the game.")
    print("         Credits                ")
    print("""Created by Alex Ridley  Designed by Alex Ridley
             Story by Alex Ridley  Coded by Alex Ridley
             Special thanks to:
                              Mr Charlton - Helped me write the code
                              Rebekah Mullen - Helped with my spelling
                              Python - The program I used
             Game made with 'Python'                

                               Thank you""")
        



# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    namescreen()
