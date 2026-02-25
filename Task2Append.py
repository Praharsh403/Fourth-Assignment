with open("output.txt","wt") as fh:
    """Task2: Write and Append the text into file name 'Output.txt'.
     Read and display the content later."""
    First_text = input("Enter text to write to your file: ")   #Takes input for text to write in the file.
    fh.write(First_text)
    fh.write("\n")                                             # makes sure that if any new text added, it starts from new line.
    print("Data successfully written to output.txt.")
with open("output.txt","at") as fh:                             # reopen file as data needs to be appended.
    Second_text = input("Enter additional text to append: ")    # Takes input for the appended data to be added
    fh.write(Second_text)
    fh.write("\n")
    print("Data successfully appended.")

print("\nFinal content of output.txt file is:")
with open("output.txt","rt") as fh:
    load = fh.read()
    print(load)

"""The final data shows the content inside the file 'output.txt' with the input entered."""