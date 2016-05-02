#!/usr/bin/env python

'''A python programmer to imitate a queue !'''

queue = []

def enQ():
    queue.append(raw_input('Please input a new string: ').strip())

def deQ():
    if len(queue) == 0:
        print 'Cannot pop from an empty queue !'
    else:
        print 'Removed [', `queue.pop(0)` ,']'

def viewQ():
    print queue

CMDs = {'e': enQ, 'd': deQ, 'v': viewQ}

def showmenu():
    pr = '''
   (E)nqueue
   (D)equeue
   (V)iew
   (Q)uit
***************

   Entry a choise: '''

    while True:
        while True:
            try:
                print '*' *15,
                choise = raw_input(pr).strip()[0].lower()
            except(EOFError,KeyboardInterrupt,IndexError):
                choise = 'q'

            print '\nYou picked [%s]' % choise
            if choise not in 'edvq':
                print 'Invalid option, try again!'
            else:
                break

        if choise == 'q':
            print 'You will quit the menu of queue !'    
            break

        CMDs[choise]()

if __name__ == '__main__':
    showmenu()
