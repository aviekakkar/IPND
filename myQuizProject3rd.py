quizData = {
"easy" :  "Computer programming is the process of ___1___ and building an executable computer program for accomplishing a specific computing task. Programming involves tasks such as: analysis, generating algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of ___2___ in a chosen programming language (commonly referred to as coding)[1][2]. The source code of a program is written in one or more languages that are intelligible to programmers, rather than machine code, which is directly ___3___ by the central ___4___ unit." ,

"medium" : " The purpose of programming is to find a sequence of ___1___ that will ___2___ the performance of a task (which can be as complex as an operating system) on a computer, often for solving a given problem. The process of ___3___ thus often requires expertise in several different subjects, including knowledge of the application domain, specialized algorithms, and formal ___4___.",
"hard" : "Tasks accompanying and related to programming include: testing, debugging, source code maintenance, implementation of build systems, and management of derived artifacts, such as the machine code of computer programs. These might be considered part of the ___1___ process, but often the term ___2___ development is used for this larger process with the term programming, implementation, or coding reserved for the actual writing of code. Software engineering combines engineering techniques with software development practices. ___3___ engineering is the ___4___  process. A hacker is any skilled computer expert that uses their technical knowledge to overcome a problem, but it can also mean a security hacker in common language."
}

quizAnswers = { "easy" : {0 : "designing", 1 : "algorithms", 2 : "executed", 3 : "processing"},
"medium" : {0 : "instructions", 1 : "automate", 2 : "programming", 3 : "logic"},
"hard" : {0 : "programming", 1 : "software", 2 : "Reverse", 3 : "opposite"}
}

currentQ = ['___1___','___2___','___3___','___4___']

quizType = raw_input("What level of difficulty would you like to be quized on sir?(easy, medium or hard)")

def chooseQuiz(quizType):
    """
        Input : Quiz difficulty level
        Behaviour : Takes the difficulty level and returns the appropiate quiz if input is easy medium or hard else it returns quits
        Return : appropiate quiz corresponding to the level
    """
    if quizType in ("easy" , "medium", "hard"):
        print ""
        print "Well, good choice!! lets begin the adventuree!!!"
        print ""
        print quizData[quizType]
        print ""
        startMyQuiz()
    else:
        print "oops invallid quiz type!!"


def startMyQuiz():
    """
    Input : None
    Behaviour : Performs the task of asking questions for each blank with 5 tries
    Return : Questions and appropiate try count
    """

    answerCount = 0
    correctResponses = 0
    max_number_of_tries = 5
    number_of_questions = 4

    while answerCount < max_number_of_tries :
        while correctResponses < number_of_questions:
            questionAnswer = raw_input("What do you feel is the answer to " + currentQ[correctResponses] + " ? ")
            if questionAnswer == quizAnswers[quizType][correctResponses]:
                print ""
                print "Wow you are smart!!"
                print ""
                quizData[quizType] = quizData[quizType].replace(currentQ[correctResponses],questionAnswer)
                print quizData[quizType]
                print ""
                correctResponses +=1
            else:
                print ""
                print "Opps!! you have " + str(max_number_of_tries - answerCount) + " tries leftt!!"
                print ""
                answerCount += 1
        answerCount += max_number_of_tries



chooseQuiz(quizType)
