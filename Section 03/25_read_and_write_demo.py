## Reading from and writing to files
# We learned the basics of using context managers to read data
# from a file, make sure to have the data.txt file in the same
# directory as this file, otherwise you have to provide the full
# path to the file
filename = 'data.txt'
with open(filename) as f:
    for line in f:
        print(line.strip())

# We then looked at how to append a new line to the file
record_to_add = "jane,doe:c,ruby,javascript"
with open(filename, "a+") as to_write:
    to_write.write(record_to_add+"\n")
