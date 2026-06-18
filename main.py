#i=1
#while i<5:
  #print("i is : {}".format(i))
  #i=i+1

#print(list(range(1,10)))

#x=[1,2,3,4,5,6,7,8,9,10]
#out=[]
#for num in x:
  #out.append(num**2)
#print(out)

  
#print([num**2 for num in x]  )


#def my_func(prame1):
  #print(prame1)



#my_func("Ahmed")



#def my_func2(name="AG"):
  #print("Hello {}".format(name))


#my_func2("Ahmed")



#def my_func2(name="AG"):
  #print("Hello {}".format(name))


#my_func2()
#print(my_func2)



#def seq(num):
  #"""
  #This function takes a number and returns the square of the number
  #num: int
  #return: int
  
  
  #"""
  #return num**2
#output=seq(2)
#print(output)
#help(seq)


# myarea=input("Choose your area (ABC),(DE),(FG)\n")
# if myarea.upper()=="ABC" or myarea.upper()=="DE" or myarea.upper()=="FG":
#   print(f"Your area {myarea} is on the list")
# else:
#   print(f"Your area{myarea} is not on the list")
  

# name=input("Enter your name\n")
# password=input("Enter your password\n")
# if name.lower()=="ag" and password=="hiThere":
#   print("Welcome back")
# else:
#   print("Sorry, wrong name or password")




# age=int(input( "Enter your age\n"))
# license=input("Do you have a license? (yes) or (no)\n")
# if license.lower()=="yes" and age>=18:
#   print("You can drive")
# elif license.lower()=="no" or age<18:
#   print("You can't drive")
# else:
#   print(f"Sorry, your entery of {license} is not understood")









# is_AMERICAN=input("Are you an American? (yes) or (no)").lower()
# if is_AMERICAN=="yes":
#   print("Good. That is the first step")
#   is_21=input("Are you above 21? (yes) or (no)").lower()
#   if is_21=="yes":
#     print("You can have a license")
#   else:
#     print("Sorry, you have to be 21 or older")
#     print("Please try again when you are 21")

# else:
#     print("Sorry, an American license is give only to Americans")










# print("""







# """)








# input(""" """)




# colors=input("""
# Welcome to my island!
# There are two doors in front of you. 🚪 a red door and � 🚪 a blue door
# Which door do you want to open? 
# """).lower()
      
      
# if colors=="blue":
#  print(""" oops! You chose the crocodile door.Game over! 🐊🐊🐊 """)
# elif colors=="red":
#  print("Great! now you entered a room.You found three boxes:🎁white, 🎁 black, 🎁 green")
#  is_color=input("Which box do you open?").lower()
#  if is_color=="white":
#       print("Oops! You opened a box filled with snakes 🐍🐍")
#  elif is_color=="black":
#       print("Oops! You opened a box filled with spiders 🕷️🕷️🕷️") 
#  elif is_color=="green":
#       print("Congratulations! You found the treasure! 💰💰💰") 
#  else:
#       print("Invalid choice! 🤷‍♂️🤷‍♂️🤷�")   
# else:
#            print("Invalid choice! 🤷‍♂️🤷‍♂️🤷�")
      
# i still have a test to do




# is_American=input("Welcome to Test Americans.You are at the train station. Do you want to take an Uber, a taxi or a car?").lower()


# if is_American=="uber":
#   print("Sorry, Uber is not available in your area")
# elif is_American=="car":
#   print("Sorry, you don't have enough money")
# elif is_American=="taxi":
#   taxicolors=input("Great, you are in front of three taxis: a red taxi, a white taxi and a black taxi").lower()
#   if taxicolors=="red":
#     print("Sorry, this color is not available")
#   elif taxicolors=="white":
#     print("Not a chance")  
#   elif taxicolors=="black":
#     payment=input("Great, you wanna pay cash or visa?").lower()
#     if payment=="cash":
#       print("This method is not available")
#     elif payment=="visa":
#       print("Great,Now we are talking")
#     else:
#       print("Invalid choice")
#   else:
#     print("Invalid choice")

# else:
#   print("Invalid choice")
















# import octucode
# import random
# my_random=random.randint(-5,5)
# print(my_random)
# print(octucode.course)
# print(octucode.level)
# print(octucode.teacher)














































# if colors=="red":
#   is_Color= input(""" Great now you entered a room.
#   you found three boxes: 🎁 white, 🎁 black, 🎁 green
#   Which box do you open?
#   """).lower()
  
#   if is_Color=="white":
#         print("Oops! You opened a box filled with snakes 🐍🐍🐍")
        
#   if is_color="black":
#         print("Oops! You opened a box filled with spiders 🕷️🕷️🕷️"")
              
#   if is_Color=="green":
#         print("Congratulations! You found the treasure! 💰💰💰")      

#               else:
#                 print("Invalid choice! 🤷‍♂️🤷‍♂️🤷‍♂️")











   

  










# import random
# comprandomnumbers=random.randint(1000,9999)

# my4randomnumbers=int(input("Enter a 4-digit PIN code:")) 
# if my4randomnumbers<=9999 and my4randomnumbers>=1000:
#   print(my4randomnumbers)

#   if my4randomnumbers==comprandomnumbers:
#       print("Congratulations! You win")
  
#   else:
#      print("Failure! PIN code did not match")
#      print(f"The computer generated this PIN:{comprandomnumbers}")
    
  
# else:
#    print(f"Please enter 4 digits This is not {my4randomnumbers}")




# import random
# pin_code=random.randint(1000,9999)
# user_input=int(input("Enter a 4-digit PIN code:")
# if len(str(user_input))>4 or len(str(user_input))<4:
#     print("Please enter 4 digits")
# elif user_input==pin_code: 
#     print("Success! PIN code matched")  
               
# else:
#     print("Failure! PIN code did not match")
#     print(f"The computer generated this PIN:{pin_code}")














































# import random
# print(random.random()) # does not have input
# print(random.uniform(0,5))
# print(random.random() *5)


# import random
# print("Welcome to the virtual coin toss game")
# input("Press Enter to start ....")
# random_number=random.randint(0,1)
# if random_number==0:
#   print("Heads")
# else:
#   print("Tails")














# import random
# print("Welcome to the virtual coin toss game")
# input("Press Enter to start ....")
# random_number=random.randint(0,1)
# if random_number>=0.5:
#   print("Heads")
# else:
#   print("Tails")










# import random
# comprandint=random.randint(0,1)
# comprandom=random.random()
# guessinggame=input("""Welcome to the coin Guessing Game!
# Choose a method to toss the coin:
# 1. Using random.random()
# 2. Using random.randint()
# Enter your choice (1 or 2):""")

# if guessinggame=="2":
#   coinguessing=input("Enter your Guess (Heads or Tails):").lower()
#   if   coinguessing=="heads" and comprandint==0:
#     print("Cogratulations! You won!")
#   elif coinguessing=="tails" and comprandint==1:
#     print("Cogratulations! You won!")
#   elif coinguessing !="heads" and coinguessing !="tails":
#     print("Invalid choice. Please select either Heads or Tails")
#   else:
#     print("Sorry, you lost!")
    
# elif guessinggame=="1":
#   coinguessing2=input("Enter your Guess (Heads or Tails):").lower()
#   if coinguessing2=="heads" and comprandom>=0.5:
#     print("Cogratulations! You won!")
#   elif coinguessing2=="tails" and comprandom<0.5:
#     print("Cogratulations! You won!")  
#   elif coinguessing2 !="heads" and coinguessing2 !="tails":
#     print("Invalid choice. Please select either Heads or Tails")
#   else:
#     print("Sorry, you lost!")  
    
# else:
#   print("Pleas enter 1 or 2")





# print(f"The computer's coin toss result was:{comprandint}")
# print(f"The computer's coin toss result was:{comprandom}")



# #list
# favouriteletters=['A',"B","C","D","E","F","G","H","I","J","K","L","M","N","O",]
# print(favouriteletters[3])
# print(favouriteletters[-1])
# print(favouriteletters[-4])

# print(f"The first letter on our list is {favouriteletters[0]} and the last letter on our list is {favouriteletters[-1]}")

# favouriteletters[-7]="i"
# print(favouriteletters)









# colors=[]
# addcolor=input("Add the first color you like:")
# colors.append(addcolor)
# anothercolor=input("Do you want to add more colors? Yes, or No?").lower()
# if anothercolor=="yes":
#   addcolor2=input("Add another color to the list:")
#   colors.append(addcolor2)
#   print(colors)
# elif anothercolor=="no":
#   print("The color you like are:")
#   print(colors)

# else:
#   print("Invalid choice. Please select either Yes or No")

# # colors.append("RED")
# # colors.append("BLUE")
# # print(colors)


# class_a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# class_b=[21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
# # class_a.extend(class_b)
# # print(class_a)
# class_b.remove(40)
# print(class_a+class_b)

# print(type(class_a))

# name=input("What is your name?")
# if name:
#   print(f"Hello,{name}")

# else:
#   print("You forgot to enter your name")




# fruit_basket=["Apples","Oranges","Bananas"]
# guess=input("Guess the name of the fruits in the basket:")
# if guess in fruit_basket:
#   print("Good guess")

# else:
#   print("Sorry, better luck next time")



# class_cd=[677,645477,6745457,67455447,45454,6454577,67667,69977,677,68877,677787,67337,67117,86798498]
# class_cd.remove(645477)
# print(class_cd)













































































# booklist=[]
# books=input("Enter the name of a book you own:").lower()
# if books:
#   booklist.append(books)
#   books2=input("Enter the name of another book you own (or press 'Enter' to skip):").lower()

#   if books2:
#      booklist.append(books2)
#      print(f"Your library:{booklist}")
    
#   else:
#      print(f"Your library:{booklist}")


# else:
#   print("Please enter the name of a book")



# booklist2=[]
# books3=input("Enter the name of a book you wish to have in the future:").lower()
# if books3:
#    booklist2.append(books3)
#    books4=input("Enter the name of another book you wish to have (or press 'Enter' to skip):").lower()

#    if books4:
#       booklist2.append(books4)
#       print(f"Your wish list:{booklist2}")
    
#    else:
#       print(f"Your wish list:{booklist2}")


# else:
#    print("Please enter the name of a book")







# booklist3=[]
# books5=input("Enter the name of a book from your wishlist that you have acquried or press enter to skip:").lower()
# if books5:
#    booklist3.append(books5)
#    print(f"Updated library:{booklist+booklist3}")
   
#    if books5 in booklist2:
#     booklist2.remove(books5)
#     print(f"Updated wishlist:{booklist2}")
#     #donation=input("Enter the name of a book from your library you wish to donate or press 'Enter' to skip:")  
#    else:
#       print(f"Your wishlist:{booklist2}")
  

# else:
#    print(f'Updated library:{booklist}')
#    print(f"Updated wishlist:{booklist2}")


# ##################
# biglist=booklist+booklist3
# books6=input("Enter the name of a book from your library you wish to donate or press enter to skip").lower()
# if books6 in biglist:
#    biglist.remove(books6)
#    print(f"Final library after donations:{biglist}")

# else:
#    print(f"Final library after donations:{biglist}")
#    print(f"Sorry, this book,{books6} is not in your library")




























#






































# library=[]
# wishlist=[]
# book_name=input("Enter the name of a book you own:")
# library.append(book_name)
# book_name=input("Enter the name of another book you own (or press 'Enter' to skip):")
# if book_name:
#   library.append(book_name)

# print("\nYour library:",library)

# book_name=input("\nEnter the name of a book you wish to have in the future:")
# wishlist.append(book_name)
# book_name=input("Enter the name of another book you wish to have in the future (or press 'Enter' to skip:")
# if book_name:
#   wishlist.append(book_name)

# print("\nYour wishlist:",wishlist)

# acquired_book=input("\nEnter the name of a book from your wishlist that you have acquired(or press 'Enter' to skip):")
# if acquired_book in wishlist:
#    library.append(acquired_book)
#    wishlist.remove(acquired_book)

# print("\nUpdated library:",library)
# print("\nUpdated wishlist:",wishlist)
# donated_book=input("\nEnter the name of a book from your library you wish to donate (or press 'Enter' to skip):")
# if donated_book in library:
#    library.remove(donated_book)

# print("\nFinal library after donations:",library)
















































# names_string=input("Enter names separated by a comma...")
# names=names_string.split(", ")
# print(type(names))
# print(names)
# print(len(names))





# print('Welcome to "Whose wallet?"')
# names=input("You will give me a list of names, and I will pick a person to pay if you're ready, enter the names seperated by a comma:")
# import random
# mynames=names.split(", ")
# myrandomname=random.randint(0,len(mynames)-1)
# print(f"Please ask {mynames[myrandomname]} to take his wallet out. Dinner is on him")






# import random
# print("Welcome to 'Whose wallet?'")
# print("You will give me a list of names, and I will pick a person to pay")
# names=input("If you're ready, enter the names separated by a comma:").split(",")
# print(f"Please ask {random.choice(names)} to take his wallet out. Dinner is on him")





































# basket= [["Apples","Bananas"],["Milk","Water"]]
# print(basket[0][0],basket[1][0])
# basket2=["cake","candy"]
# basket.append(basket2)
# basket.append(["cucumber","tomato"])
# print(basket)













# books=["book2","book3","book5"]
# books.insert(0,"book1")
# books.insert(3,"book4")
# books.insert(5,"book6")
# print(books)


# basket=[["Apples","Bananas"],["Milk","Water"]]
# print(basket)
# input("Press enter to change the content...")
# print("Here is the updated basket")
# basket[0].insert(0,"Oranges")
# basket[0].insert(3,"Kiwis")
# basket[1].insert(0,"Coffee")
# basket[1].remove('Water')
# basket[1].insert(2,'Tea')
# numbers=[1,2,3]
# basket.append(numbers)
# print(basket)

























# print("Welcome to place the rabbit")


# list1=["Grass1","Grass2","Grass3"]
# list2=["Grass4","Grass5","Grass6"]
# list3=["Grass7","Grass8","Grass9"]

# print(list1)
# print(list2)
# print(list3)
# print("Where should the rabbit go?🐇")
# myrabbit=input("Please choose a row and a column:")

# if myrabbit=="11":
#   list1=["🐇","Grass2","Grass3"]
#   print(list1)
#   print(list2)
#   print(list3)

# elif myrabbit=="12":
#    list1=["Grass1","🐇","Grass3"]
#    print(list1)
#    print(list2)
#    print(list3)

# elif myrabbit=="13":
#    list1=["Grass1","Grass2","🐇"]
#    print(list1)
#    print(list2)
#    print(list3)

# elif myrabbit=="21":
#     list2=[ "🐇","Grass5","Grass6"]
#     print(list1)
#     print(list2)
#     print(list3)

# elif myrabbit=="22":
#      list2=["Grass4","🐇","Grass6"]
#      print(list1)
#      print(list2)
#      print(list3)

# elif myrabbit=="23":
#      list2=["Grass4","Grass5","🐇"]
#      print(list1)
#      print(list2)
#      print(list3)

# elif myrabbit=="31":
#      list3=["🐇","Grass8","Grass9"]
#      print(list1)
#      print(list2)
#      print(list3)

# elif myrabbit=="32":
#      list3=["Grass7","🐇","Grass9"]
#      print(list1)
#      print(list2)
#      print(list3)

# elif myrabbit=="33":
#      list3=["Grass7","Grass8","🐇"]
#      print(list1)
#      print(list2)
#      print(list3)

# else:
#      print("Invalid choice,Please enter the row and the column again")





# print("Welcome to place the rabbit")
# field=[["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]
# print(f"{field[0]}\n{field[1]}\n{field[2]}")
# print("Where should the rabbit go?🐇")
# position=input("Please choose a row and a column:")
# row=int(position[0])
# column=int(position[1])
# field[row-1][column-1]="🐇"
# print("\nSuccess....\n")
# print(f"{field[0]}\n{field[1]}\n{field[2]}")








# print("Welcome to place the rabbit")
# field=[["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]
# print(f"{field[0]}\n{field[1]}\n{field[2]}\n")
# position=input('Where should the rabbit go? 🐇')
# row=int(position[0])
# column=int(position[1])
# field[row-1][column-1]="🐇"
# print("\nSuccess....\n")
# print(f"{field[0]}\n{field[1]}\n{field[2]}")









# print("Welcome to place the rabbit")
# field=[["🌿","🌿","🌿✋"],["🌿","🌿","🌿👊"],["🌿","🌿✌","🌿"]]
# print(f"{field[0]}\n{field[1]}\n{field[2]}\n")
# print("Please choose a row and a column\n")
# position=input("Where should the rabbit go? 🐇")
# row=int(position[0])
# column=int(position[1])
# field[row-1][column-1]="🐇"
# print("\nSuccess....\n")
# print(f"{field[0]}\n{field[1]}\n{field[2]}")








# import random
# mylist=["Rock","Paper","Scissors"]
# myrandomlist=random.randint(0,2)
# computer_choice=mylist[myrandomlist]


# print("Waiting for user input...")
# game=input("Welcom to the rock, paper, scissors game.\nPress Enter to continue or type (Help) for the rules").lower()
# print("User input received.")
# if game=="help":
#    print("*********Rules*********\n1) You choose and the computer chooses\n2) Rock smashes  scissors -> Rock wins\n3) Scissors cut paper\n4) Paper covers rock -> Paper wins")
   
  
#  ###  
# mygame=input("Please enter your choice (rock, paper, scissors):").lower()
# if mygame == "rock" and computer_choice == "Paper":
#         print("👊\n✋\nSorry, you lost")
# elif mygame == "paper" and computer_choice == "Scissors":
#         print("✋\n✌\nSorry, you lost")
# elif mygame == "scissors" and computer_choice == "Rock":
#         print("✌\n👊\nSorry, you lost")
# elif mygame == "rock" and computer_choice == "Scissors":
#         print("👊\n✌\nYou win!")
# elif mygame == "scissors" and computer_choice == "Paper":
#         print("✌\n✋\nYou win!")
# elif mygame == "paper" and computer_choice == "Rock":
#         print("✋\n👊\nYou win!")

# elif mygame not in ["rock","paper","scissors"]:
#         print("Invalid choice. Please run the program again and choose rock, paper, or scissors.")
# else:
#         print(f"{mygame} vs {computer_choice}. It is a draw!")




#





### Asci print("""
# ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████�""")

# import random
# myrock="👊"
# mypaper="✋"
# myscissors="✌"

# print("\nWelcome to the Rock, Paper, Scissors game:")
# confirm=input("Press Enter to continue or type (Help) for the rules:").lower()
# if confirm=="help":
#    print("*********Rules*********\n1) You choose and the computer chooses\n2) Rock smashes  scissors -> Rock wins\n3) Scissors cut paper\n4) Paper covers rock -> Paper wins")







# ###########################################
    
# user_choice=input("Enter your choice (rock, paper, scissors):").lower()
        
# if user_choice not in ["rock","paper","scissors"]:
#         print("Invalid choice. Please run the program again and choose rock, paper, or scissors.")   
# elif user_choice=="rock":
#            print(f"You chose:\n{myrock}")
# elif user_choice=="paper":
#            print(f"You chose:\n{mypaper}")
# else :
#            print(f"You chose:\n{myscissors}")
        
    





# ###

# computer_choice=random.choice(["rock","paper","scissors"])

# if computer_choice=="rock":
#        print(f"computer chose:\n{myrock}")

# elif computer_choice=="paper":
#        print(f"computer chose:\n{mypaper}")
# else: 
#        print(f"computer chose:\n{myscissors}")


# #
# if user_choice==computer_choice:
#     print("It is a tie!")

# elif (user_choice== "rock" and computer_choice=="scissors")or (user_choice=="paper" and computer_choice=="rock")or (user_choice=="scissors" and computer_choice=="paper"):
#     print(f"You win! {user_choice} beats {computer_choice}")
# else:
#     print(f"You lose! {computer_choice} beats {user_choice}")
   
































# ########################################### Loops
# name="Ahmed"
# for myname in name:
#     print(myname.upper())










# colors=["blue","yellow","red","pink"]
# #colors[0]="Blue is my favorite color"
# for color in colors:
#     if color=="blue":
#        print("Blue is my favorite color")
#     else:
#        print(color)           

           






# numbers=[1,2,3,4,5,6,7,8,9,10]
# for x in numbers:
#     if x==1 or x==3 or x==5 or x==7 or x==9:
#         print()

#     else:
#         print(f"{x}\n")




# print("Finished the loop successfully")













# numbers=[1,2,3,4,5,6,7,8,9,10]
# for x in numbers:
#     if x%2==0:
#         print(f"{x}\n")
   

# print("\nFinished the loop successfully")











# numbers=[1,2,3,4,5,6,7,8,9,10]
# for x in numbers:
#     if x==2 or x==4 or x==6 or x==8 or x==10:
#          print(f"{x}\n")
   

# print("\nFinished the loop successfully")





# names=["Alice","Bob","Charlie","David","Eve"]
# for person in names:
#     print(person)
#     confirm=input("Is this person attending?(yes/no):").lower()
#     if confirm=="yes":
#         print("Attendance confirmed\n------")

#     elif confirm=="no":
#         print("Attendance not confirmed\n------")

#     else:
#         print("Invalid choice. Please enter yes or no.")









# names=[]
# mynames=input().append(names)
# print(names)











#names=input("Enter the names of attendees sprated by a comma:nter the names of attendees").split(",")
#mynames=names.split(",")
#allnames=[]
#allnames.append(names)
#print(allnames)
#for person in allnames[0]:
#    print(f"\n{person}")
#    confirm=input("Is this person attending? (yes/no):").lower()
#    if confirm=="yes":
#       print("Attendance confirmed\n------")
#    elif confirm=="no":
#        print("Attendance not confirmed\n------")
#    else:
#        print("Invalid choice. Please enter yes or no.")








from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/free_slots', methods=['POST'])
def free_slots():
    data = request.json
    
    booked = data.get('booked_slots', [])
    duration = int(data.get('duration', 60))
    work_start = data.get('work_start', '09:00')
    work_end = data.get('work_end', '21:00')
    requested_time = data.get('requested_time', '')

    fmt = '%H:%M'
    ws = datetime.strptime(work_start, fmt)
    we = datetime.strptime(work_end, fmt)
    rt = datetime.strptime(requested_time, fmt)
    rt_end = rt + timedelta(minutes=duration)

    booked_parsed = []
    for b in booked:
        s_dt = datetime.fromisoformat(b['start'].replace('Z', '+00:00'))
        s_str = (s_dt + timedelta(hours=3)).strftime('%H:%M')
        s = datetime.strptime(s_str, fmt)
        
        e_dt = datetime.fromisoformat(b['end'].replace('Z', '+00:00'))
        e_str = (e_dt + timedelta(hours=3)).strftime('%H:%M')
        e = datetime.strptime(e_str, fmt)
        booked_parsed.append((s, e))

    conflict = False
    for (s, e) in booked_parsed:
        if rt < e and rt_end > s:
            conflict = True
            break

    free = []
    current = ws
    while current + timedelta(minutes=duration) <= we:
        current_end = current + timedelta(minutes=duration)
        is_free = True
        
        for (s, e) in booked_parsed:
            if current < e and current_end > s:
                is_free = False
                break
        if is_free:
            free.append(current.strftime(fmt))
        current += timedelta(minutes=duration)

    return jsonify({
        'conflict': conflict,
        'free_slots': free
    })
import requests as req

VF_API_KEY = "VF.DM.6a1fa0a61170c413c675898c.p1cnh386niQf8SFI"
VF_VERSION_ID = "main"
VF_PROJECT_ID = "6a1f9adbaf8ad1542a2b58b1"

sessions = {}

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    from_number = request.form.get('From', '')
    body = request.form.get('Body', '').strip()
    
    user_id = from_number.replace('whatsapp:', '').replace('+', '')
    
    #is_new = user_id not in sessions or body.lower() in ['hello', 'hi', 'start']
    is_new = body.lower() in ['hello', 'hi', 'start']
    
    if is_new:
        sessions[user_id] = True
        vf_body = {
            "action": {"type": "event", "payload": {"event": {"name": "start_booking_2"}}},
            "config": {"tts": False, "stripSSML": True}
        }
    else:
        vf_body = {
            "action": {"type": "text", "payload": body},
            "config": {"tts": False, "stripSSML": True}
        }
    
    headers = {
        "Authorization": VF_API_KEY,
        "Content-Type": "application/json",
        "versionID": VF_VERSION_ID
    }
    
    url = f"https://general-runtime.voiceflow.com/state/user/{user_id}/interact"
    response = req.post(url, json=vf_body, headers=headers)
    data = response.json()
    
    messages = []
    for item in data:
        if item.get('type') == 'text':
            messages.append(item['payload']['message'])
    
    reply = '\n\n'.join(messages) if messages else ''
    
    from twilio.twiml.messaging_response import MessagingResponse
    resp = MessagingResponse()
    if reply:
        resp.message(reply)
    return str(resp)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)







