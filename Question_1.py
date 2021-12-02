import re
import nltk
from queue import Queue

def main():
    
    #read txt file to string
    with open ("ide.txt", "r") as myfile:
        data = myfile.read()

    #tokenize the string
    tokens = nltk.wordpunct_tokenize(data)

    #regex for categories
    keywords = "System|out|println|break|case|char|const|continue|default|do|double|else|float|for|if|int|long|register|return|short|static|struct|switch|void|while|string|class"
    special = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
    operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
    numbers = "^(\d+)$"
    identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"

    keywordDict = ["for", "if", "else", "while", "do", "int", "float", "switch"]
    codes = ["(FOR_CODE, 30)", "(IF_CODE, 31)", "(ELSE_CODE, 32)", "(WHILE_CODE, 33)", "(DO_CODE, 34)", "(INT_CODE, 35)", "(FLOAT_CODE, 36)", "(SWITCH_CODE, 37)"]

    queue = []

    for i in tokens:
        queue.append(i)

    while(len(queue) != 0):
        lex = queue.pop(0)
        print("Next lexem is: ", lex)

        if(lex == keywordDict[0]):
            forFunction(queue)
            break

        if(lex == keywordDict[1]):
            ifFunction(queue)
            break

        if(lex == "else"):
            print('ERROR - CANNOT ELSE WITHOUT IF')

        if(lex == keywordDict[3]):
            whileFunction(queue)
            break

        if(lex == keywordDict[4]):
            doFunction(queue)
            break

        if(lex == keywordDict[7]):
            switchFunction(queue)
            break

def forFunction(queue):
    print("<FOR FUNCTION ENTERED>")
    lex = queue.pop(0)
    print("Next lexem is: ", lex)
    if(lex != "("):
        print("<ERROR - '(' MISSING>")
    else:
        print("<ARGS>")
        lex = queue.pop(0)
        print("Next lexem is: ", lex)
        if(lex != ")"):
            print("<ERROR - ')' MISSING>")
        else:
            lex = queue.pop(0)
            print("Next lexem is: ", lex)
            if(lex != "{"):
                print("ERROR - '{' MISSING>")
            else:
                #when the block in entered, it is assumed that there are arguments within the block. 
                #entering arguments inside the IDE.txt enclosed in { } will cause an error.
                print("<BLOCK ENTERED>")
                lex = queue.pop(0)
                print("Next lexem is: ", lex)
                if(lex != "}"):
                    print("ERROR - '}' MISSING>")
                else:
                    print("<BLOCK EXITED>")

def switchFunction(queue):
    print("<SWITCH FUNCTION ENTERED>")
    lex = queue.pop(0)
    print("Next lexem is: ", lex)
    if(lex != "("):
        print("<ERROR - '(' MISSING>")
    else:
        print("<ARGS>")
        lex = queue.pop(0)
        print("Next lexem is: ", lex)
        if(lex != ")"):
            print("<ERROR - ')' MISSING>")
        else:
            lex = queue.pop(0)
            print("Next lexem is: ", lex)
            if(lex != "{"):
                print("ERROR - '{' MISSING>")
            else:
                #when the block in entered, it is assumed that there are arguments within the block. 
                #entering arguments inside the IDE.txt enclosed in { } will cause an error.
                print("<BLOCK ENTERED>")
                lex = queue.pop(0)
                print("Next lexem is: ", lex)
                if(lex != "case" and lex != "default"):
                    print("ERROR - MUST BE A CASE OR DEFAULT")
                else:
                    lex = queue.pop(0)
                    print("Next lexem is: ", lex)
                    if(lex != ":"):
                        print("ERROR - NO ':' DETECTED")
                    else:
                        lex = queue.pop(0)
                        print("Next lexem is: ", lex)
                        if(lex != "}"):
                            print("ERROR - '}' MISSING>")
                        else:
                            print("<BLOCK EXITED>")

def ifFunction(queue):
    ifBool = False
    print("<IF FUNCTION ENTERED>")
    lex = queue.pop(0)
    print("Next lexem is: ", lex)
    if(lex != "("):
        print("<ERROR - '(' MISSING>")
    else:
        print("<ARGS>")
        lex = queue.pop(0)
        print("Next lexem is: ", lex)
        if(lex != ")"):
            print("<ERROR - ')' MISSING>")
        else:
            lex = queue.pop(0)
            print("Next lexem is: ", lex)
            if(lex != "{"):
                print("ERROR - '{' MISSING>")
            else:
                #when the block in entered, it is assumed that there are arguments within the block. 
                #entering arguments inside the IDE.txt enclosed in { } will cause an error.
                print("<BLOCK ENTERED>")
                lex = queue.pop(0)
                print("Next lexem is: ", lex)
                if(lex != "}"):
                    print("ERROR - '}' MISSING>")
                else:
                    print("<BLOCK EXITED>")
                    ifBool = True

    if(lex == "else" and ifBool == False):
        print('ERROR - CANNOT ELSE WITHOUT IF')
    else:
        lex = queue.pop(0)
        print("Next lexem is: ", lex)
        lex = queue.pop(0)
        print("Next lexem is: ", lex)
        if(lex != "{"):
                print("ERROR - '{' MISSING>")
        else:
            print("<BLOCK ENTERED>")
            lex = queue.pop(0)
            print("Next lexem is: ", lex)
            if(lex != "}"):
                print("ERROR - '}' MISSING>")
            else:
                print("<BLOCK EXITED>")

def whileFunction(queue):
    print("<WHILE FUNCTION ENTERED>")
    lex = queue.pop(0)
    print("Next lexem is: ", lex)
    if(lex != "("):
        print("<ERROR - '(' MISSING>")
    else:
        print("<ARGS>")
        lex = queue.pop(0)
        print("Next lexem is: ", lex)
        if(lex != ")"):
            print("<ERROR - ')' MISSING>")
        else:
            lex = queue.pop(0)
            print("Next lexem is: ", lex)
            if(lex != "{"):
                print("ERROR - '{' MISSING>")
            else:
                #when the block in entered, it is assumed that there are arguments within the block. 
                #entering arguments inside the IDE.txt enclosed in { } will cause an error.
                print("<BLOCK ENTERED>")
                lex = queue.pop(0)
                print("Next lexem is: ", lex)
                if(lex != "}"):
                    print("ERROR - '}' MISSING>")
                else:
                    print("<BLOCK EXITED>")

def doFunction(queue):
    print("<DO WHILE FUNCTION ENTERED>")
    lex = queue.pop(0)
    print("Next lexem is: ", lex)
    if(lex != "while"):
        print("ERROR - WHILE MISSING")
    else:
        lex = queue.pop(0)
        print("Next lexem is: ", lex)
        if(lex != "("):
            print("<ERROR - '(' MISSING>")
        else:
            print("<ARGS>")
            lex = queue.pop(0)
            print("Next lexem is: ", lex)
            if(lex != ")"):
                print("<ERROR - ')' MISSING>")
            else:
                lex = queue.pop(0)
                print("Next lexem is: ", lex)
                if(lex != "{"):
                    print("ERROR - '{' MISSING>")
                else:
                    #when the block in entered, it is assumed that there are arguments within the block. 
                    #entering arguments inside the IDE.txt enclosed in { } will cause an error.
                    print("<BLOCK ENTERED>")
                    lex = queue.pop(0)
                    print("Next lexem is: ", lex)
                    if(lex != "}"):
                        print("ERROR - '}' MISSING>")
                    else:
                        print("<BLOCK EXITED>")

if __name__ == "__main__":
    main()