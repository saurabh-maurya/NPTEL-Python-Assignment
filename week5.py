input_list = []
while True:
    input_str = input()
    if input_str == "":
        break
    else:
        input_list.append(input_str)

namescores = {}
for line in input_list:
    line_split = line.split(':')
    name1 = line_split[0]
    name2 = line_split[1]
    namescores[name1] = {}
    namescores[name2] = {}
    namescores[name1]['3set_game_won'] = 0
    namescores[name1]['5set_game_won'] = 0
    namescores[name2]['3set_game_won'] = 0
    namescores[name2]['5set_game_won'] = 0
    namescores[name1]['set_won'] = 0
    namescores[name1]['set_lost'] = 0
    namescores[name2]['set_won'] = 0
    namescores[name2]['set_lost'] = 0
    namescores[name1]['game_won'] = 0
    namescores[name1]['game_lost'] = 0
    namescores[name2]['game_won'] = 0
    namescores[name2]['game_lost'] = 0

for line in input_list:
    line_split = line.split(':')
    name1 = line_split[0]
    name2 = line_split[1]
    scores = line_split[2]
    score_pairs = scores.split(',')
    name1_3set_won = 0
    name1_5set_won = 0
    name2_3set_won = 0
    name2_5set_won = 0
    
    for score_pair in score_pairs:
        
        score_pair_split = score_pair.split('-')
        namescores[name1]['game_won'] = int(namescores[name1]['game_won'])+int(score_pair_split[0])
        namescores[name1]['game_lost'] = int(namescores[name1]['game_lost'])+int(score_pair_split[1])
        namescores[name2]['game_won'] = int(namescores[name2]['game_won'])+int(score_pair_split[1])
        namescores[name2]['game_lost'] = int(namescores[name2]['game_lost'])+int(score_pair_split[0])

        if (len(score_pairs)>3 and len(score_pairs)<=5 and (int(score_pair_split[0]) >=6 or int(score_pair_split[1]) >=6)):
                    
                    if int(score_pair_split[0])>int(score_pair_split[1]):
                        namescores[name1]['set_won'] = int(namescores[name1]['set_won'])+1
                        namescores[name2]['set_lost'] = int(namescores[name2]['set_lost'])+1
                        name1_5set_won += 1
                        
                    elif int(score_pair_split[0])<int(score_pair_split[1]):
                        namescores[name1]['set_lost'] = int(namescores[name1]['set_lost'])+1
                        namescores[name2]['set_won'] = int(namescores[name2]['set_won'])+1
                        name2_5set_won += 1
                        
        elif (len(score_pairs)<=3 and (int(score_pair_split[0]) >=6 or int(score_pair_split[1]) >=6)):

                    if int(score_pair_split[0])>int(score_pair_split[1]):
                        namescores[name1]['set_won'] = int(namescores[name1]['set_won'])+1
                        namescores[name2]['set_lost'] = int(namescores[name2]['set_lost'])+1
                        name1_3set_won += 1
                        
                    elif int(score_pair_split[0])<int(score_pair_split[1]):
                        namescores[name1]['set_lost'] = int(namescores[name1]['set_lost'])+1
                        namescores[name2]['set_won'] = int(namescores[name2]['set_won'])+1
                        name2_3set_won += 1

    if (name1_5set_won >=(name2_5set_won + 1)):
        namescores[name1]['5set_game_won'] = int(namescores[name1]['5set_game_won'])+1
        
    elif (name2_5set_won >=(name1_5set_won + 1)):
        namescores[name2]['5set_game_won'] = int(namescores[name2]['5set_game_won'])+1

    elif (name1_3set_won >=(name2_3set_won + 1)):
        namescores[name1]['3set_game_won'] = int(namescores[name1]['3set_game_won'])+1
        
    elif (name2_3set_won >=(name1_3set_won + 1)):
        namescores[name2]['3set_game_won'] = int(namescores[name2]['3set_game_won'])+1


final_list = [[] for name in namescores]
i=0
for player in namescores:
    final_list[i].append(player)
    final_list[i].append(namescores[player]['5set_game_won'])
    final_list[i].append(namescores[player]['3set_game_won'])
    final_list[i].append(namescores[player]['set_won'])
    final_list[i].append(namescores[player]['game_won'])
    final_list[i].append(namescores[player]['set_lost'])
    final_list[i].append(namescores[player]['game_lost'])
    i += 1

final_list.sort(key=lambda x: (x[1],x[2],x[3],x[4],x[6],x[5]))
final_list=final_list[::-1]


for i in range (len(final_list)):
               print(final_list[i][0], end =" ")
               print(final_list[i][1], end =" ")
               print(final_list[i][2], end =" ")
               print(final_list[i][3], end =" ")
               print(final_list[i][4], end =" ")
               print(final_list[i][5], end =" ")
               print(final_list[i][6], end ="\n")
