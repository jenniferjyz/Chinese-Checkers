grid = [[-9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9,  1, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9],
       [-9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9,  1, -9,  1, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9],
       [-9, -9, -9, -9, -9, -9, -9, -9, -9, -9,  1, -9,  1, -9,  1, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9],
       [-9, -9, -9, -9, -9, -9, -9, -9, -9,  1, -9,  1, -9,  1, -9,  1, -9, -9, -9, -9, -9, -9, -9, -9, -9],
       [ 0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0],
       [-9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9],
       [-9, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9, -9],
       [-9, -9, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9, -9, -9],
       [-9, -9, -9, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9, -9, -9, -9],
       [-9, -9, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9, -9, -9],
       [-9, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9, -9],
       [-9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9],
       [ 0 , -9, 0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0, -9,  0],
       [-9, -9, -9, -9, -9, -9, -9, -9, -9,  2, -9,  2, -9,  2, -9,  2, -9, -9, -9, -9, -9, -9, -9, -9, -9],
       [-9, -9, -9, -9, -9, -9, -9, -9, -9, -9,  2, -9,  2, -9,  2, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9],
       [-9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9,  2, -9,  2, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9],
       [-9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9,  2, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9]]


class player_move:
    def __init__(self, p, t):
        self.p = p
        self.win = False
        self.turn = t

    def availableMove(self, r, c):
        available = []
        player_move.checkHop(grid, r, c, available, 0, 0)
        return available

    def checkHop(self, r, c, available, i, dirc):
        # base case: if out of range or not available move
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] < 0:
            return
        print(r, ", ", c, " ", grid[r][c])
        # add available move to array than return
        if grid[r][c] == 0:
            print(r, ", ", c, " ")
            available.append([r, c])
            print(available)
            return

        if i % 2 != 0 and i > 0:
            if dirc == 0:
                player_move.checkHop(grid, r - 1, c - 1, available, i + 1, 0)
            if dirc == 1:
                player_move.checkHop(grid, r - 1, c + 1, available, i + 1, 1)
            if dirc == 2:
                player_move.checkHop(grid, r + 1, c + 1, available, i + 1, 2)
            if dirc == 3:
                player_move.checkHop(grid, r + 1, c - 1, available, i + 1, 3)
            if dirc == 4:
                player_move.checkHop(grid, r, c + 2, available, i + 1, 4)
            if dirc == 5:
                player_move.checkHop(grid, r, c - 2, available, i + 1, 5)

        # check for available spots
        if grid[r][c] > 0 and i > 1 or i == 0:
            # left down diagonal

            player_move.checkHop(grid, r - 1, c - 1, available, i + 1, 0)
            # left up diagonal
            player_move.checkHop(grid, r - 1, c + 1, available, i + 1, 1)
            # right up diagonal
            player_move.checkHop(grid, r + 1, c + 1, available, i + 1, 2)
            # right down diagonal
            player_move.checkHop(grid, r + 1, c - 1, available, i + 1, 3)
            # right
            player_move.checkHop(grid, r, c + 2, available, i + 1, 4)
            # left
            player_move.checkHop(grid, r, c - 2, available, i + 1, 5)
        return

        


def board():
  global ava
  for i in range(len(grid)):#rows
      for j in range(len(grid[0])): #columns
       # rect(200,50,600,600)
        if grid[i][j] >= 0: #rest of board
            fill(169,169,169)
            if grid[i][j] == 1: #red pieces
                fill(255,0,0)
            elif grid[i][j] == 2: #blue pieces
                fill(69,169,169)
            #rect(200+24*j, 50+35*i, 30, 30) #draw the rectangles, position at 200 + 24 columns, position at 50 with 35 rows
            if [i,j] in ava:
                fill(255,165,0)
            ellipse(215+24*j, 65+35*i, 30, 30)
            
mode = 0
ava = []
player1 = player_move(1, True)
player2 = player_move(2, False)

def setup():
    global player1, player2
    size(1000,700)
    background(255, 217, 130)
    

def draw():
  global mode, grid, board, ava, r, c
#Main screen--------------------------------------------------------------------------------------------------------
  if mode == 0:
    # text
    background(255, 217, 130)

    textSize(40)
    fill(14, 24, 160)
    text("Chinese Checkers",330,250)

    # click here to play box
    fill(219, 209, 127,127)
    stroke(0)
    rect(350,360,300,100)
    #instructions box
    rect(350,500,300,100)
    #text
    fill(0)
    textSize(28)
    text("Click here to play",378,420)
    text("Instructions",415,557)
    fill(255)

#Game Screen-----------------------------------------------------------------------------------------------------
  if mode == 1:
    background(255, 217, 130)
    
    print("fdsf")
    clicked = False
    while not player1.win and not player2.win:
        if player1.turn:
            if not clicked and r>-1 and c>-1 and grid[r][c] == player1.p:
                clicked = True
                ava = player1.checkAvailable(r,c)
                grid[r][c] = 0
            if clicked and r>-1 and c>-1 and [r,c] in ava:
                grid[r][c] = 1
                ava = []
    
        if player2.turn:
            if not clicked and r>-1 and c>-1 and grid[r][c] == player2.p:
                clicked = True
                ava = player2.checkAvailable(r,c)
                grid[r][c] = 0
            if clicked and r>-1 and c>-1 and [r,c] in ava:
                grid[r][c] = 2
                ava = []

    board() #display board
    
    fill(0)
    textSize(14)
    text("Number of Player 1 Moves:",20,20)
    fill(255)
    rect(20,40,50,50) #box for number
    rect(20,630,50,50) #player 2 box
    fill(254, 255, 206)
    rect(850,20,100,50) #go back home box
    fill(0)
    text("Number of Player 2 Moves:",20,610)
    text("Home", 880, 50)
    
#Instructions-----------------------------------------------------------------------------------------------------
  if mode == 2:
    background(255, 217, 130)
    textSize(16)
    fill(0)   
    text("You can move one step in any direction", 60, 400)
    text("or jump over other checkers.", 80, 415)
    text("A single move can consist of multiple hops",55,430)
    text("each piece hopped must be directly adjacent",55,445)
    text("and hops can be in any direction",60,460)
    text("Your goal is to place all your pieces",550,400)
    text("in the opposite star corner before your opponent",495,415)
    rect(850,20,100,50)
    fill(254, 255, 206) 
    rect(850,20,100,50) #go back home box
    fill(0)
    text("Home", 880, 50)
#-----------------------------------------------------------------------------------------------------    
r = -1
c = -1
def boardPress(mx, my):
    if mx >=200 and mx<800 and my >= 50 and my <= 650:
        x = mx-200
        y = my-50
    
        r = -1
        c = -1
    
        for i in range(len(grid)):
            if y >= 30*i + 5*i and y <= 30 + 30*i + 5*i:
                r = i
    
        for i in range(len(grid[0])):
            if r%2 == 0:
                if x >= 30*i + 18*i and x <= 30 + 30*i + 18*i:
                    c=i        
            else:
                if x >= 18 + 30*i + 18*i and x <= 48 + 30*i + 18*i:
                    c=i 
        #print("error fucker")
    
def mousePressed():
  global mode,r,c, boardPress

  if mode == 0: #main screen
      # for the start box
      if 720 > mouseX and mouseX > 350 and 460 > mouseY and mouseY > 360:
          mode = 1

      # instructions box
      if 720 > mouseX and mouseX> 350 and 600 > mouseY and mouseY > 500:
          mode = 2
       #clear screen when on game screen
 
  if mode == 1: #game screen (850,20,100,50)
      
      print("fdsf")
      clicked = False
      while not player1.win and not player2.win:
          if player1.turn:
              boardPress(mouseX, mouseY)
              if not clicked and r>-1 and c>-1 and grid[r][c] == player1.p:
                  clicked = True
                  ava = player1.checkAvailable(r,c)
                  grid[r][c] = 0
              if clicked and r>-1 and c>-1 and [r,c] in ava:
                  grid[r][c] = 1
                  ava = []
    
          if player2.turn:
              if not clicked and r>-1 and c>-1 and grid[r][c] == player2.p:
                  clicked = True
                  ava = player2.checkAvailable(r,c)
                  grid[r][c] = 0
              if clicked and r>-1 and c>-1 and [r,c] in ava:
                  grid[r][c] = 2
                  ava = []
                  
      
            
          
      #print(mouseX-200, mouseY-50)
      
      if 950 > mouseX and mouseX > 850 and 70 > mouseY and mouseY > 20:
          mode = 0
  
  if mode ==2:
      if 950 > mouseX and mouseX > 850 and 70 > mouseY and mouseY > 20:
          mode = 0
