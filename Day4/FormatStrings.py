# Python also provides a handy string method for including variables in strings. This method is .format().
# .format() takes variables as an argument and includes them in the string that it is run on. You include {} marks as placeholders for where those variables will be imported.

# Consider the following function:

def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)

print(favorite_song_statement("Smooth", "Santana"))
# => "My favorite song is Smooth by Santana."

####

def poem_title_card(title, poet): ##function defined taking two arguments 
  poem_desc = "The poem \"{}\" is written by {}.".format(title, poet) ##new variable which is equal to string inc formatting 
  return poem_desc##returns the variable result 

print(poem_title_card("I Hear America Singing","Walt Whitman"))
# prints The poem "I Hear America Singing" is written by Walt Whitman.

####
# By including keywords in the string, and in the arguments, you can remove that ambiguity. Let’s look at an example.

def favorite_song_statement(song, artist):
  return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

## can reverse too
def favorite_song_statement(song, artist):
  # this will have the same output as the above example
  return "My favorite song is {song} by {artist}.".format(artist=artist, song=song)

#####

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc



my_beard_description = poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends",)

print(my_beard_description)
## prints  The poem My Beard by Shel Silverstein was originally published in Where the Sidewalk Ends in 1974.