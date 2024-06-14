##syntax is
# 'delimiter'.join(list_you_want_to_join)

my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(' '.join(my_munequita))
# => 'My Spanish Harlem Mona Lisa'
# We take the list of strings, my_munequita, and we joined it together with our delimiter, ' ', which is a space. 


reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)
##prints Black reapers with the sound of steel on stones

###
## CSV is comma separated values and common to join using this 
santana_songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']
santana_songs_csv = ','.join(santana_songs)
print(santana_songs_csv)
# => 'Oye Como Va,Smooth,Black Magic Woman,Samba Pa Ti,Maria Maria'

### can use escapesequence too 

smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio', 'You feel the turning of the world so soft and slow', 'Turning you \'round and \'round']

smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines) ##this means join via a new line 

print(smooth_fifth_verse)
## prints 
# Well I'm from the barrio
# You hear my rhythm on your radio
# You feel the turning of the world so soft and slow
# Turning you 'round and 'round

###

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)
##prints...
# All the complicated details
# of the attiring and
# the disattiring are completed!
# A liquid moon
# moves gently among
# the long branches.
# Thus having prepared their buds
# against a sure winter
# the wise trees
# stand sleeping in the cold.



