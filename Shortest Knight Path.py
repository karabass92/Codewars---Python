'''
Given two different positions on a chess board, find the least number of moves it would take a knight to get from one to the other. The positions will be passed as two arguments in algebraic notation. For example, knight("a3", "b5") should return 1.

The knight is not allowed to move off the board. The board is 8x8.

For information on knight moves, see https://en.wikipedia.org/wiki/Knight_%28chess%29

For information on algebraic notation, see https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29

(Warning: many of the tests were generated randomly. If any do not work, the test cases will return the input, output, and expected output; please post them.)
'''

def knight(p1, p2):
    board = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    start_pos = list(p1)
    x1 = board.index(start_pos[0])
    y1 = int(start_pos[1])
    
    end_pos = list(p2)
    x2 = board.index(end_pos[0])
    y2 = int(end_pos[1])

    return max(abs(x1-x2), abs(y1-y2))