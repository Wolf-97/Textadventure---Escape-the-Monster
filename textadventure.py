
Level = 1
Question = 0

Done = False

while not Done:   
    
    ja = ["Yes", "Ye", "Y", "yes", "ye", "y", "Ja", "ja"]
    nein = ["No", "no","n", "N", "nein", "Nein"]

    if Question == 0:
        Done1 = False

        while not Done1:
            print()     
            print()
            print("Welcome to \"Escape the Monster\"!")
            print("Would you like to play? Yes, No")

            eingabe = []
            eingabe = input("")

            if eingabe in ja:
                print("Welcome to Level 1 of \"Escape the Monster\"!")
                Done1 = True
                Question += 1
            elif eingabe in nein:
                print()
                print("Have a great day!")
                print("Till next time!")
            else:
                print()
                print("ERROR")

    elif Question == 1:
        print("You were laying around your home like always. It was around midnight.")
        print("Suddenly you hear a loud commotion outside your house.")
        print("As fast as the commotion came, it went away again.")
        print("Out of curiosity to know what all of this was about")
        print("you went to your window and took a peek.")
        print("What you saw gave you the chills.")
        print("Every single car was thrown over or demolished.")
        print("Even the street lights were bend over and destroyed.")
        print()
        print("Out of curiosity and greeness you go outside")
        print("You walk around for a bit and look at all the destruction that has been done.")
        print("After a few minutes of walking you suddenly hear a deafening scream.")
        print("Your are so shocked and scared that you can't move. Not even a little bit.")
        print("But the longer you stay there, the higher the possibility that")
        print("whatever kind of thing produced this deafening scream,")
        print("will find you and do something.")
        print()
        print("\"Answer the following Question to start moving\"")
        print("What's the solution of the following equation?")

        eingabe = input("60 + 40 * 5 = ")

        if eingabe == '260':                                                              
            print("That's correct!")
            print("Somehow you luckily regained your senses.")
            print("You finally came back to yourself and realized")
            print("in what kind of situation you are in.")
            Question += 1
        else:
            print ("That's incorrect")
            print()
            print("No matter what you try you just can't move.")
            print("After a few seconds you hear how something heavy is coming your way")
            print("Next thins you know is that an abnormal big Demon like")
            print("creature stands infront of you and looks you dead in the eyes.")
            print("Now you stand there even more frozen up by the fear that runs through you.")
            print("The \"Demon\" looks at you")
            print("ERROR in the Game")
            print("You seem to have been killed")
            print("Please try again")
            Question = 1
       

    elif Question == 2:

        print("Next thing you know is that you are turning")
        print("on your heal and run with full spead into the opposite")
        print("direction from where the scream came.")
        print("You don't want to stand there and wait")
        print("till whatever this thing was finds you and KILLS you.")
        print("While you're running you pray for your life and just hope to")
        print("get out of there alive.")
        print()
        print("Suddenly you hear the deafening scream again.")
        print("The scream is getting closer and closer to you....")
        print()
        print("Who was the king of Pop? (1; Lady Gaga: 2; Mickael Jackson: 3; Justin Bieber)")
        eingabe = input("Answer with 1, 2 or 3: ")

        if eingabe == '2':
            print ("That's correct")
            print()
            print("Suddenly you see an alleyway")
            print("Without thinking much further you run straight into the alleyway.")
            print("You hide behind a dumpster and even hold your breathing")
            print("You wait till you're sure that this monster is not anywhere close by.")
            Question += 1
        else:
            print("That's incorrect")
            print("You run and run....")
            print("You try to speed up as much as you can.")   
            print("But no matter what you do you just can't seem to get faster.")
            print("Suddenly this Monster is right behind you.")
            print("It's catching up really fast and makes you pray for")
            print("your life even more.")
            print("But there's no escape....")
            print()
            print("In the end the Monster catched you and KILLED you.")
            print("Please try again.")
            Question = 1           

    
    elif Question == 3:
        print("What's the solution of the following equation?")
        print("3(x + 7) = 4(2x - 1)")
        print()

        eingabe = input("x = ")

        if eingabe == '5':
            print("That's correct")
            print("After you made sure that the Monster wasn't near you.")
            print("You finally breathed out.")
            print("This sure was a crazy rollercoaster of emotions.")
            print("For now you seem to be safe.")
            print("You decide to go farther away from the Monster.")
            Question += 1
        else:
            print("That's incorrect")
            print("You walk to the right. You think it's the opposite direction of the Monster.")
            print("But you were so wrong. Before you can realize what happened someone")
            print("or more like something had a thight grip around your waist.")
            print("No matter what you did. How hard you tried.")
            print("The Monster just didn't let you go.")
            print()
            print("Please try again.")
            Question = 1
    
    elif Question == 4:
        print("How many hearts does an Octopus have? 1, 2 or 3?")

        eingabe = input("")

        if eingabe == '3':
            print("That's correct!")
            print("You walked for quite a while now.")
            print("One thing you noticed on your way was that...")
            print("there was no one else besides you.")
            print("No matter where you looked it seemed as if everybody")
            print("dissapeared suddenly...")
            print("")
            Question += 1
        else:
            print("That's incorrect!")
            print("You turn to the left and walk into a")
            print("Dark alleyway...")
            print("Suddenly you hear light footsteps")
            print("Then you see red eyes glowing in the dark.")
            print("They look right into your eyes.")
            print()
            print("ERROR")
            print()
            print("You've gotten killed by the Monster.")
            print("Please try again.")
            Question = 1
        

    elif Question == 5:
        print("What's the error?;")
        print("supercalifragilisti  g  expialido  c  ious")
        print("1; g = c")
        print("2; c = k")
        print()

        eingabe = input("")

        if eingabe == '1':
            print("That's correct!")
            print("Now you were really creeped out.")
            print("When and where to did everybody disapear?)")
            print("With each second you became more sure")
            print("that you needed to leave")
            print("Right NOW!")
            Question += 1
        else:
            print("That's incorrect")
            print("The more you looked around")
            print("The more you felt like someone was watching you.")
            print("As you were searching for other peopole")
            print("Suddenly this huge thing jumps right infront of you.")
            print("It kills you in a small and slow death")
            print()
            print("Please try again")
            Question = 1

    elif Question == 6:
        print("How much longer did the 2WW last than the 1WW? 2 years; 3 years")

        eingabe = input("")

        if eingabe in ["3", "3 years", "3 Years"]:
            print("That's correct!")
            print("You ran like you've never run before.")
            print("It was hard but you somehow made it quite far.")
            print("When you finally stopped running you looked around.")
            print("You realized that you were at a place that you've")
            print("Never seen before.")
            print("Before you go furthter you decide to look around.")
            Question += 1
        else:
            print("That's incorrect")
            print("You run for your life.")
            print("After a good 20-30 Minutes of running you ")
            print("finally decide to take a little break.")
            print("This turns out to be a huge mistake...")
            print("Someone shoots something into your neck and you pass out")
            print("Next thing you know is that you are looking")
            print("at two big red and angry eyes.")
            print("They're creeping you out but you can't move.")
            print("Suddenly this things starts torturing you.")
            print("Starting off with cutting off every limp of your body.")
            print("Your cause of death is: Died of too much Bloodlos")
            print("Please try again")
            Question = 1

    elif Question == 7:
        print("You now are running to the right.")
        print("You have no idea where you are as of now.")
        print("You only hope to escape this horrible nightmare")
        print("")
        print("What's the name of the fandom of the most influential Group in the world?")

        eingabe = []
        eingabe = input("")

        if eingabe in ["ARMY", "army", "Army"]:
            print("That's correct!")
            Question += 1
        else:
            print("That's incorrect!")
            print("Shame on you for not knowing.")
            print("But yea I guess not everyone can have taste...")
            print("After you looked around you decide to go right.")
            print("This way seemes to be getting darked and lonlyer with each second.")
            print("Suddenly you cut yourself at something")
            print("You have no idea what it is but it's pretty deep.")
            print("You try walking further but in the end your wound interrupts you.")
            print("The wound is getting deeper with each step.")
            print("In the end you are not able to move any further.")
            print("So you decide to sit down for a while.")
            print("Suddenly something grabs you by your head an lifts you up.")
            print("Last thing you remember is that you looked in blood red eyes.")
            print("Please try again")
            Question = 1


    elif Question == 8:
        print("How many full cantons does Switzerland have?")

        eingabe = input("")

        if eingabe == '23':
            print("That's correct!")
            print("Switzerland has 3 half cantons.")
            Question += 1
        else:
            print("That's incorrect")
            print("There's a difference between one canton and a half canton.")
            print("Suddenly you hear sounds.")
            print("Like something heavy is coming your way.")
            print("Infact there is something heave coming your way.")
            Question = 1
        
    elif Question == 9:

        print("Name one of the three first cantons.")

        eingabe = input("")

        if eingabe in ["uri", "schwyz", "unterwalden", "Uri", "Schwyz", "Unterwalden"]:
            print("That's correct!")
            print("Suddenly something keeps you from moving.")
            print("You look down and see a little girl holding onto your leg.")
            print("She looks up at you and she tells you that")
            print("she lost her parents. She pleads you to take her with you.")
            Question += 1
        else:
            print("That's incorrect")
            print("")
            Question = 1

    elif Question == 10:
        print("Decide")
        print("Do you want to take the girl with you?")

        eingabe = input("")
        
        if eingabe in ja:
            print("You tell the little girl that she can come with you.")
            print("The eyes of the little Girl light up and she says:")
            print("\"Thank you, thank you so much\"")
            print("\"Please follow me I know a place where we are save\"")
            print()
            print()
            print()
            print("Congratulations you've made it!")
            print("You solved all 10 Questions correctly.")
            print()
            print("Do you want to play again or do you want to go to Level 2?")
            print("Play again   -> Yes")
            print("Level 2      -> Level up")

            eingabe1 = input("")

            if eingabe1 in ja:
                Question = 1
                Done2 = True
            elif eingabe1 in ["level up", "level", "Level up", "Level"]:
                Level += 1
            else:
                Done2 = True
                Done = True
        else:
            print("You decide yourself against taking the little girl with you.")
            print("You tell her that you can't help her and leave her")
            print("She gets sad and cries.")
            print("You walk away in the opposite direction and...")
            print("Suddenly the Monster is right behind you.")
            print("The eyes of the Monster stare directly into your eyes.")
            print("Then.....")
            print("The demon jumps at you and kills you slowly and painfuly.")
            Question = 1

    elif Level == 2:
        print("Hello and Welcome to Level 2!")
        print("Congratulations on ending the first Level!")
        print("You've made the right decision before but will you")
        print("be able to do this also on Level 2?")
        print()
        print("We're about to find out ;)")

        Question2 = 1

        Donelvl2 = False

        while not Donelvl2:
            if Level == 2:
                print("Hello and welcome to Question 1 of Level 2")
                Question2 += 1






    print()
    print("-" * 75)
    print()

