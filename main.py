

import pygame

import BoardObjects
from BoardObjects import Tile
from BoardObjects import Pawn
from BoardObjects import King
from BoardObjects import Queen
from BoardObjects import Knight
from BoardObjects import Rook
from BoardObjects import Bishop

#sets constants for colors and size of window
SHIRO = (255, 255, 255)
MIDORI = (0, 255, 0)
AOI = (0, 0, 255)
GUREE = (128,128,128)
#extra space for displaying turn
padding = 100
#actual side length of board
sideLength = 600
#size of tiles on the board
squareSize = int(sideLength / 8)

pygame.init()
#constants for text and images to be used
gameOver_font = pygame.font.Font('freesansbold.ttf', 32)
gameOverW_text = gameOver_font.render("GAME OVER. WHITE WON", True, (0, 0, 0) )
gameOverB_text = gameOver_font.render("GAME OVER. BLACK WON", True, (0, 0, 0) )
turn_textB = gameOver_font.render( " Black turn ", True, (0, 0, 0))
turn_textW = gameOver_font.render(" White turn", True, (0,0,0))
button_text = gameOver_font.render("Play again?", True, (0, 0,0))
pygame.display.set_caption("Chess game")
rookW = pygame.image.load("images/RookW.png")
rookB = pygame.image.load("images/RookB.png")
pawnB = pygame.image.load("images/PawnB.png")
pawnW = pygame.image.load("images/PawnW.png")
bishopB = pygame.image.load("images/BishopB.png")
bishopW = pygame.image.load("images/BishopW.png")
queenB = pygame.image.load("images/QueenB.png")
queenW = pygame.image.load("images/QueenW.png")
knightB = pygame.image.load("images/KnightB.png")
knightW = pygame.image.load("images/KnightW.png")
kingB = pygame.image.load("images/KingB.png")
kingW = pygame.image.load("images/KingW.png")
#board is going to be represented as a 2d array of tile objects
board = list()
#keeps track of all the pieces on the board
pieceList = list()

#used to find what object type to create during pawn promotion
findObject = {
    "rook" : Rook,
    "queen" : Queen,
    "bishop" : Bishop,
    "knight" : Knight





}
#used for pawn promotion in order to set the image, converts a string to an image name
findImage = {
    "rookW": rookW,
    "pawnW": pawnW,
    "bishopW": bishopW,
    "queenW": queenW,
    "kingW": kingW,
    "knightW": knightW,
    "rookB": rookB,
    "pawnB": pawnB,
    "bishopB": bishopB,
    "queenB": queenB,
    "kingB": kingB,
    "knightB": knightB



}

#method used to fill the board and set the starting positions of all the pieces
def startUp():
    #removes any existing objects
    board.clear()
    pieceList.clear()

    #creates a list of tile objects for each column in board, size of the tiles is scaled to the size of window using squareSize
    #therefore first index in board represents a column and second index represents a row

    for i in range(int((sideLength) / squareSize)):
        board.append(list())
        for j in range(int(sideLength / squareSize)):
            #determines if the tiles should be green or white based on the sum of its coordinates
            if ((i + j) % 2 == 0):
                board[i].append(Tile(i * squareSize, (j * squareSize), SHIRO))
            else:
                board[i].append(Tile(i * squareSize, (j * squareSize), MIDORI))

    '''creates objects for each piece type, with the position of the piece being scaled with the size of the squares, then places them on board
    on correcting starting coordinates. This process is repeated for each piece type '''

    pieceList.append(Rook('B', rookB, squareSize * 0.25, squareSize * 0.25))
    pieceList.append(Rook('B', rookB, 7.25 * squareSize, squareSize * 0.25))
    pieceList.append(Rook('W', rookW, squareSize * 0.25, 7.25 * squareSize))
    pieceList.append(Rook( 'W', rookW, 7.25 * squareSize, 7.25 * squareSize))


    board[0][0].piece = pieceList[0]
    board[7][0].piece = pieceList[1]
    board[0][7].piece = pieceList[2]
    board[7][7].piece = pieceList[3]

    pieceList.append(Knight('B', knightB, 1.25 * squareSize, squareSize * 0.25))
    pieceList.append(Knight('B', knightB, 6.25 * squareSize, squareSize * 0.25))
    pieceList.append(Knight('W', knightW, 1.25 * squareSize, 7.25 * squareSize))
    pieceList.append(Knight('W', knightW, 6.25 * squareSize, 7.25 * squareSize))
    board[1][0].piece = pieceList[4]
    board[6][0].piece = pieceList[5]
    board[1][7].piece = pieceList[6]
    board[6][7].piece = pieceList[7]

    pieceList.append(Bishop('B', bishopB, 2.25 * squareSize, squareSize * 0.25))
    pieceList.append(Bishop( 'B', bishopB, 5.25 * squareSize, squareSize * 0.25))
    pieceList.append(Bishop('W', bishopW, 2.25 * squareSize, 7.25 * squareSize))
    pieceList.append(Bishop('W', bishopW, 5.25 * squareSize, 7.25 * squareSize))
    board[2][0].piece = pieceList[8]
    board[5][0].piece = pieceList[9]
    board[2][7].piece = pieceList[10]
    board[5][7].piece = pieceList[11]

    pieceList.append(Queen('B', queenB, 3.25 * squareSize, squareSize * 0.25))
    pieceList.append(Queen('W', queenW, 3.25 * squareSize, 7.25 * squareSize))
    board[3][0].piece = pieceList[12]
    board[3][7].piece = pieceList[13]
    pieceList.append(King('B', kingB, 4.25 * squareSize, squareSize * 0.25))
    pieceList.append(King('W', kingW, 4.25 * squareSize, 7.25 * squareSize))
    board[4][0].piece = pieceList[14]
    board[4][7].piece = pieceList[15]

    currentCol = 0;

    for i in range(int(squareSize * 0.25), int(8.25 * squareSize), squareSize):
        pieceList.append(Pawn('B', pawnB, i, 1.25 * squareSize))
        pieceList.append(Pawn('W', pawnW, i, 6.25 * squareSize))
        board[currentCol][1].piece = pieceList[16 + currentCol * 2]
        board[currentCol][6].piece = pieceList[17 + currentCol * 2]
        currentCol += 1

#changes the color of the tiles to blue if the selected piece can move to that tile
def highlightTile(movable):
    for tile in movable:
        tile.color = AOI

#removes highlighting once piece is placed
def unHightLightTile(movable):
    for tile in movable:
        if ((tile.x / squareSize + tile.y / squareSize) % 2 == 0):
            tile.color = SHIRO
        else:
            tile.color = MIDORI








# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    screen = pygame.display.set_mode((sideLength, sideLength + padding))
    #represents whether or not a piece is being moved

    pieceDrag = False

    #represents selected piece to move
    pieceToDrag = None

    gameOver = False
    #if pawn promotion is happening or not
    pawnPromotion = False
    turn = 'W'

    startUp()
    #represents all the positions on the board the selected piece can move to
    canMove = list()
    running = True

    while running:
        for event in pygame.event.get():
            #quits the game
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            #handles clicking events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                if event.button == 1:
                    ''' this checks whether or not pieces on the board can be checked by checking if the board itself can be clicked
                    and that the game is still going
                    '''
                    if not gameOver and mouse_y < sideLength and not pawnPromotion:

                        #converts the coordinates clicked to indexes on the board

                        tileClicked = board[int(mouse_x // squareSize)][int(mouse_y // squareSize)]

                        #checks if a friendly piece has been pressed
                        if tileClicked.getSide() == turn:
                            #tags piece on selected tile as the piece to be moved
                            pieceToDrag = tileClicked.piece

                            #gets valid move list for selected piece
                            canMove = pieceToDrag.getMoves(int(tileClicked.x / squareSize),
                                                           int(tileClicked.y / squareSize), turn, board)
                            highlightTile(canMove)
                            pieceDrag = True

                            tileClicked.piece = None
                    #this handles when the mouse is pressed after the game is over

                    elif gameOver:
                        #checks whether coordinates pressed match replay button

                        if(mouse_y > sideLength):
                            #resets state

                            turn = 'W'
                            gameOver = False
                            startUp()

            #deals with events once mouse is released
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:

                    pieceDrag = False
                    #checks whether or not a piece was being moved
                    if pieceToDrag is not None:

                        #converts end coordinates of selected pieces to coordinates on list
                        tileFinal = board[int(pieceToDrag.x // squareSize)][int(pieceToDrag.y // squareSize)]
                        '''checks whether the final position is a valid position 
                        to move to by checking if its highlighted'''
                        if tileFinal.color == AOI:
                           #checks whether or not an enemy piece is at the final position
                            if tileFinal.getSide() != turn and tileFinal.getSide() != 0:
                                #if the enemy piece at the final position is the king, the game is over
                                if type(tileFinal.piece) == BoardObjects.King:

                                    gameOver = True
                                pieceList.remove(tileFinal.piece)
                            #deals with pawn promotion
                            if type(pieceToDrag) == BoardObjects.Pawn and not gameOver:
                                y = int(pieceToDrag.y // squareSize)

                                #checks whether the pawn made to the end of the board from its respective side
                                if (turn == 'W' and y == 0) or (turn == 'B' and y == 7):

                                    pawnPromotion = True
                                    #decides what to change the pawn to
                                    promotion = input(" type in the piece to promote this pawn to, use all lowercase: ")
                                    while (
                                            promotion != "queen" and promotion != "rook" and promotion != "knight" and promotion != "rook"):
                                        promotion = input(
                                            " type in the piece to promote this pawn to, use all lowercase: ")

                                    #deletes old pawn piece and replaces it with new object representing the piece it's promoted to
                                    pieceList.remove(pieceToDrag)
                                    image = findImage[promotion + turn]

                                    pieceToDrag = findObject[promotion](turn, image, tileFinal.x,
                                                                        tileFinal.y)
                                    pieceList.append(pieceToDrag)
                                    pawnPromotion = False
                            #sets the piece of the final position as the selected piece
                            tileFinal.piece = pieceToDrag

                            #adjusts the coordinates of the selected piece for display purposes
                            pieceToDrag.x = tileFinal.x + squareSize * 0.25
                            pieceToDrag.y = tileFinal.y + squareSize * 0.25
                            #deselects piece
                            pieceToDrag = None

                           #changes the turn
                            if turn == 'B':
                                turn = 'W'
                            else:
                                turn = 'B'
                        else:
                            #if an invalid final position is chosen, the selected piece is sent back to intial position and deselted
                            tileClicked.piece = pieceToDrag
                            pieceToDrag.x = tileClicked.x + squareSize * 0.25
                            pieceToDrag.y = tileClicked.y + squareSize * 0.25
                            pieceToDrag = None

                        unHightLightTile(canMove)


            elif event.type == pygame.MOUSEMOTION:
                '''if there is a piece selected, change its x and y coordinates to match that of the mouse.
                This is what creates the drag behaviour
                
                '''
                if pieceDrag:
                    mouse_x, mouse_y = event.pos
                    pieceToDrag.x = mouse_x
                    pieceToDrag.y = mouse_y




        #draws extra space at the bottom
        pygame.draw.rect(screen, GUREE, (0, sideLength, sideLength, padding))

        #draws board and pieces on the screen
        for row in board:
            for col in row:
                col.draw(screen, sideLength)

        for piece in pieceList:
            screen.blit(piece.image, (piece.x, piece.y))


        #if the game over, displays text displaying the winner and replay button
        if gameOver:

            pygame.draw.rect(screen, GUREE, (sideLength * 0.25, sideLength*0.35, sideLength*0.70, sideLength*0.15))
            screen.blit(button_text, (sideLength*0.3, sideLength+padding*0.3))

            if turn == 'B':
                screen.blit(gameOverW_text, (sideLength * 0.25, sideLength * 0.4))
            else:
                screen.blit(gameOverB_text, (sideLength * 0.25, sideLength * 0.4))

        #draws text representing who's turn it is if the game is not over
        else:
            if turn == 'W':
                screen.blit(turn_textW, (sideLength * 0.3, sideLength+padding/2))
            else:
                screen.blit(turn_textB,(sideLength*0.3, sideLength+padding/2))

        pygame.display.update()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
