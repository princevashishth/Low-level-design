class Player:
  def __init__(self,name):
    self.userName=name


class Grid:
  def __init__(self, board_size):
    self.board_size=board_size
    self.grid=[[0 for x in range(board_size)] for y in range(board_size)]

  def printGrid(self):
    for y in range(len(self.grid)):
      for x in range(len(self.grid[y])):
        print(self.grid[y][x],end=" ")
      print("")

  def isValid(self):
    for y in range(len(self.grid)):
      for x in range(len(self.grid[y])):
        if(self.grid[y][x]==0):
          return True
    return False


  def validMove(self,y,x):
    return (y>=0 and y<=self.board_size) and (x>=0 and x<=self.board_size) and self.grid[y][x]==0

  def setValue(self,y,x,val):
    self.grid[y][x]=val


  def solve(self):
    # Horizontal Check
    for y in range(len(self.grid)):
      state=self.grid[y][0]
      flag=True
      if(state==0):
        continue
      for x in range(1,len(self.grid[y])):
        if(self.grid[y][x]!=state):
          flag=False
          break
      if(flag):
        return True

    # Vertical Check
    for x in range(len(self.grid[0])):
      state=self.grid[0][x]
      flag=True
      if(state==0):
        continue
      for y in range(1,len(self.grid)):  
        if(self.grid[y][x]!=state):
          flag=False
          break
      if(flag):
          return True

    # Diagonal Check
    diagonal_match = True
    for i in range(self.board_size-1):
        if(self.grid[i][i]!=0 and self.grid[i+1][i+1]==self.grid[i][i]):
            continue
        else:
            diagonal_match=False
    if(diagonal_match):
        return True
    diagonal_match = True
    for i in range(self.board_size-1):
        if(self.grid[i][self.board_size-i-1]!=0 and self.grid[i+1][self.board_size-i-2]==self.grid[i][self.board_size-i-1]):
            continue
        else:
            diagonal_match=False
    if(diagonal_match):
        return True

    # No One Won
    return False


class Game:
  def __init__(self,user1,user2,board_size):
    self.player1=user1
    self.player2=user2
    self.choice=True
    self.grid=Grid(board_size)

  def gameInstance(self):
    self.grid.printGrid()

  def play(self):
    if(not self.grid.isValid()):
      print("MATCH DRAW")
      return

    if(self.choice):
      print("Player 1: "+self.player1.userName+" Move")
      y1,x1=map(int,input().split())
      y1-=1
      x1-=1
      if(self.grid.validMove(y1,x1)):
        self.grid.setValue(y1,x1,1)
        self.gameInstance()
        if(self.grid.solve()):
          print("Player 1: "+self.player1.userName+" Won the Match")
          return
        self.choice=False
        self.play()
      else:
        print("Invalid Move...Try A Valid Move Instead")
        self.play()

    else:
      print("Player 2: "+self.player2.userName+" Move")
      y2,x2=map(int,input().split())
      y2-=1
      x2-=1
      if(self.grid.validMove(y2,x2)):
        self.grid.setValue(y2,x2,2)
        self.gameInstance()
        if(self.grid.solve()):
          print("Player 2: "+self.player2.userName+" Won the Match")
          return
        self.choice=True
        self.play()
      else:
        print("Invalid Move...Try A Valid Move Instead")
        self.play()

board_size = int(input("Enter size of board : "))
player1=Player(input("Enter first player's name : "))
player2=Player(input("Enter second player's name : "))
newGame=Game(player1,player2,board_size)
newGame.gameInstance()
newGame.play()
