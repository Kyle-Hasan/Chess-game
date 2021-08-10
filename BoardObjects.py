import pygame


class Tile:
    def __init__(self, x, y, color):
        self.piece = None
        self.x = x
        self.y = y

        self.color = color

    def draw(self, surface, sideLength):
        #draws a rectangle on the board, size is scaled using sideLength of board
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, sideLength / 8, sideLength / 8))

    def getSide(self):
        #returns 0 if there is no occupying piece on the tile, otherwise returns side of occupying piece
        if self.piece is None:
            return 0
        else:
            return self.piece.side

#parent class for all the other piece classes, defines the constructor for all of the piece classes
class Piece:
    def __init__(self, side, image, x, y):

        self.side = side
        self.image = image
        self.x = x
        self.y = y


class Rook(Piece):
    #x and y args represent the position of the piece

    def getMoves(self, x, y, turn, board):
        #the movable list contains all the valid positions on the board the piece can move to
        movable = list()
        '''directions stores a list of row and column indexes for each direction the rook can move in.
        The stored lists are generated using list comprehension and contain tuples representing the row and column indexes of each tile in that
        direction (first index of tuple is row, second one is column'''
        directions = [[(i, y) for i in range(x + 1, 8)], [(x, i) for i in range(y + 1, 8)],
                      [(i, y) for i in range(x - 1, -1, -1)],
                      [(x, i) for i in range(y - 1, -1, -1)]]
        #loops over every direction
        for direction in directions:
            '''loops over every square on the board in that direction (represented by having row of square in first index of tuple
            and column of square in second index of tuple)
            
            '''
            for square in direction:
                #checks what is occupying the square
                occupied = board[square[0]][square[1]].getSide()
                '''if nothing is occupying the square, it is valid to move there, 
                 therefore that position is added to movable'''
                if (occupied == 0):
                    movable.append(board[square[0]][square[1]])

                #if an enemy is occupying the square, it is valid to move there,
                #but it is longer possible to move further in that direction, so the loop is broken
                #in order to stop iterating over it

                elif(occupied != turn):
                    movable.append(board[square[0]][square[1]])
                    break
                #if a friendly piece is occupying the square, it is invalid to move there and
                #it is no longer possible to move further in this direction, so the loop is broken to
                # prevent further iteration over the direction

                else:
                    break

        return movable

#x and y args represent the position of the piece

class Bishop(Piece):

    # x and y args represent the position of the piece

    def getMoves(self, x, y, turn, board):
        # the movable list contains all the valid positions on the board the piece can move to
        movable = list()

        #calculates how far it can move in each diagonal direction based on current position of piece
        down = 7 - y
        right = 7 - x

        lowerRight = min(down, right)
        lowerLeft = min(down, x)
        upperRight = min(y, right)
        upperLeft = min(y, x)

        '''directions stores a list of row and column indexes for each direction the rook can move in.
               The stored lists are generated using list comprehension and contain tuples representing the row and column indexes of each tile in that
               direction (first index of tuple is col, second one is row'''
        directions = [[(x + i, y + i) for i in range(1, lowerRight + 1)],
                      [(x + i, y - i) for i in range(1, upperRight + 1)],
                      [(x - i, y - i) for i in range(1, upperLeft + 1)],
                      [(x - i, y + i) for i in range(1, lowerLeft + 1)]]

        # loops over every direction
        for direction in directions:
            for square in direction:
                '''loops over every square on the board in that direction (represented by having column of square in first index of tuple
                            and row of square in second index of tuple)

                            '''
                occupied = board[square[0]][square[1]].getSide()
                '''if nothing is occupying the square, it is valid to move there, 
                                 therefore that position is added to movable'''
                if (occupied == 0):
                    movable.append(board[square[0]][square[1]])

                # if an enemy is occupying the square, it is valid to move there,
                # but it is longer possible to move further in that direction, so the loop is broken
                # in order to stop iterating over it

                elif (occupied != turn):
                    movable.append(board[square[0]][square[1]])
                    break

                # if a friendly piece is occupying the square, it is invalid to move there and
                # it is no longer possible to move further in this direction, so the loop is broken to
                # prevent further iteration over the direction

                else:
                    break

        return movable


class Pawn(Piece):

    def getMoves(self, x, y, turn, board):
        #movable contains all the valid positions the piece can move to
        movable = list()

        if turn == 'B':
            #if a black pawn is at row 7, then it has reached the end of board
            if y == 7:
                return movable
            #if a black pawn is at row 1, it is making it's first move and can therefore move 2 squares forward
            elif y == 1:
                for i in range(2, 4):
                    #checks whether both squares are valid to move to by
                    # checking if they are empty before adding them to movable
                    if (board[x][i].piece is None):
                        movable.append(board[x][i])

            #moving the pawn forward after it's first move

            else:
                #checks whether the the square forward is empty before adding it to movable

                if (board[x][y + 1].piece is None):
                    movable.append(board[x][y + 1])

            #checks whether the pawn can move in the lower right direction to capture an empty piece

            if (x < 7):

                #if the lower right square contains a white piece, the position of that square is added to movable

                if (board[x + 1][y + 1].getSide() == 'W'):
                    movable.append(board[x + 1][y + 1])

            # checks whether the pawn can move in the lower left direction to capture an empty piece

            if (x > 0):

                # if the lower left square contains a white piece, the position of that square is added to movable

                if (board[x - 1][y + 1].getSide() == 'W'):
                    movable.append(board[x - 1][y + 1])


        else:
            # if a white pawn is at row 0, then it has reached the end of board
            if y == 0:
                return movable
            #if a white pawn is at row 6, it is making it's first move and therefore move 2 squares forward
            elif y == 6:
                # checks whether both squares are valid to move to by
                # checking if they are empty before adding them to movable
                for i in range(5, 3, -1):
                    if (board[x][i].piece is None):
                        movable.append(board[x][i])
            else:

                # checks whether the the square forward is empty before adding it to movable

                if (board[x][y - 1].piece is None):
                    movable.append(board[x][y - 1])

            # checks whether the pawn can move in the upper right direction to capture an empty piece

            if (x < 7):
                # if the upper right square contains a black piece, the position of that square is added to movable

                if (board[x + 1][y - 1].getSide() == 'B'):
                    movable.append(board[x + 1][y - 1])

            # checks whether the pawn can move in the upper left direction to capture an empty piece

            if (x > 0):

                # if the upper left square contains a black piece, the position of that square is added to movable

                if (board[x - 1][y - 1].getSide() == 'B'):
                    movable.append(board[x - 1][y - 1])

        return movable


class Queen(Piece):
    '''the moves a queen can make are the combined moves of a rook and bishop, therefore the getMoves method
    for the queen piece is essentially determining all the valid moves a rook in the position can make, all the valid moves
    a bishop in that direction can make and combining the two into a list

    '''
    def getMoves(self, x, y, turn, board):

        movable = list()
        directions = [[(i, y) for i in range(x + 1, 8)], [(x, i) for i in range(y + 1, 8)],
                        [(i, y) for i in range(x - 1, -1, -1)],
                        [(x, i) for i in range(y - 1, -1, -1)]]

        for direction in directions:
            for square in direction:
                occupied = board[square[0]][square[1]].getSide()
                if (occupied == 0):
                    movable.append(board[square[0]][square[1]])
                elif (occupied != turn):
                    movable.append(board[square[0]][square[1]])
                    break
                else:
                    break

        down = 7 - y
        right = 7 - x

        lowerRight = min(down, right)
        lowerLeft = min(down, x)
        upperRight = min(y, right)
        upperLeft = min(y, x)

        directions = [[(x + i, y + i) for i in range(1, lowerRight + 1)],
                        [(x + i, y - i) for i in range(1, upperRight + 1)],
                        [(x - i, y - i) for i in range(1, upperLeft + 1)],
                        [(x - i, y + i) for i in range(1, lowerLeft + 1)]]

        for direction in directions:
            for square in direction:
                occupied = board[square[0]][square[1]].getSide()
                if (occupied == 0):
                    movable.append(board[square[0]][square[1]])
                elif (occupied != turn):
                    movable.append(board[square[0]][square[1]])
                    break
                else:
                    break

        return movable


class Knight(Piece):

    def getMoves(self, x, y, turn, board):
        # movable contains all the valid positions the piece can move to
        movable = list()

        #here i represents and offset to the column of the current position of the piece.

        for i in range(-2, 3):
            #makes sures the column index doesnt go off the board
            if x + i < 0:
                continue
            elif x + i > 7:
                break

            # here j represents and offset to the row of the current position of the piece.

            for j in range(-2, 3):
                #makes sure row index doesn't go off the board.
                #the absolute values of both offsets to the the row and col indexes of the knight must add up to 3 for
                # a valid move
                if y + j < 0 or abs(i) + abs(j) != 3:
                    continue
                elif y + j > 7:
                    break

                #makes sure friendly piece is not occupying position before adding it to movable

                if (board[x + i][y + j].getSide() != turn):
                    movable.append(board[x + i][y + j])
        return movable


class King(Piece):

    def getMoves(self, x, y, turn, board):
        # movable contains all the valid positions the piece can move to
        movable = list()

        #checks how many squares from the ends of the board in every direction based on current position of king

        down = 7 - y
        right = 7 - x

        upperRight = min(y, right)
        upperLeft = min(y, x)
        lowerRight = min(down, right)
        lowerLeft = min(down, x)

        '''for each direction, it is first determined whether there is at least 1 square in that direction.
        Then it is determined whether or not the closest square in that direction has a friendly piece on it, if not,
        that square is valid to move to and it's position is added to movable'''

        # down

        if down > 0:
            if (board[x][y + 1].getSide() != turn):
                movable.append(board[x][y + 1])
        # up
        if y > 0:
            if (board[x][y - 1].getSide() != turn):
                movable.append(board[x][y - 1])
        # upperRight
        if upperRight > 0:
            if (board[x + 1][y - 1].getSide() != turn):
                movable.append(board[x + 1][y - 1])
        # upperLeft

        if upperLeft > 0:
            if (board[x - 1][y - 1].getSide() != turn):
                movable.append(board[x - 1][y - 1])
        # lowerLeft
        if lowerLeft > 0:
            if (board[x - 1][y + 1].getSide() != turn):
                movable.append(board[x - 1][y + 1])

        # lowerRight
        if lowerRight > 0:
            if (board[x + 1][y + 1].getSide() != turn):
                movable.append(board[x + 1][y + 1])

        if right > 0:
            if (board[x + 1][y].getSide() != turn):
                movable.append(board[x + 1][y])
        # left
        if x > 0:
            if (board[x - 1][y].getSide() != turn):
                movable.append(board[x - 1][y])

        return movable
