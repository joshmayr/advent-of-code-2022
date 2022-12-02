
# TODO: Split the lines into games
# TODO: Check if we win, lose, or draw
# TODO: Get the points from the shape we play

input = open("input.txt", "r").read()

lines = input.splitlines()

num_wins = 0
num_draws = 0
num_rock = 0
num_paper = 0
num_scissors = 0

user_move_dict = {
    "X": 0,
    "Y": 0,
    "Z": 0
}

user_outcome_dict = {
    "win": 0,
    "lose": 0,
    "draw": 0
}

part_two_outcome = {
    'X': 0,
    'Y': 0,
    'Z': 0
}

part_two_move_score = 0

def get_user_move(move):
    user_move_dict[move] += ord(move) - ord('X') + 1

def get_user_outcome(opp, user):
    opp_int = ord(opp)
    user_int = ord(user)
    outcome = user_int - opp_int
    if outcome == 23:
        user_outcome_dict["draw"] += 1
    elif outcome == 22 or outcome == 25:
        user_outcome_dict["lose"] += 1
    elif outcome == 21 or outcome == 24:
        user_outcome_dict['win'] += 1
    else:
        print("ERROR")
        print("USER MOVE: " + user + " OPP MOVE: " + opp)
        print("OUTCOME: " + str(outcome))


def get_part_two_outcome(outcome):
    part_two_outcome[outcome] += (ord(outcome) - ord('X')) * 3

def get_part_two_move(opp_move, outcome):
    difference = {
        "X": 2,
        "Y": 0,
        "Z": 1
    }
    int_opp_move = ord(opp_move) - ord('A')
    int_opp_move += difference[outcome]
    int_opp_move = int_opp_move % 3
    int_opp_move += 1
    global part_two_move_score
    part_two_move_score += int_opp_move
    if int_opp_move not in [1,2,3]:
        print("ERROR: " + str(int_opp_move))

def part_one():
    for line in lines:
        game = line.split(" ")
        opponent_move = game[0]
        user_move = game[1]
        get_user_move(user_move)
        get_user_outcome(opponent_move, user_move)

    final_score = 0
    for key in user_move_dict:
        final_score += user_move_dict[key]
    final_score += 3 * user_outcome_dict["draw"]
    final_score += 6 * user_outcome_dict['win']

    print(final_score)

def part_two():
    for line in lines:
        game = line.split(" ")
        opp_move = game[0]
        outcome = game[1]
        get_part_two_outcome(outcome)
        get_part_two_move(opp_move, outcome)
    final_score = part_two_move_score
    
    for key in part_two_outcome:
        final_score += part_two_outcome[key]
    print(final_score)

part_two()
