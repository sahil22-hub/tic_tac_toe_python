def sum(a, b, c ):
    return a + b + c

# def checkValidation(xState, zState):
#     for value in xState:
#         if(value == "X"):

    

def printBoard(xState, zState):
    displaying_value = []
    index = 0
    while index < 9:
        displaying_value.append('X' if xState[index] else ('O' if zState[index] else index))
        index += 1
    print(f"{displaying_value[0]} | {displaying_value[1]} | {displaying_value[2]} ")
    print(f"--|---|---")
    print(f"{displaying_value[3]} | {displaying_value[4]} | {displaying_value[5]} ")
    print(f"--|---|---")
    print(f"{displaying_value[6]} | {displaying_value[7]} | {displaying_value[8]} ") 

def checkWin(xState, zState, player_name):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print(f"  { player_name[0]} Won the match")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print(f"  {player_name[1]} Won the match")
            return 0
    return -1
    
if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    selectedState = []
    turn = 1   # 0 stands for 0's turn and 1 stands for X's turn to play
    print("Welcome to Tic Tac Toe")
    name1 = input("Enter player name for X: ")
    player_name = []
    player_name.append(name1)
    name2 = input("Enter player name for 0: ")
    player_name.append(name2)
    while(True):
        printBoard(xState, zState)
        if(turn == 1):
            print("%s's chance" %player_name[0])
            value = int(input("Please enter a value: "))
            if (value in selectedState): # Validation of incorrect value of already selected value
                print(" The value is already selected. Please select a valid one.")
                turn = 1 - turn
            elif(value > 8 or value < 0): # Validation for out of range value
                print(" Incorrect value. Valid range: 0-8")
                turn = 1 - turn
            else:
                xState[value] = 1
                selectedState.append(value)
        else:
            print("%s's chance" %player_name[1])
            value = int(input("Please enter a value: "))
            if (value in selectedState):
                print(" The value is already selected. Please select a valid one.")
                turn = 1
            elif(value > 8 or value < 0):
                print(" Incorrect value. Valid range: 0-8")
                turn = 1
            else:
                zState[value] = 1
                selectedState.append(value)
        cwin = checkWin(xState, zState, player_name)
        if(cwin != -1):
            printBoard(xState, zState)
            print("Match over")
            break
        
        turn = 1 - turn # Change the player's turn
    