#WELCOME TO EI-Q Buddy!

print("Dear User, Greetings from EI-Q Buddy!")

user_name = (input("\nEnter your name here : "))
print("Please provide your information as required to continue with the program.")


user_age = None
while True:
    try:
        user_age = int(input("\nEnter your age here : "))
    except ValueError:
        print("\nInvalid entry, Enter something valid this time by using a number!")
        continue
    else:
        break
print("I appreciate you for providing your age!")


user_gender = input("\nEnter your gender (Male or Female): ").lower()
print("I appreciate you for providing your gender!")
if user_gender == "male":
    print("\nGreetings Mr.", user_name, "!")
elif user_gender == "female":
    print("\nGreetings Ms.", user_name, "!")
else:
    print("\nGreetings", user_name, "!")

intro = input("\nEnter 'P' to continue the test, or 'I' to learn more about the game. : ").upper()
if intro == "I":
    print("Let's learn more about IQ and EQ!\nIQ, which stands for Intelligence Quotient, refers to the measure of "
              "your capacity to understand and solve issues is measured by your IQ, or intelligence quotient.\n"
              "In comparison to other individuals in your age, it shows how well you performed on a particular test. "
              "Meanwhile, EQ, which stands for Emotional Quotient, refers to the ability to recognize, manage, "
              "and control your own emotions in order to reduce stress, improve communication, empathize with others, "
              "overcome obstacles, and \ndefuse conflicts.")
elif intro == "P":
    print("\nThe test is about to begin!")
else:
    print("Please select and enter the suitable answer!")


# IQ TEST QUESTIONS

iq_questions = [" \n1. You are in a dark room with a candle, a wood stove, and a gas lamp. If you only have one match, what do you light first? ",
                " \n2. You answer me although I never ask you questions. What am I? ",
                " \n3. If you rearrange the letters of 'ahret' you would have the name of a:",
                " \n4. Which of the five is least like the other four? ",
                " \n5. The capital of Turkey is a strange word. Would you please spell “it”? ",
                " \n6. Three of the following numbers add up to twenty-seven. 6, 22, 13, 17, 14, 5  ",
                " \n7. Some months have 31 days. Some have 30. How many have 28? ",
                " \n8. 3, 7, 13, 21, 31. What number comes next in the sequence?",
                " \n9. I have three apples. If you take away two from me, how many do you have? ",
                " \n10. Which is greater: six dozen or half a dozen? ",

                ]

iq_answer_options = [" A. The Match\n B. A Candle\n C. A Wood Stove\n D. Gas Lamp\n\nAnswer: ",
                     " A. Computer\n B. Telephone\n C. Pendrive\n D. Harddisk\n\nAnswer:",
                     " A. Vehicle\n B. Fish\n C. River\n D. Planet\n\nAnswer:",
                     " A. Eel \n B. Shark \n C. Dolphin \n D. Turtle\n\nAnswer:",
                     " A. Colombo \n B. Ankara C. It \n D. Berlin\n\nAnswer:",
                     " A. True \n B. False \n\nAnswer:",
                     " A. 1 \n B. 2\n C. 28 \n D. 12 \n\nAnswer:",
                     " A. 37\n B. 45\n C. 43\n D. 39\n\nAnswer:",
                     " A. 1\n B. 2\n C. 3\n D. 4\n\nAnswer:",
                     " A. One\n B. Six\n C. Three\n D. Nine\n\nAnswer:",

                    ]

iq_correct_option = ["A", "B", "D", "D", "C", "B", "C", " C", "B", "B", ]

# EQ TEST QUESTIONS

eq_questions = ["\n1. Emotional intelligence is characterised by: ? ",
                "\n2. Some people tend to be disconnected from their emotions.What can be a reason for this?",
                "\n3. Assume you had hoped to get an A in one of your courses, but you have just found out you got a C on the midterm. What do you do?",
                "\n4. You and your boyfriend/girlfriend have gotten into an argument that has escalated into a shouting match. In the heat of the moment, you are both making personal attacks that you don't really mean. What's the best thing to do?",
                "\n5. You have been assigned to lead a work group that is trying to come up with a creative solution to a nagging problem at work. What is the first thing you do?",
                "\n6. What is an indicator of emotional awareness?",
                "\n7. What entails the attribute of social awareness?",
                "\n8. You are a manager in an organization that is trying to encourage respect for racial and ethnic diversity. You overhear someone telling a racist joke. What do you do?",
                "\n9. Which of the following is a technique in reducing stress in the heat of a moment?",
                "\n10. I listen to others with patience and understanding. Choose the correct option",
                ]

eq_answer_options = ["\n A.Proficient in problem solving\n B.Better interpersoanl relationship\n C.Indulging in soothing or relaxing activities\n D.Maintaining physical and emotional health at all times\n\nAnswer: ",
                     " A. A dominant personality\n B. Unhappy childhood experiences\n C. High absract thinking ability\n D. Good sense of humor\n\nAnswer:",
                     " A. Sketch out a specific plan for ways to improve your grade and resolve to follow through on your plans\n B. Resolve to do better in the future\n C. Tell yourself it really doesn't matter much how you do in that particular course, and concentrate instead on other classes where your grades are higher\n D. Go to the professor and try to talk her into giving you a better grade\n\nAnswer:",
                     " A. Take a 20-minute break and then continue the discussion. \n B. Stop the argument - stay silent, no matter what your partner says. \n C. Say that you're sorry and ask your partner to apologize too. \n D. Stop for a moment, collect your thoughts, and then state your side of the argument as clearly as you can.\n\nAnswer:",
                     " A. Draw up an agenda and allot time for discussion of each item so you make best use of your time together.\n B. Have people take the time to get to know each other better.\n C. Begin by asking each person for ideas about how to solve the problem, while ideas are fresh.\n D. Start with a brainstorming session, encouraging everyone to say whatever comes to mind, no matter how wild their idea is.\n\nAnswer:",
                     " A. Keeping quiet when conflicts are happening\n B. Letting emotions shift from negative to positive and vice versa, depending on the situation\n C. Recognizing and experiencing distinct emotions\n D. Channeling negative emotions to physical activities\n\nAnswer:",
                     " A. You can understand the emotions, needs, and concerns of other people, pick up on emotional cues,feel comfortable socially, and recognize the power dynamics in a group or organization\n B. You’re able to control impulsive feelings and behaviors, manage your emotions in healthy ways,take the initiative, follow through on commitments, and adapt to changing circumstances\n C. You recognize your own emotions and how they affect your thoughts and behavior,know your strengths and weaknesses, and have self-confidence\n D. You know how to develop and maintain good relationships, communicate clearly,inspire and influence others, work well in a team, and manage conflict\n\nAnswer:",
                     " A. Ignore it—it's only a joke.\n B. Call the person into your office for a reprimand\n C. Speak up on the spot, saying that such jokes are inappropriate and will not be tolerated in your organization\n D. Suggest to the person telling the joke he go through a diversity training program\n\nAnswer:",
                     " A. Identifying and maximizing sensory stimuli that soothe and energizes a person\n B. By excessively indulging in a favorite hobby\n C. Confronting the person who is a source of your stress\n D. Letting all anger out by shouting, hitting something, or engaging in sports\n\nAnswer:",
                     " A. Strongly disagree\n B. Disagree\n C. Neither agree nor disagree\n D. Agree\n\nAnswer:",

                     ]

eq_correct_option = ["B", "C", "A", "D", "D", "C", "A", "C", "A", "D"]


# FUNCTION TO DELIVER THE IQ TEST, EVALUATE THE RESPONSE, AND DETERMINE THE SCORE

def start_game_iq():
    global iqscore_percentage
    iqscore = 0
    for iqquestion, iqoptions, iqcorrect_option in zip(iq_questions, iq_answer_options, iq_correct_option):
        print(iqquestion)
        user_iqanswer = input(iqoptions).upper()
        if user_iqanswer in iqcorrect_option:
            print(">>>>>>> Correct answer! <<<<<<<")
            iqscore += 1
        else:
            print(">>>>>>> Incorrect answer <<<<<<<")
            iqscore += 0
        print("\n")
    print("||||||||||     ", iqscore, "out of", len(iq_questions), "that is", float(iqscore / len(iq_questions)) * 100,
          "%      ||||||||||")
    iqscore_percentage = float(iqscore / len(iq_questions))*100


# FUNCTION TO DELIVER THE EQ TEST, EVALUATE THE RESPONSE, AND DETERMINE THE SCORE

def start_game_eq():
    global  eqscore_percentage
    eqscore = 0
    for eqquestion, eqoptions, eqcorrect_option in zip(eq_questions, eq_answer_options, eq_correct_option):
        print(eqquestion)
        user_eqanswer = input(eqoptions).upper()
        if user_eqanswer in eqcorrect_option:
            eqscore += 1
            print(">>>>>>> Correct Answer! <<<<<<<")
        else:
            print(">>>>>>> Incorrect Answer <<<<<<<")
            eqscore += 0
        print("\n")
    print("||||||||||     ", eqscore, "out of", len(eq_questions), "that is", float(eqscore / len(eq_questions)) * 100,
          "%      ||||||||||")
    eqscore_percentage = float(eqscore / len(iq_questions)) * 100


# FUNCTION TO RETAKE THE TESTS

def retry_test():
    response = input("\nThe IQ and EQ tests are starting soon; Are you ready?? (YES/NO): ").upper()

    if response == "YES":
        response_iqeq = input("\nEnter 'IQ' to take the IQ test first OR Enter 'EQ' to take the EQ test! : ").upper()
        if response_iqeq == "IQ":
            print("\n\n }}}}}}}}}} I WELCOME YOU TO THE IQ TEST {{{{{{{{{{")
            print("\nSelect the most appropriate answer out of the options A, B, C and D...")
            start_game_iq()
            print("\n\n }}}}}}}}}} I WELCOME YOU TO THE EQ TEST {{{{{{{{{{")
            print("\nSelect the most appropriate answer out of the options A, B, C and D...")
            start_game_eq()
            print("\n")
            print("=" * 100, "\n\n")

            print(" Well done,", user_name, ". The IQ and EQ tests were successfully completed! ")
            print("Name:", user_name, "\n", "Age:", user_age, "\n", "Gender:", user_gender)
            print("Your IQ test result:", eqscore_percentage, "%")
            print("Your EQ test result:", iqscore_percentage, "%")
            print("Your results has successfully been saved in a file!")
            file = open("ResultFile.txt", "w")
            textfile = "Name:\t" + user_name + "\n" + "Age:\t" + str(user_age) + "\n" + "Gender:\t" + user_gender + "\n" + "IQ result: " + \
                       str(iqscore_percentage) + "/100" + "\n" + "EQ Result: " + str(eqscore_percentage) + "/100"
            file.write(textfile)
            file.close()
            print("\n\t\tDo you wish to retake the tests?")

            retry_test()
        elif response_iqeq == "EQ":
            print("\n\n }}}}}}}}}} I WELCOME TO THE EQ TEST {{{{{{{{{{")
            print("\nSelect the most appropriate answer out of the options A, B, C and D...")
            start_game_eq()
            print("\n\n }}}}}}}}}} I WELCOME TO THE IQ TEST {{{{{{{{{{")
            print("\nSelect the most appropriate answer out of the options A, B, C and D...")
            start_game_iq()
            print("\n")
            print('=' * 100, "\n\n")
            print(" Well done,", user_name, ". The IQ and EQ tests were successfully completed! ")
            print("Name:", user_name, "\nAge:", user_age, "\nGender:", user_gender)
            print("Your IQ test result:", iqscore_percentage, "%")
            print("Your EQ test result:", eqscore_percentage, "%")
            print("Your results has successfully been saved in a file!")
            file = open("ResultFile.txt", "w")
            textfile = "Name:\t" + user_name + "\n" + "Age:\t" + str(
                user_age) + "\n" + "Gender:\t" + user_gender + "\n" + "IQ result: " + \
                       str(iqscore_percentage) + "/100" + "\n" + "EQ Result: " + str(eqscore_percentage) + "/100"
            file.write(textfile)
            file.close()
            print("\n\t\tDo you wish to retake the tests?")

            retry_test()
        else:
            print("No data entered! Try once more, please")
            retry_test()
    elif response == "NO":
        print("\n ~~~~~~~~~~~~~~~ BYE! Until next time ~~~~~~~~~~~~~~~")
        exit()
    else:
        print("No data entered! Try once more, please")
        retry_test()

retry_test()
