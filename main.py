# main
# chatbot read in user input and respond with corresponding response.
import random as rand
import pandas as pd
import sys
from datetime import datetime
import csv

df = pd.read_csv(r"testchatbot2.csv")
command = df['Command']
response1 = df['Response1']
resposne2 = df['Response2']


def greetings(forms_of_greetings):
    i = rand.randrange(1, 3, 1)

    if forms_of_greetings == "end" or forms_of_greetings == "End":
        sys.exit("End of our conversation")

    if forms_of_greetings == "hey" or forms_of_greetings == "Hey" or forms_of_greetings == "Hi" or forms_of_greetings == "hi":

        if i == 1:
            print("What can I do for you? ")

        elif i == 2:
            print("How may I help you? ")

        elif i == 3:
            print("Is there anything I can do for you? ")

    else:
        normal_talks(forms_of_greetings)
        return


def unlearn_command():
    unlearn = input("What should I unlearn?: ")
    is_learned = df.loc[df['Command'].str.contains(unlearn, case=False)]
    if is_learned.empty == True:
        print("I did not learn that before")
        Cont_learning = input("Would you like to to contine learning? ")
        Continue_learning(Cont_learning)

    else:
        lines = list()
        with open('testchatbot2.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == unlearn:
                        lines.remove(row)

        with open('testchatbot2.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        print("Unlearned successfully, Thank you.")
        Continue_chat = input("What can I do for you?: ")
        normal_talks(Continue_chat)
    return


def trainer():
    learn_or_unlearn = input("Should I learn or unlearn?")
    if learn_or_unlearn == "unlearn" or learn_or_unlearn == "Unlearn":
        unlearn_command()
    elif learn_or_unlearn == "learn" or learn_or_unlearn == "Learn":
        learn_command()
    else:
        print("Sorry, I do not understand you, would you like to continue learning?: ")
        cont_or_not = input()
        Continue_learning(cont_or_not)


def learn_command():
    train_command = input("What should I learn?: ")
    i = df.loc[df['Command'].str.contains(train_command, case=False)]

    if len(i.index.values) > 1:
        user_len = len(train_command)
        for y in range(len(i.index.values)):
            x = command[i.index.values[y]]
            if len(train_command) == len(x):
                print("I have learned that before, would you like to continue learning?: ")
                cont_or_not = input()
                Continue_learning(cont_or_not)

    response1 = input("What should the response be?: ")

    if response1 == "end" or response1 == "End":
        sys.exit("End of our conversation")

    response2 = input("what else should I reply?: ")

    if response2 == "end" or response2 == "End":
        sys.exit("End of our conversation")

    confirmation = input("Would you like me to learn that?: ")

    if confirmation == "yes" or confirmation == "Yes":
        df2 = pd.DataFrame(
            {
                'Command': [train_command],
                'Response1': [response1],
                'Response2': [response2]
            }
        )
        df2.to_csv('testchatbot2.csv', mode='a', index=False, header=False)
        print("I have learned the new knowledge, Thank you.")

        Cont_learning = input("Would you like to to contine learning? ")
        Continue_learning(Cont_learning)

    elif confirmation == "No" or confirmation == "no":
        Cont_learning = input("Would you like to to contine learning? ")
        Continue_learning(Cont_learning)
    else:
        bad_input_confirmation = input("Sorry, I do not understand you, would you like to continue learning?: ")
        Continue_learning(bad_input_confirmation)
    return


def Continue_learning(continue_or_not):
    if continue_or_not == "Yes" or continue_or_not == "yes":
        trainer()

    elif continue_or_not == "no" or continue_or_not == "No":
        Back_to_norm = input("What can I do for you?: ")
        normal_talks(Back_to_norm)

    else:
        badinput = input('Please let me know if you want to continue teaching, reply "Yes" or "No": ')
        Continue_learning(badinput)
    return


def normal_talks(user_input):
    df = pd.read_csv(r"testchatbot2.csv")
    command = df['Command']
    response1 = df['Response1']
    resposne2 = df['Response2']
    u = df.loc[df['Command'].str.contains(user_input, case=False)]
    if len(u.index.values) > 1:
        count = 0
        user_len = len(user_input)
        for i in range(len(u.index.values)):
            x = command[u.index.values[i]]
            if len(user_input) == len(x):
                print(response1[u.index.values[i]])
                count = count + 1
            else:
                count = count + 0
        if count == 0:
            print("I do not understand you")

        return
    if user_input == "trainerID001":
        trainer()
        return

    if user_input == "end" or user_input == "End":
        sys.exit("End of our conversation")

    if user_input.find("+") > -1:
        addition_input = user_input.replace("+", "\+")
        u = df.loc[df['Command'].str.contains(addition_input, case=False)]

    if u.empty == True:
        print("I do not understand you")
        return

    if df.loc[int(u.index.values), 'Response1'] == "date":
        print("Today is: ", datetime.now())
        return

    else:
        x = rand.randrange(1, 3, 1)

        if x == 1:
            y = df.loc[int(u.index.values), 'Response1']
            print(y)


        elif x == 2:
            y = df.loc[int(u.index.values), 'Response2']
            print(y)
    return

    i = df.loc[df['Command'].str.contains(user_input, case=False)]

    if i.empty == True:
        print("I do not understand you")
        return

    else:
        x = rand.randrange(1, 3, 1)

        if x == 1:
            y = df.loc[int(i.index.values), 'Response1']
            print(y)
            return

        elif x == 2:
            y = df.loc[int(i.index.values), 'Response2']
            print(y)
            return


value = input("Hello ")
greetings(value)
ask_for_user_input = input()
normal_talks(ask_for_user_input)

while ask_for_user_input != "end" or ask_for_user_input != "End":
    ask_for_user_input = input()
    normal_talks(ask_for_user_input)


