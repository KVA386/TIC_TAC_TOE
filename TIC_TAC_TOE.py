 #-------------Global variables--------

#Game board
board=["-","-","-",
       "-","-","-",
       "-","-","-"]
#if game is still going
game_still_going=True

#who won or tie???
winner=None

#Whos turn is it??
current_player="x"

def display_board():
    
    print(board[0]+"|" + board[1]+"|"+board[2]) 
    print(board[3]+"|" + board[4]+"|"+board[5]) 
    print(board[6]+"|" + board[7]+"|"+board[8])  
    
  
def play_game():
    # display initial board
     display_board()
     
     while game_still_going:
        #Handle a single turn of an arbitary player
        handle_turn(current_player)
        
        # check if game has ended
        check_if_game_over()
        
        
        
        #Flip to the other player
        flip_player()
        
     #The game has ended 
     if winner=="x" or winner=="o":
        print(winner +"\t Won!!")
        
     elif winner==None:
        print("Tie...")
        
def handle_turn(player):
           print(player+"'s turn.")
           
           position=input("Choose a position from 1 to 9: ")
           valid= False
           while not valid :
           
               while position not in ["1","2","3","4","5","6","7","8","9"] :
                  position=input("Choose a position from 1 to 9: ")
           
               position=int(position)-1
           
               if board[position] == "-" :
                  valid=True   
               else:
                  print("You cant go there.go again")
             
             
           board[position]=player
           
           
           display_board()
                

def check_if_game_over():
    check_for_winner()
    check_if_tie()
    
def check_for_winner():
    
    # set up a global variable 
    global winner
    
    #check rows
    row_winner=check_rows()
    
    #check columns
    column_winner=check_columns()
    
    #check diagonals
    diagonal_winner=check_diagonals()
    
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner: 
        winner=diagonal_winner
    else:
        winner=None
    
  

def check_rows():
    global game_still_going 
    
    row_1=board[0]==board[1]==board[2] !="-"
    row_2=board[3]==board[4]==board[5] !="-"
    row_3=board[6]==board[7]==board[8] !="-"
    
    # if any row does have a match , flag that there is win
    if row_1 or row_2 or row_3:
        game_still_going = False
        
    # return the winner ( X por O) 
    
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None
    

def check_columns():
    global game_still_going 
    
    col_1=board[0]==board[3]==board[6] !="-"
    col_2=board[1]==board[4]==board[7] !="-"
    col_3=board[2]==board[5]==board[8] !="-"
    
    # if any column does have a match , flag that there is win
    if col_1 or col_2 or col_3:
        game_still_going = False
        
    # return the winner ( X por O) 
    
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
       return None
   

def check_diagonals():
    global game_still_going 
    
    diagonal_1=board[0]==board[4]==board[8] !="-"
    diagonal_2=board[2]==board[4]==board[6] !="-"
    
    
    # if any diagonal does have a match , flag that there is win
    if diagonal_1 or diagonal_2 :
        game_still_going = False
        
    # return the winner ( X por O) 
    
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    # return none if there is no winner
    else:
        return None
    
def check_if_tie():
    global game_still_going 
    if "-" not in board:
        game_still_going=False
        return True
    else:
        return False
    
    
def flip_player():
    global current_player
    if current_player=="x":
        current_player="o"
    elif current_player=="o":
        current_player="x"
    

    
       
play_game()
