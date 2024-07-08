"""Welcome to the SCRABBLE SCOREKEEPER, a project by Francisco Cristina (https://github.com/gumballoon).
This tool simplifies score keeping, player management, and awarding special prizes in Scrabble games.
For detailed instructions and information, please refer to the README file."""

# DEFAULT DATA
points = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3,
          'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

players = {"Carlos": 99, "John": 102, "Kelly": 72}

players_words = {"Carlos": ["ball", "window", "eraser", "dog", "cat", "youth", "haste", "jeans", "table", "finger", "plant"],
                 "John": ["headphones", "head", "grace", "printer", "monitor", "desk", "heater"],
                 "Kelly": ["wardrobe", "bed", "painting", "whiskey"]}


# GENERIC FUNCTIONS
def tester(user, options):
    if user.upper() in options:
        return True
    else:
        print("\nThat's not a valid option. Please try again.")
# tester: validates the user's answer

def score(word):
    letters = list(word.upper())    # list w/ all the letters as individual elements
    result = 0
    for letter in letters:
        if letter in points:
            result += points[letter]  # adds up each letter's points to the end result
        else:
            print("\nOnly characters from the English alphabet are accepted. Please try again.")
            break
    return result
# score: calculates the standard score of any word

def score_extra(word, result):
    while True:
        print("""
To assign extra points, select one of the options below. You'll be able to repeat this step.
[D] Double Letter
[T] Triple Letter
[2] Double Word
[3] Triple Word
[S] Skip to Score""")
        user_extra = input("...").upper()
        if tester(user_extra, ["D", "T", "2", "3", "S"]):
            if user_extra in ["D", "T"]:  # double/triple letter
                letter = input("\nWhich letter?").upper()
                if tester(letter, list(word)):
                    if user_extra == "D":
                        result += points[letter]  # adds up the points of the letter to the result
                        print(f"\nNice one! That special '{letter}' equals {points[letter]} extra point(s).")
                    elif user_extra == "T":
                        result += points[letter] * 2  # adds up twice the points of the letter to the result
                        print(f"\nWay to go! That special '{letter}' equals {points[letter] * 2} extra points.")
            elif user_extra in ["2", "3"]:
                result *= int(user_extra)  # multiplies the result by 2 or 3
                print(f"\nAMAZING! Extra trouble incoming for your opponent.")
            elif user_extra == "S":
                break
    return result
# score_extra: calculates the extra score (double/triple letter, double/triple word)


# GAME FUNCTIONS
def one_word():
    word = input("\nWhat's your word?...").upper()
    result = score(word)
    final_result = score_extra(word, result)
    user_final = ""
    while user_final != "S":
        user_final = input(f"""\nThe final score of '{word.lower()}' is {final_result}. To add this word to a player's overall score, choose one of the options below.
[R] Registered Player
[N] New Player
[S] Skip to Menu
...""").upper()
        if tester(user_final, ['R', 'N', 'S']):
            if user_final == "N":
                user_name = input("\nWhat's the name of the player?\n...").title()
                if user_name not in players:
                    players[user_name] = final_result
                    players_words[user_name] = [word.lower()]
                    print(f"\nWelcome aboard, {user_name}! Your current overall score is {final_result}.\n")
                    break
                else:  # if the user enters the name of a registered player
                    print(f"\nThat name is already registered. Please try again.")  # tester
            elif user_final == "R":
                user_name = input("\nWhat's the name of the player?\n...").title()
                if user_name in players:
                    players[user_name] += final_result
                    players_words[user_name].append(word.lower())
                    print(f"\nWelcome back, {user_name}! Your current overall score is {players[user_name]}.\n")
                    break
                else:  # if the user enters a non-registered name
                    print(f"\nThere is no player registered under that name. Please try again.")  # tester
# one_word: allows the user to calculate the total score of any word, also allowing him to add that word to a player's profile

def batch_insert():
    user_name = input("\nWhat's the name of the player?\n...").title()
    if user_name not in players:
        players[user_name] = 0
        players_words[user_name] = []
        user_batch = input(f"\nWelcome aboard, {user_name}! Let's start by adding your words. Make sure you separate them with spaces.\n...").lower()
    else:  # if the name is already registered
        user_batch = input(f"\nWelcome back, {user_name}! Please write the news words below. Make sure you separate them with spaces.\n...").lower()
    word_list = user_batch.split(" ")  # list w/ all the separate words
    players_words[user_name].append(word_list)     # adds the new words to the players' word list
    user_words = {word: score(word) for word in word_list}  # separates the words of the string into a new dict and calculates each word score

    # extra points
    user_index = ""
    while user_index != "S":    # while the user doesn't hit "Skip to Menu"
        print("\nYour words have been registered. To assign extra points, choose which word(s) you need to review. Just like before, use spaces in case you insert more than one option.")
        index = 0  # index will be used to have an input associated with each word, as it's the same index
        index_list = ["S"]  # list of possible answers
        for word in user_words:
            print(f"[{index}] {word}")  # prints each word with an associated index, so the user can quickly choose
            index_list.append(str(index))  # stores all the indexes that are created in a string format to compare with the user's answer (tester)
            index += 1  # keeps changing the index to make it unique from word to word
        print("[S] Skip to Menu")
        user_index = input("...").upper()
        index_list = user_index.split(" ")  # separates the options into separate elements of a new list
        for i in index_list:  # to assign extra points to the standard scores
            if tester(i, index_list):
                result_extra = 0  # all extra points will be added to this variable
                i_word = word_list[int(i)].lower()  # variable to simplify the identification of each word
                user_extra = ""
                while user_extra != "S":
                    user_extra = input(f"""\nTo assign extra points to '{i_word}', select one of the options below. You'll be able to repeat this step.
[D] Double Letter
[T] Triple Letter
[2] Double Word
[3] Triple Word
[S] Skip
...""").upper()
                    if tester(user_extra, ["D", "T", "2", "3", "S"]):
                        if user_extra in ["D", "T"]:  # double/triple letter
                            letter = input("\nWhich letter?").upper()
                            if tester(letter, list(i_word.upper())):
                                if user_extra == "D":
                                    result_extra += points[letter]  # adds up the points of the letter to the result
                                    print(f"\nNice one! That special '{letter}' equals {points[letter]} extra point(s).")
                                elif user_extra == "T":
                                    result_extra += points[letter] * 2  # adds up twice the points of the letter to the result
                                    print(f"\nWay to go! That special '{letter}' equals {points[letter] * 2} extra points.")
                        elif user_extra in ["2", "3"]:
                            result_extra *= int(user_extra)  # multiplies the result by 2 or 3
                            print(f"\nAMAZING! Extra trouble incoming for your opponent.")
                        elif user_extra == "S":  # if the user skips, the loop continues to the next index (word)
                            continue
                user_words[i_word] += result_extra  # ends the process by adding the total extra points to the previously calculated score
        break
    players[user_name] = sum(user_words.values())
# batch_insert: allows the user to quickly calculate the total score of various words and associate them with a player's profile

def check_letters():
    print("\nPOINTS PER LETTER")
    for letter in points:
        print(f"{letter}: {points[letter]} | ", end="")
    print("\n")
# check_letters: shows the standard score of each letter

def ranking_players():
    print("\nPLAYERS RANKING")
    rank_players = dict(sorted(players.items(), key=lambda k: k[1], reverse=True))
    # dicts are sets (the elements order can't be manipulated), so the only way to sort them is by creating a new dict)
    for p in rank_players:
        print(f"{p}: {rank_players[p]}")
    print(" ")
# ranking_players: shows the current ranking of players (based on their total score)

def prize_creative():
    letters_used = {p: 0 for p in players}
    for player in players_words:
        letters = []
        for word in players_words[player]:
            for letter in word:
                letters.append(letter)
        letters_used[player] = len(set(letters))
    winner = max(letters_used, key=lambda x: letters_used[x])
    return print(f"\n** Most Creative **\n{winner} WINS after using 20 different letters. Wow!")
# prize_creative: awards the user who uses the largest variety of letters

def prize_efficient():
    letters_number = {p: 0 for p in players}
    for player in players_words:
        for word in players_words[player]:
            letters_number[player] += len(set(word))
    ratio_letters = {p: players[p] / letters_number[p] for p in players}
    winner = max(ratio_letters, key=lambda x: ratio_letters[x])
    return print(f"** Most Efficient **\n{winner} WINS after achieving the most amount of points ({round(ratio_letters[winner], 2)}) per letter. Damn!")
# prize_efficient: awards the user who achieves the most amount of points per letter

def prize_lucky():
    standard_score = {p: 0 for p in players}
    for player in players_words:
        for word in players_words[player]:
            standard_score[player] += score(word)
    extra_score = {p: players[p] - standard_score[p] for p in players}
    winner = max(extra_score, key=lambda x: extra_score[x])
    return print(f"** Lucky Strike **\n{winner} WINS after collecting the larger amount of extra points: {extra_score[winner]}. Congrats!")
# prize_lucky: awards the user who scores the larger amount of extra points

def special_prizes():
    prize_creative()
    prize_efficient()
    prize_lucky()
# special_prizes: puts all the prizes functions together

# MAIN MENU
def menu():
    print("""
SCRABBLE SCOREKEEPER
[W] One Word Score\n[B] Batch Insert Per Player (Various Words)
[C] Check Letters' Score\n[R] Ranking of Players\n[P] Scrabble Special Prizes""")     # menu options
    user_act = input("...").upper()
    if tester(user_act, actions):
        actions[user_act]()
# menu: main instructions and first user input to choose the next action
actions = {"W": one_word, "B": batch_insert, "C": check_letters, "R": ranking_players, "P": special_prizes}
# to allow the user to quickly call any of the main functions

while True:
    menu()
# keeps the game running nonstop
