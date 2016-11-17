# An adventure game

hp = 10
def room1():
    global hp

    print("You find the dungeon enterance. Do you")
    print("A. Go throughthe door")
    print("B. Find another enterance")
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

   print("You say hello to the door. It replies with a riddle of sorts.To all thoes who seek to pass tell me what the sword if for. Which of these is your reply")         
   print("A. The sword is used to intimidat and show you power over others")
   print("B. The sword is used an extention of the arm. It is your battle partner and should only be used when needed")
   print            
    
    

    








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()
