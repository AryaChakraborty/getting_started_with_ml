try :
    x = int(input('gimme a number'))//int(input('gimme another number'))
    if x == 20 :
        raise Exception # creating an exception manually
except Exception :
    print('Sorry, something went wrong')
else : # if try doesn't give an exception
    print(x)
finally :
    print('Thank You')