#Christopher Stephenson
#COP2500 0V04
#Final Project - Surveys
#4/12/23

##########################################################################

######## SURVEYS FOR UCF STUDENTS TO COMPLAIN ABOUT THEIR CLASSES ########

######## AS WELL AS READ SUBMITTED SURVEYS TO SEE OTHER OPINIONS! ########

##########################################################################

#stores all sumbitted surveys in a list
survey = []

#asks for user input then places the input into the list
def survey_questions(subject):
    professor = str(input("Which professor did you have?\n")).strip()
    pros_cons = str(input("What were the pros and cons of your class?\n")).strip()
    improve = str(input("How could the professor improve the class?\n")).strip()
    learn = str(input("Would you say you learned from this class? If so what was the most important thing?\n")).strip()
    advise = str(input("What advise would you give to students who take this class next semester?\n")).strip()

    #adds a dict to the list
    survey.append({
        "Professor": professor,
        "Pros and Cons": pros_cons,
        "Improvements": improve,
        "Learned": learn,
        "Advise": advise
    })

    print("Your submission has been added to the survey responses!")
    
#views the submitted surveys and organizes them so it's easy to read
def view_surveys():
    if not survey:
        print("There are no survey responses yet.")
        print()
        return

    print("\nSurvey Responses:")
    print("-----------------")

    #loops through the responses and adds them to its own line
    for response in survey:
        print("Professor:", response["Professor"])
        print("Pros and Cons:", response["Pros and Cons"])
        print("Improvements:", response["Improvements"])
        print("Learned:", response["Learned"])
        print("Advise:", response["Advise"])
        print("-----------------")

#menu to choose which class survey to take or view sumbitted surveys
def menu():
    print("Welcome to the open surveys!")
    print("----------------------------")
    print("Which class survey would you like to take?")
    print("1. CS Concepts")
    print("2. Trigonometry")
    print("3. Technical Writing")
    print("4. Intro to C")
    print("5. View Survey Responses")
    print("6. Exit")
    choice = int(input("Choose a number:\n"))
    return choice


def main():
    #varible allows option to be called in the func
    option = 0

    #displays menu until user chooses to exit
    while (option != 6):
        option = menu()

        #if/elif/else statements that will call the needed function given what option the user chose
        if (option == 1):
           survey_questions("CS Concepts")

        elif (option == 2):
           survey_questions("Trigonometry")

        elif (option == 3):
           survey_questions("Technical Writing")

        elif (option == 4):
           survey_questions("Intro to C")

        elif (option == 5):
            view_surveys()

        elif (option == 6):
            print("Tell your friends about these surveys. Bye!")

        else:
            print("That's not an option.")
            print()
main()
