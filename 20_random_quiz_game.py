print("Welcome to the 20 RANDOM QUIZ GAME!")

playing = input("Do you really want to play? ")

if playing.lower() != "yes":
    quit()

print("OKAY! Let's play the 20 RANDOM QUIZ GAME! :) ")
score = 0

answer = input("1. Who wrote Romeo and Juliet? ")
if answer.lower() == "William Shakespeare":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("2. What is the largest planet in our solar system? ")
if answer.lower() == "Jupiter":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("3. Which famous scientist developed the theory of general relativity? ")
if answer.lower() == "Albert Einstein":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("4. What is the chemical symbol for gold? ")
if answer.lower() == "Au":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("5. In what year did the Titanic sink? ")
if answer.lower() == "1912":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("6. Who painted the Mona Lisa? ")
if answer.lower() == "Leonardo da Vinci":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("7. What is the largest ocean on Earth? ")
if answer.lower() == "Pacific Ocean":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("8. Who is known as the Father of Computer Science? ")
if answer.lower() == "Alan Turing":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("9. What is the currency of Japan? ")
if answer.lower() == "Japanese Yen":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("10. Which planet is known as the Red Planet? ")
if answer.lower() == "Mars":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("11. What is the capital city of Australia? ")
if answer.lower() == "Canberra":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("12. Who wrote To Kill a Mockingbird? ")
if answer.lower() == "Harper Lee":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("13. What is the main ingredient in guacamole? ")
if answer.lower() == "Avocado":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("14. In which year did the first manned moon landing occur? ")
if answer.lower() == "1969":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("15. What is the longest river in the world? ")
if answer.lower() == "Nile River":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("16. Who discovered penicillin? ")
if answer.lower() == "Alexander Fleming":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("17. Which planet is known as the Blue Planet? ")
if answer.lower() == "Earth":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("18. What is the speed of light in a vacuum? ")
if answer.lower() == "Approximately 299,792 kilometers per second":
    print('Correct!')
    score += 1
else:
     print("Incorrect!")

answer = input("19. What is the capital city of France? ")
if answer.lower() == "Paris":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("20. In which year did World War II end? ")
if answer.lower() == "1945":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("Alright! You answered " + str(score) + " questions correct!")
print("That means, you got " + str((score/4)*100) + "%.")