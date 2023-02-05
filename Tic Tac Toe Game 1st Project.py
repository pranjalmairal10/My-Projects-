def display_board(board):
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])
def player_input():
    choice = 'wrong'
    while choice not in ['x','o']:
        choice = input('please enter the correct choice ie X or O :' )
        if choice in ['x','o']:
            if choice == 'x':
                print('player 1 has chosen x so player 2 will have o ')
                return choice
            else:
                print('player 1 has chosen o so player 2 will have x')
                return choice
def place_marker(board, marker, position):
    board[position] = marker
def win_check(board, mark):
    if mark == 'x':
        if board[1] == board[2] == board[3] == 'x':
            print('x won')
            return False
        elif board[4] == board[5] == board[6] == 'x':
            print('x won')
            return False
        elif board[7] == board[8] == board[9] == 'x':
            print('x won')
            return False
        elif board[1] == board[4] == board[7] == 'x':
            print('x won')
            return False
        elif board[2] == board[5] == board[8] == 'x':
            print('x won')
            return False
        elif board[3] == board[6] == board[9] == 'x':
            print('x won')
            return False
        elif board[1] == board[5] == board[9] == 'x':
            print('x won')
            return False
        elif board[3] == board[5] == board[7] == 'x':
            print('x won')
            return False
        else:
            return print('x not won')
        
    elif mark == 'o':
        if board[1] == board[2] == board[3] == 'o':
            print('o won')
            return False
        elif board[4] == board[5] == board[6] == 'o':
            print('o won')
            return False
        elif board[7] == board[8] == board[9] == 'o':
            print('o won')
            return False
        elif board[1] == board[4] == board[7] == 'o':
            print('o won')
            return False
        elif board[2] == board[5] == board[8] == 'o':
            print('o won')
            return False
        elif board[3] == board[6] == board[9] == 'o':
            print('o won')
            return False
        elif board[1] == board[5] == board[9] == 'o':
            print('o won')
            return False
        elif board[3] == board[5] == board[7] == 'o':
            print('o won')
            return False
        else:
            return print('o not won')
    
    else:
        return print('not the correct sign')
import random

def choose_first():
    x = random.randint(1,2)
    if x == 1:
        choose = 1
        return choose
    elif x == 2:
        choose = 2
        return choose
    else:
        pass
def space_check(board, position):
    position = int(position)
    if position in range(1,10):
        if board[position] == ' ':
            return True
        else:
            return False
    else:
        print('index out of range')
def full_board_check(board):
    for i in range (1,10):
        if board[i] != ' ':
            i += 1
        else:
            return True
    return False
def player_choice(board):
    position = int(input('enter your next position: '))
    c = space_check(board,position)
    if c is True:
        return int(position)
    elif c is False:
        return print('position is already filled')
    else:
        pass
def replay():
    replay1 = 'wrong'
    while replay1 not in ['yes','no']:
        replay1 = input('do you want to continue playing ? \n type yes to continue and no to quit ')
        if replay1 == 'yes':
            #t = True
            return True
        elif replay1 == 'no':
            #t = False
            return False
        else:
            print('please type in yes or no')
            
print('Welcome to Tic Tac Toe!')

while True:
    #from IPython.display import clear_output
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    import random
    # Set the game up here
    display_board(board)
    player_input()
    f = choose_first()
    #pass
    full_board_check(board)
    while not False:
        #Player 1 Turn
        if f == 1:
            print('x will go first')
            a = player_choice(board)
            place_marker(board, 'x',a)
            display_board(board)
            win = win_check(board,'x')
            if win is False:
                break
            else:
                pass
            full = full_board_check(board)
            if full is True:
                pass
            else:
                break
        
        # Player2's turn.
            a = player_choice(board)
            place_marker(board, 'o', a)
            display_board(board)
            win = win_check(board,'o')
            if win is False:
                break
            else:
                pass
            full = full_board_check(board)
            if full is True:
                pass
            else:
                break
        else:
            print('o will go first')
            #player2 will go first
            a = player_choice(board)
            place_marker(board, 'o', a)
            display_board(board)
            win = win_check(board,'o')
            if win is False:
                break
            else:
                pass
            full = full_board_check(board)
            if full is True:
                pass
            else:
                break
            
            #player1 then
            
            a = player_choice(board)
            place_marker(board, 'x',a)
            display_board(board)
            win = win_check(board,'x')
            if win is False:
                break
            else:
                pass
            full = full_board_check(board)
            if full is True:
                pass
            else:
                break
            
    win_check(board, 'x')
    win_check(board, 'o')
            #pass
    t = replay()
    if t is True:
        continue
    elif t is False:
        break
    else:
        pass
    #if not replay():
        #break
    

