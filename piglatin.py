

'''
1. Get string from person - DONE
2. Split each word - DONE
3. Store each word in an array/list - DONE
4. Get the first letter of each word
5. Add letter to the end of the word
6. Repeat for each word
7. Add -ay to each word - DONE
8. Print the completed word/sentence - DONE
'''

    
personText = input("Type the word you want to convert: ")


def ifNumbers(s):
    if (any(i.isdigit() for i in s) == True):
        print("No numbers please")
        
        

def PigLatinGen(z):
    ifNumbers(z)
    personSplit = personText.split(" ")
    print(personSplit)

    firstLetter = ([y[0] for y in personText.split()])

    print(firstLetter)
    trimLetter = [i[1:] for i in personSplit]

    for x in firstLetter:
        for y in trimLetter:
            print (y + x + "ay")

PigLatinGen(personText)
    
