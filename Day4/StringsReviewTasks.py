highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems) ##prints list as it is

highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list) #prints listed separated by commas

highlighted_poems_stripped = [] ##new empty list 
for line in highlighted_poems_list: #for loop, iterates through poems list
  highlighted_poems_stripped.append(line.strip()) #new list created, all info added without whilte space
print(highlighted_poems_stripped)

highlighted_poems_details = [] ##empty list
for chars in highlighted_poems_stripped: ##for loop, iterates through poems
  highlighted_poems_details.append(chars.split(":")) ##new list has all ifno added but with data split around :
print(highlighted_poems_details) ##prints new list
titles = [] ## 3 new lists created 
poets = []
dates = []
for details in highlighted_poems_details: ##for loop iterates through poems 
  titles.append(details[0]) ##adds title to title, poet to poet list and dates to date list, using same index in each list
  poets.append(details[1])
  dates.append(details[2])

print(titles)##prints lists of titles etc 
print(poets)
print(dates)

for i in range(0,len(highlighted_poems_details)):  #new for loop, runs full length of lists
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i])) #prints string which includes each title, poet and date 
    
    ###final product
# The poem Ecstasy was published by Gabriela Mistral in 1925
# The poem Georgia Dusk was published by Jean Toomer in 1923
# The poem Parting Before Daybreak was published by An Qi in 2014
# The poem The Untold Want was published by Walt Whitman in 1871
# The poem Mr. Grumpledump's Song was published by Shel Silverstein in 2004
# The poem Angel Sound Mexico City was published by Carmen Boullosa in 2013
# The poem In Love was published by Kamala Suraiyya in 1965
# The poem Dream Variations was published by Langston Hughes in 1994
# The poem Dreamwood was published by Adrienne Rich in 1987

