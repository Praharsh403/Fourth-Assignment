try:
    """Task: Open and read a file 'sample.txt'.
    Print the content line by line and
    handle the errors gracefully."""

    with open("sample.txt", "rt") as fh:   #using with statement allows closing of file on its own.
        lin = 1                            #the lin(input) is giving the count of rows containing lines
        print("Reading the file content:")
        for linee in fh:                   #the for loop allows to print the content line by line as we do not know the amount of content inside.
            print(f"Line{lin}: {linee.strip()}")   #.strip() removes the extra or unnecessary spaces or \n
            lin += 1
except FileNotFoundError as error:         # Error name can also be used as Exception if unaware of its name or code
    print("Error: The file 'sample.txt' was not found")

"""The output prints the result line by line as per the availability of data inside the file.
   'try & except' along with 'for' loop allows the solve the given task."""