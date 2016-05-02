#!/usr/bin/env python

''' imitate a user login system'''
db = {}

def newUser():
    pr = "input a user's name: "

    while True:
        name = raw_input(pr).strip()

        if db.has_key(name):
            pr = '\nname used, try again: '
            continue
        else:
            break

    pw = raw_input('Please input passwd: ').strip()
    db[name] = pw

def oldUser():
    
    name = raw_input('Entry a user name: ').strip()
    passwd = raw_input('Entry a passwd: ').strip()

    '''if db[name] == None:
        print "\nYou login user's name is inexistence !"
        print "Please choose again!"
        showMenu()
    '''
    if passwd == db[name]:
        print '\nWelcome back: ',name,'\n','-'*35,'\n\n'
    else:
        print '\nThe  passwd you entered is incorrect!'
        print 'Login fail !','\n','-'*35,'\n\n'

def showMenu():

    pr = '''
    (N)ew user login
    (E)xisiting user login
    (Q)uit

    Entry your choise: '''

    done = False
    while not done:
        
        choese = False
        while not choese:
            
            try:
                print '\n','*' *25
                choise = raw_input(pr).strip()[0].lower()
                print '\n','*' *25
            except(EOFError,KeyboardInterrupt):
                choise = 'q'

            print '\n----------You picked [%s]----------' % choise
            if choise in 'neq':
                choese =True
            
        if choise == 'q': done = True; print 'You will leave the system!\n'
        if choise == 'n': newUser()
        if choise == 'e': oldUser()

if __name__ == '__main__':
    showMenu()



