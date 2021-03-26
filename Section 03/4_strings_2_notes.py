# We can use string concatenation and add strings
# together
message = "Welcome to the course"
name = "Mashrur"
print(message + name)

# We can add an empty space in there too
print(message + " " + name)

# Strings are sequences of characters which are indexed
# We can index into a string by using square bracket notation
movie_name = "Interstellar"
print(movie_name[0]) # This will print 'I' which is at index 0
print(movie_name[1]) # This will print 'n' which is at index 1
print(movie_name[11]) # This will print 'r' which is the last character
print(movie_name[-1]) # This will print 'r', last character
print(movie_name[-2]) # This will print 'a', second to last character

# We can use slicing to select portions of the string
print(movie_name[0:5]) # This will print 'Inter'
print(movie_name[:5])   # We can leave the starting 0 out if we start at
                        # at the beginning to get 'Inter' as well
print(movie_name[5:]) # This will print 'stellar', begin index to end
print(movie_name[:]) # This will print "Interstellar", begin to end
print(movie_name[5:9]) # This will print 'stel'

# You can specify step size as optional third argument
print(movie_name[5:9:2]) # This will print 'se', moving forward by
                        # 2 steps instead of the default 1
print(movie_name[::2]) # This will print "Itrtla"
print(movie_name[::-1]) # This will reverse the string and print
                        # 'ralletsretnI'
