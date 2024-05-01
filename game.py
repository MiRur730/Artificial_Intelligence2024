board = [' ' for x in range(10)]
def printBoard(board):
    print('... |... |... ')
    print('.' + board[1] + '.|.' + board[2] + '.|.' + board[3])
    print('... |... |... ')
    print('------------')
    print('... |... |... ')
    print('. ' + board[4] + ' .| .' + board[5] + ' .| .' + board[6])
    print('... |... |... ')
    print('------------')
    print('... |... |... ')
    print(' .' + board[7] + ' .|. ' + board[8] + ' .|. ' + board[9])
    print('... |... |... ')

# all winning moves   one at all the places 
def IsWinner(b,l):
 return (b[1]== l and b[2]==l and b[3]==l) or (b[4]== l and b[5]==l and b[6]==l) or \
 (b[7]== l and b[8]==l and b[9]==l) or \
 (b[1]== l and b[4]==l and b[7]==l) or (b[3]== l and b[6]==l and b[9]==l) or \
 (b[2]== l and b[5]==l and b[8]==l) or \
 (b[1]== l and b[5]==l and b[9]==l) or (b[3]== l and b[5]==l and b[7]==l)


#returning true is like below blank otherwise false
def spaceIsFree(pos):
  return board[pos]==' '





#inserting the value at that position  letter x or 0 
# pos enetered by the user
def insertLetter(letter,pos):
  board[pos]=letter

def playerMove(symbol):
  run = True
  while run:
        # here symbol is coming either X or 0
        move = input("please select a position to enter the {sym} between 1 to 9".format(sym=symbol))
        try:
            move = int(move)
            if move > 0 and move < 10:
                print(f"The space free shows {spaceIsFree(move)}")
                if spaceIsFree(move):
                    run = False
                    # so this stops and next time runs only when it is called externally
                    insertLetter(symbol , move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')
        except:
            print('Please type a number')

def main():
    """Main game loop."""
    print("Welcome to Tic-Tac-Toe!")
    player1 = 'X'
    player2 = 'O'
    turn = player1

    while True:
        printBoard(board)

        if turn == player1:
            # called function from player 1 side and that symbol of player 1
            playerMove(player1)
            if IsWinner(board, player1):
                printBoard(board)
                print("Congratulations! Player 1 wins!")
                break
            # otherwise second turn
            turn = player2
            # it goes to second else runnin for player 2
        else:
            playerMove(player2)
            if IsWinner(board, player2):
                printBoard(board)
                print("Congratulations! Player 2 wins!")
                break
            turn = player1

        if ' ' not in board:
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()