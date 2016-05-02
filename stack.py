#!/usr/bin/env python

'''
A ptrhon programmer to imited a stack.
'''
stack = []

def Push_in():
    stack.append(raw_input('Please input a new string: ').strip())

def Pop_out():
    if len(stack) == 0:
        print 'Can not pop from a empty stack !'
    else:
        print 'Removed [', `stack.pop()` ,']'
#print "Removed [ '%s']" % stack.pop()

def View_stack():
    print stack

CMDs = {'u': Push_in, 'o': Pop_out, 'v': View_stack}

def showmenu():
    pr = '''
    p(U)sh
    p(O)p
    (V)iew
    (Q)uit
***************
    Entry a choise: '''

    while True:
        while True:
            try:
                print '*' * 15,
                choise = raw_input(pr).strip()[0].lower()
            except(EOFError,KeyboardInterrupt,IndexError):
                choise = 'q'

            print '\nYou picked: [%s]' % choise
            if choise not in 'uovq':
                print 'Invalid option, try again!'
            else:
                break

        if choise == 'q':
            break
        
        CMDs[choise]()
        
if __name__ == '__main__':
    showmenu()
            

