import random
def my_valid_choice(total_lists):
    valid_lists = []
    unpreferred_lists = []
    for each in total_lists:
        if each.find('-') != -1:
            unpreferred_lists.append(each)
        elif each.find('*') != -1:
            valid_lists.append(each) 
    if valid_lists:
        return random.choice(list("".join(valid_lists).replace('*','')))
    else:
        valid_lists = set(total_lists) - set(unpreferred_lists)
        choices = list("".join(valid_lists).replace('*',''))
        if choices:
            return random.choice(choices) 
        else:
            return 

def update_total_lists(val, guess, total_lists):
    for i, each in enumerate(total_lists):
        if each.find(str(val)) != -1:
            total_lists[i] = each.replace(str(val), guess)
    show_field(total_lists) 

def my_choice(total_lists):
    if '---' in total_lists:
        return 'You Lose!!!'
    for each in total_lists:
        if each.count('*') == 2 and each.count('-') != 1:
            print 'What have you done!!!!'
            update_total_lists(each.replace('*',''), '*', total_lists) 
            return 'You Win!!!'
    for each in total_lists:
        if each.count('-') == 2 and each.count('*') != 1:
            val = each.replace('-','') 
            print 'Ufff I saved the game'
            update_total_lists(val, '*', total_lists)
            return 'Saved the game'
    choice = my_valid_choice(total_lists)
    return choice

total_lists = ['123', '456', '789', '147', '258', '369', '159', '357']
my_valid_lists = []
comp_valid_lists = []
def show_field(total_lists):
    for i, each in enumerate(total_lists):
        print each
        if i>=2:
            break
show_field(total_lists)

toss = raw_input("Choose Heads(0) or Tails(1). Please input '0'/'1' or 'H'/'T' ")
choice = random.choice(range(2))
if toss.lower() not in ['h', 't', '0', '1']:
    print 'you have not chosen a valid value hence, considering your input as Head '
    toss = 'h'

if choice == 0 and toss in ['h', '0']:
    winner = 'player1'
    print 'You win the toss'
elif choice == 0 and toss not in ['h', '0']:
    winner = 'comp'
    print 'You lose the toss'
elif choice == 1 and toss in ['t', '1']:
    winner = 'player1'
    print 'You win the toss'
else:
    winner = 'comp'
    print 'You lose the toss'

while True: 
    if winner == 'comp':
        mychoice = my_choice(total_lists)
        print 'Ok I have chosen ', mychoice
        update_total_lists(mychoice, '*', total_lists)
        winner = 'reset after 1st try'

    print 'Ok player your turn'
    opponent_inp = raw_input('select a valid input from the field ')
    update_total_lists(opponent_inp, '-', total_lists)
    #print total_lists
    mychoice = my_choice(total_lists)
    if mychoice == 'You Win!!!':
        print 'Game over!! I win!!!'
        break
    if mychoice == 'You Lose!!!':
        print 'Game over!! Well played! You win!!!'
        break
    elif mychoice == 'Saved the game': 
        continue
    elif mychoice == None: 
        print 'Draw!!'
        break
    else:
        print 'Ok I am updating {}'.format(mychoice)
        update_total_lists(mychoice, '*', total_lists)
