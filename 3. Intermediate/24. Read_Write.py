# Read the current file
content = open(__file__).read()

# Print the content of the file in console
print(content)

# Create a new file with .txt 
new_file = open(__file__ + ".txt", "w")

# Write this content to the file
new_file.write("The last line of the file.")

# Close the file, so it can be used by another task or process
new_file.close()
