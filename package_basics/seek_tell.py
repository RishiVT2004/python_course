# Open a file in binary mode
file = open("file.txt", "r")

# Read 10 bytes from the file
data = file.read(20)
print("Data read:", data)

# Get the current file position
position = file.tell()
print("Current position:", position)

# Move the file pointer 5 bytes forward from the current position
file.seek(5)

# Get the new position
new_position = file.tell()
print("New position:", new_position)

# Close the file
file.close()
