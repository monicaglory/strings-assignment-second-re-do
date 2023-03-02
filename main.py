# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
first_scorer="Ruud Gullit"
second_scorer="Marco Van Basten"
print(first_scorer)

goal_0=32
goal_1=54

scorers=first_scorer + " " +(str(goal_0))+','+second_scorer + " " +(str(goal_1))
print(scorers)

report=f'{first_scorer} scored in the {goal_0}nd minute \n {second_scorer} scored in the {goal_1}th minute'
print(report)

player='Jan Wouters'
first_Index=player.find('Jan')
print(first_Index)
last_Index=player.find(' ')
print(last_Index)
first_name=player[first_Index:last_Index]
print(first_name)

first_index_last_name=player.find('Wouters')
last_index_last_name=player.find('JanWouters')
last_name=player[first_index_last_name:last_index_last_name]
print(last_name)
last_name_len=len(last_name)

name_short=player[0]+'.'+ ' '+player[4:12]
print(name_short)

chant= (first_name + '!')*len(first_name)
print(chant)

good_chant=chant[:12]!=" "
print(good_chant)