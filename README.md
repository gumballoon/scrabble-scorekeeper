# scrabble-scorekeeper
**Disclaimer**
This project is a significant milestone in my journey of learning Python, as it was the first project where I truly invested myself. I completed it in March 2024, with just two months of learning under my belt. As a beginner project, there are many things I would do differently today with the knowledge and experience I've gained since then. I appreciate any feedback or suggestions for improvement!

**Overview**
Welcome to the SCRABBLE SCOREKEEPER, developed by Francisco Cristina (https://github.com/gumballoon).
This program is designed to help you keep track of scores, manage player profiles, and award special prizes in a game of Scrabble. Whether you're playing a casual game with friends or hosting a Scrabble tournament, this tool makes scorekeeping easy and fun.

**Features**
	•	Score Calculation: Calculate the standard score of any word and add extra points for double/triple letters or words.
	•	Player Management: Add new players or update scores for existing players.
	•	Batch Insert: Quickly add multiple words for a player and calculate their total score.
	•	Letter Scores: View the standard point value for each letter in Scrabble.
	•	Player Ranking: Display a ranked list of players based on their total scores.
	•	Special Prizes: Award special prizes for creativity, efficiency, and luck.

**Installation**
To run the SCRABBLE SCOREKEEPER, you need Python installed on your system. Download the script and run it in your preferred Python environment.

**Usage**
Run the script and follow the on-screen instructions to navigate through the menu and use the different features.

**Main Menu Options**
[W] One Word Score: Calculate the score for a single word and add it to a player's profile.
[B] Batch Insert Per Player: Add multiple words for a player at once and calculate the total score.
[C] Check Letters' Score: View the standard score of each letter.
[R] Ranking of Players: Display the current ranking of players based on their total scores.
[P] Scrabble Special Prizes: Award special prizes for the most creative, efficient, and lucky players.

**Functions and Their Descriptions**
tester(user, options)
Validates the user's input against a list of options.
score(word)
Calculates the standard score of any word based on letter values.
score_extra(word, result)
Calculates extra points for a word (double/triple letters, double/triple words).
one_word()
Calculates the score for a single word, allows adding the score to a player's profile.
batch_insert()
Allows the user to add multiple words for a player and calculates their total score.
check_letters()
Displays the point value for each letter in Scrabble.
ranking_players()
Displays a ranked list of players based on their total scores.
prize_creative()
Awards the player who used the largest variety of different letters.
prize_efficient()
Awards the player who achieved the most points per letter.
prize_lucky()
Awards the player who scored the most extra points.
special_prizes()
Calls all the prize functions to determine and display the special prizes.
menu()
Displays the main instructions and allows the user to choose the next action.

**Example Usage**
	1	Calculate One Word Score: Select [W] One Word Score, enter the word, assign extra points if needed, and choose to add the score to a player's profile.
	2	Batch Insert: Select [B] Batch Insert Per Player, enter the player's name, input the words, and assign extra points if needed.
	3	Check Letters' Score: Select [C] Check Letters' Score to view the points for each letter.
	4	Ranking of Players: Select [R] Ranking of Players to see the current player rankings.
	5	Scrabble Special Prizes: Select [P] Scrabble Special Prizes to award special prizes based on various criteria.

**Contact**
For more information or to report any issues, please contact Francisco Cristina at https://github.com/gumballoon
