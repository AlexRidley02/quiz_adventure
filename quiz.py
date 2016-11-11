# Our quiz!

score = 0

def quiz():
    global score

    question1()
    question2()
    question3()
    question4()

def question1():
    global score

    print("Who is the strongest")
    print("A. bulbasour")
    print("B. charmander")
    print("C. squirtle")
    print("D. pidgey")
    answer = input("Select an option: ")

    if answer.upper() == "A":
        score = score + 50
    elif answer.upper() == "B":
        score = score + 100
    elif answer.upper() == "C":
        score = score + 75
    elif answer.upper() == "D":
        score = score + 25

    print(score)

def question2():
    global score

    print("which pokemon did ash get at the start of his journey")
    print("A. squirtle")
    print("B. pikachu")
    print("C. metapod")
    answer = input("Select an option: ")

    if answer.upper() == "A":
        score = score + 0
    elif answer.upper() =="B":
        score = score + 100
    elif answer.upper() == "C":
        score = score + a
        15

    print(score)

def question3():
    global score

    print("Whick pokemon created the universe")
    print("A. arceus")
    print("B. mew")
    print("C. pikachu")
    answer = input("Select an option: ")
    
    if answer.upper() == "A":
       score = score + 100

    elif answer.upper() == "B":
         score == score + 0

    elif answer.upper() == "C":
         score == score + 0

         
    print(score)

def question4():
    global score

    print("what were the 3 pokemon X and Y started pokemon")
    print("A. Froakie, Chespin and Fennekin")
    print("B. Charmander, Bulbasour and Squirtle")
    print("C. Piplup, Turtwig, and Chimchar")
    print("D. Totodile, Cyndaquil and Chikorita")
    answer = input("Select an option: ")

    if answer.upper() == "A":
      score = score + 150

    else:
        score = score + 0
        
    print(score)
       

         
        





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
