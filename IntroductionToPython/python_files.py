# Write 10 lines to the file. If file does not exist, create it
print("Write 10 lines to the file. If file does not exist, create it")
file2 = open("python_files.txt", "w+")
for i in range(10):
    file2.write("The line is %d\r\n" % (i + 1))
file2.close()



# Read from the file after checking its mode.
print("\n\nRead from the file after checking its mode.")
file2 = open("python_files.txt", "r")
if file2.mode == "r":
    contents = file2.read()
    print(contents)
file2.close()



# Read the first line from the file after checking its mode.
print("\n\nRead the 1st line from the file after checking its mode.")
file1 = open("python_files.txt", "r")
if file1.mode == "r":
    contents = file1.readline()
    print(contents)
file1.close()



# Append a new line
print("\n\nAppend a new line")
file1 = open("python_files.txt", "a")
file1.write("This is a new appended line")
file1.close()
# Print file's contents
file1 = open("python_files.txt", "r")
if file1.mode == "r":
    contents = file1.read()
    print(contents)
file1.close()