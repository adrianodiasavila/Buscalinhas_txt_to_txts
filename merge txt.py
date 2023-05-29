import os

# Specify the directory containing the .txt files
directory = r"C:\Users\Adriano\Desktop"

# Specify the name of the new file to which contents will be written
output_file = "merged_file.txt"

# Open the output file in write mode
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        # Only consider .txt files
        if filename.endswith('.txt'):
            # Open each .txt file in read mode
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as infile:
                # Read the contents of the .txt file and write to the output file
                outfile.write(infile.read())
            # Optionally, write a newline character to separate contents of different files
            outfile.write("\n")