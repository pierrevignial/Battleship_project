from os import system, name
import string

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

ALPHABET = list(string.ascii_uppercase)

number_of_rows = 10 #(max 26)
number_of_columns = 10
number_of_carriers = 1
number_of_battleships = 1
number_of_cruisers = 2
number_of_submarines = 1
number_of_patrol_boats = 3

boats = {}

def define_boats(number_of_patrol_boats, number_of_submarines, number_of_cruisers, number_of_battleships, number_of_carriers):
    boats["carriers"] = {"size" : 5, "number" : number_of_carriers}
    boats["battleships"] = {"size" : 4, "number" : number_of_battleships}
    boats["cruisers"] = {"size" : 3, "number" : number_of_cruisers}
    boats["submarines"] = {"size" : 3, "number" : number_of_submarines}
    boats["patrol_boats"] = {"size" : 3, "number" : number_of_patrol_boats}
    return boats

boats = define_boats(number_of_patrol_boats, number_of_submarines, number_of_cruisers, number_of_battleships, number_of_carriers)

carrier_size = 5
battleship_size = 4
cruiser_size = 3
submarine_size = 3
patrol_boat_size = 2

player_board = {}
computer_board = {}
player_radar = {}

def create_board(board, number_of_rows, number_of_columns):
    for i in range(number_of_rows):
        line = {}
        for n in range(number_of_columns):
            line[ALPHABET[n]] = []
        board[i + 1] = line
    return board

def display(board):
    clear()
    for row in board.keys():
        line_display = []
        for column in board[row].keys():
            line_display.append(board[row][column])
        print(line_display)



def datadisplay(board):
    df = pd.DataFrame(data=board)
    print(df)

player_board = create_board(player_board, number_of_rows, number_of_columns)
computer_board = create_board(computer_board, number_of_rows, number_of_columns)
computer_board = create_board(player_radar, number_of_rows, number_of_columns)


print(boats)

print(player_board)

display(player_radar)
print("----------------------------------------------------------------------------")
display(player_board)


print(player_board[1]["A"])
