#-*- coding: utf-8 -*-

###
def indict(alist):
    adict = {}
    for i in alist:
        adict[i] = alist.index(i)
    return(adict)

	
###	

def guess():
    a = input("Please enter four numbers: ")
    b = list(a)
    c = b[0:4]
    d = ['0','1','2','3','4','5','6','7','8','9']
    for i in c:
        if i not in d:
            print ('invalid guess')
            guess()
	    else:
	        continue
	return()


	
###
def game():
    def comp(old, new):
        result = [0,0]
        for i in new.keys():
            if i in old.keys():
                result[0] += 1
                if new[i] == old[i]:
                    result[1] += 1
        return(result)
    count = 10
    while count > 0:
        E1 = list(input("Please enter four numbers: "))[0:4]
        compare = comp(indict(R1), indict(E1))
        print ('correct number: %s' %compare[0])
        print ('correct position: %s' %compare[1])
        if compare[0] == 4 and compare[1] == 4:
            print ('CONGRATULATION, YOU WIN!')
            break
        count -= 1
        print ('You have %s chances.' %count)
    else:
        print ('GAME OVER!')
        print ('NUMBER is %s.' %R1)


import random
while(1):
    print ('---GUESS GAME---')
    command = input('Press "go" to start or Press "quit" to exit:\n')
    if command == 'go':
        R1 = random.sample('0123456789',4)
        game()
    elif command == 'quit':
        break
    else:
        pass
