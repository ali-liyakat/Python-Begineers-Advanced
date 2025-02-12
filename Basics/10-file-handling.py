# File Handling 

file = open("funny.txt", "r")
for line in file:
    print(line)

file.close()    


# Reading the file using with statement
with open("funny.txt", "r") as file:
    for line in file:
        print(line)

with open("funny.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)


# Writing to a file
with open("love.txt", "w") as file:
    file.write("I love ptyhon\n")
    file.write("I love machine learning\n")
    file.write("I love Rsearch\n")


# Appending to a file
with open("love.txt", "a") as file:
    file.write("I love to exercise\n")
    file.write("I love to play volleyball\n")
    file.write("I love swimming\n")



player_scores = {}
with open("scores.csv", "r") as file:
    for line in file:
        player, _, score = line.split(",")
        score = int(score.strip())
        if player in player_scores:
            player_scores[player].append(score)
        else:
            player_scores[player] = [score]

print(player_scores)

for player, score_list in player_scores.items():
    min_score = min(score_list)
    max_score = max(score_list)
    avg_score = sum(score_list) / len(score_list)
    print(f"{player} -> Min: {min_score}, Max: {max_score}, Avg: {avg_score}")


# Remove the file
import os
if os.path.exists("love.txt"):
    os.remove("love.txt")
else:
    print("The file does not exist") 

