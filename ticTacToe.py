theBoard = {'top-L': '','top-M': '', 'top-R': '',
            'mid-L': '','mid-M': '', 'mid-R': '',
            'low-L': '','low-M': '', 'low-R': ''}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-+')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-+')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('-+-+-+')


#Because you created a data structure to represent
#a tic-tac-toe board and wrote code in printBoard() to interpret that data structure,
#you now have a program that 'models' the tic-tac-toe board.

# code that allows the players to enter their movies.

turn = 'X'
for i in range (9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'    

printBoard(theBoard)
