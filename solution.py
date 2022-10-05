list = [1,2,3,4,4,2,1]
newlist = []                    # this will be the answer
badlist = []                    # this will be the numbers the fucntion already passed so this will be a list with only numbers and repeated numbers

def onlynumber(x):
    for i in x:
        if i not in newlist and i not in badlist:     # checks if the number is not in newlist and not in the badlist (basically if its a new number)
            newlist.append(i)                         
            badlist.append(i)                          # here im adding the new numbers to the newlist and badlist
        elif i in badlist and i not in newlist:        # if its already in the badlist and not in newlist, its a repeated number and it was already removed from the answer so we can pass                                                          to the next number in the original list
            pass
        else:
            newlist.remove(i)    #  if the number is in newlist and badlist, then its because it is at least two times in the original list, so we need tp remove it from the answer
    print(newlist)

onlynumber(list)

string = "asd asda dasdad 123456789"

def lastwordcharacters(x):
    newstring = x[::-1]          # reverses the order of the string
    number = 0
    for i in newstring:          
        if i == " ":              # checks every letter from last to first, if its a space then you know the last word is over, so you break the for loop
            break
        else:
            number += 1           # counts the letters 
    print(number)

lastwordcharacters(string)
