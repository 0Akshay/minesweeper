##minefield = [[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
import random

VISIBLE_SAFE = 0
HIDDEN_SAFE = 1
HIDDEN_MINE = 2


minefield= []  #creates minefield
for x in range(1,9):
    row = []
    for y in range(1,9):
        row.append(HIDDEN_SAFE)
    minefield.append(row)

def print_debug_minefield():
            
    for x in minefield: #prints minefield

        for y in x:
            print(y, end='   ')

        print('\n', end='\n')




num_of_mines = int(input('Please enter the number of mines: ')) #Takes the input for number of mines



def manualfill(): #YOU get to fill the mines yourself
    print('\nPlease enter the positions of mines in format: <row number[0,7]><space><column number[0,7]>\n')


    for i in range(0,num_of_mines):


        print("Enter position of mine ",i+1,": ",sep = '', end='')
        x = input()
        a = int(x[0])
        b = int(x[2])
        
        while(minefield[a][b] == HIDDEN_MINE):
            print("mine already exists at that position")
            print("Enter position of mine ",i+1,": ",sep = '', end='')
            x = input()
            a = int(x[0])
            b = int(x[2])
            
        minefield[a][b] = HIDDEN_MINE

def autofill(): #Computer does it for you but UNSTABLE. Also, unecessary.

    for i in range(0,num_of_mines):

        a = random.randrange(0,8)
        b = random.randrange(0,8)

        while(minefield[a][b] == HIDDEN_MINE):

            a = random.randrange(0,8)
            b = random.randrange(0,8)

        minefield[a][b] = HIDDEN_MINE

c = int(input("How would you like to fill the mines\n\nEnter 1 for Manualfill\nEnter 2 for Autofill: "))
if(c==1):
    manualfill()
elif(c==2):
    autofill()

print('\nGame started\n')

print_debug_minefield()


def detect_row(r_row_num): #Returns no of mines in a row

    mine_count = 0
    row = minefield[r_row_num]

    for i in row:
        if(i == HIDDEN_MINE):
            mine_count = mine_count+1

    return mine_count

def detect_column(r_column_num): #Returns the number of minesin given column

    mine_count = 0
    for i in minefield:
        if(i[r_column_num] == HIDDEN_MINE):
            mine_count = mine_count + 1

    return mine_count
            
def detect_square(row, column, side): #Returns the no of mines in the given description of a square

    term_number = int(((side - 3)/2)+1)

    square_star_row = row - term_number
    square_start_column = column - term_number
    square = []

    for x in range(square_star_row, square_star_row+side):
        square_row = []
        for y in range(square_start_column, square_start_column + side):

            if((x>=0 and x<=7)and(y>=0 and y<=7)):
                square_row.append(minefield[x][y])

        square.append(square_row)
        
    mine_count = 0
    for i in square:
        for j in i:
            if(j == HIDDEN_MINE):
                mine_count = mine_count+1
    
    return mine_count

    
while(True):    #Program main command flow
    command = input('')
    
    q = int(command[0])
    
    if (q == 1):
        row_num = int(command[2])
        x = detect_row(row_num)
        print('\nThere are ',x,' mine(s) in row ',row_num,'\n',sep = '')

    elif(q == 2):
        col_num = int(command[2])
        x = detect_column(col_num)
        print('\nThere are ',x,' mine(s) in column ',col_num,'\n',sep = '')

    elif(q == 3):
        row_of_square = int(command[2])
        column_of_square = int(command[4])
        side_of_square = int(command[6])
        
        x = detect_square(row_of_square, column_of_square, side_of_square)
        print('\nThere are ',x,' mine(s) in the square centered at row ',row_of_square,' column ',column_of_square,' of size ',side_of_square,'\n',sep = '')

        


