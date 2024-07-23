table = []
game ={}
# 'X' - vertikalno 1. igra
# 'O' - horizontalno 2. igra
def createTable(m,n):
    for i in range(m):
        list = []
        for j in range(n):
            list.append(None)
        table.append(list)


def firstPlayer():
    pomocna = input("Ako prvi igra racunar unesite 1 , ako igra covek unesite 0 \n") 
    if(int(pomocna)==0):
        return 0
    elif(int(pomocna)==1):
        return 1
    else:
        print("Uneli ste navildnu opciju")

def makeTableRow(rowNum,n):
    for i in range(0,n+n-1+4):
        if(i==0 or i== n+n-1+4-1):
            el = rowNum
            if(i==n+n-1+4-1):
                print(el)
            else:
                print(el,end='')
        elif(i==1 or i==n+n-1+4-2):
            el='|'
            print(el,end='')
        elif(i%2==0):
            if(table[rowNum][(i-2)//2]==None):
                el=''
            else:
                el=table[rowNum][(i-2)//2]
            print(el,end='')
        else:
            el ='|'
            print(el,end='')
def makeHorizontalTableNumeration(n):
    for i in range(0,n+n-1+4):
        if(i==0 or i==1 or i== n+n-1+4-1 or i== n+n-1+4-2):
            el = ' '
            if(i==n+n-1+4-1):
                print(el)
            else:
                print(el,end='')
        elif(i%2==0):
            el =(int) (i-2)//2
            print(el,end='')
        else:
            el = ' '
            print(el,end='')
def printTable(m,n):
    makeHorizontalTableNumeration(n)
    for i in range(0,m):
        makeTableRow(i,n)
    makeHorizontalTableNumeration(n)

def inputDimensions():
    m = input("Unesite broj vrsta: ")
    n = input("Unesite broj klolona: ")
    game['rows'] = int(m)
    game['columns'] = int(n) 
    createTable(int(m),int(n))
    printTable(int(m),int(n))

def isValidX(move):
   return True if move[0]>=0 and move[0]<=game['rows']-2 and move[1]>=0 and move[1]<=game['columns']-1 and table[move[0]][move[1]]==None and table[move[0]+1][move[1]]==None else False
def isValidO(move):
   return True if move[0]>=0 and move[0]<=game['rows']-1 and move[1]>=0 and move[1]<=game['columns']-2 and table[move[0]][move[1]]==None and table[move[0]][move[1]+1]==None else False
def makeMove(player,move): # ovo je valjda za 2. fazu 
    #if(player == 'X'):
    if(player==0):
        if(isValidX(move)):
            table[move[0]][move[1]] = 'X'
            table[move[0]+1][move[1]] = 'X'
            print("Igrac X odigrava potez %d , %d" % (move[0],move[1]))
            printTable(game['rows'],game['columns'])
            return True
        else:
            print("Igrac X ne moze odigrati ovaj potez")
            printTable(game['rows'],game['columns'])
            return False

    else:
        if(isValidO(move)):
            table[move[0]][move[1]] = 'O'
            table[move[0]][move[1]+1] = 'O'
            print("Igrac O odigrava potez %d , %d" % (move[0],move[1]))
            printTable(game['rows'],game['columns'])
            return True
        else:
            print("Igrac O ne moze dodigrati ovaj potez")
            printTable(game['rows'],game['columns'])
            return False

    
def inputMove():
    x = int(input('Unesite X koordinatu zeljenog poreza : '))
    y = int(input('Unesite Y koordinatu zeljenog poteza : '))
    potez = (x,y)
    return potez

def endGame(player):
    #if player=="X":
    if player==0:
        for i in range(0,game['rows']-1):
            for j in range(0,game['columns']):
                if(table[i][j]==None and table[i+1][j]==None):
                    return False
        game['winner']="O"
    else:
        for i in range(0,game['rows']):
            for j in range(0,game['columns']-1):
                if(table[i][j]==None and table[i][j+1]==None):
                    return False
        game['winner']="X"
    return True

def startGame():
    inputDimensions()
    game['racunarPrvi']=(int)(firstPlayer())
    game['currentPlayer']=0
    end=False
    while(not end):
        if(game['currentPlayer']==0):
            print("Igra X")
        else:
            print("Igra O")
        move=inputMove()
        if(makeMove(game['currentPlayer'],move)):
            game['currentPlayer']=game['currentPlayer']^1
            end=endGame(game['currentPlayer'])


    print("Igra je zavrsena. Pobednik je igrac: "+game['winner'])
         
startGame()
