# Define the filename and open the file
filename = "C:\Users\ADMIN\Downloads\Voters Data\Voters Data\216-21.txt"
with open(filename, "r") as file:

    # Initialize a list to store the data
    data = []

    # Process each line in the file
    for line in file:
        # If the line is not empty, extract the relevant data
        if line.strip():
            # Extract the EPIC No., Name, and Relative (based on your provided format)
            # Add the extracted data to the data list
            data.append([line[line.find("EPIC No. ") + len("EPIC No. "):line.find(" Name ")-1],
                         line[line.find(" Name ") + len(" Name "):line.find(" Relative ")-1],
                         line[line.find(" Relative ") + len(" Relative "):].strip()])

# Create a pandas DataFrame from the data list
df = pd.DataFrame(data, columns=["EPIC No.", "Name", "Relative"])

# Save the DataFrame to an Excel file
df.to_excel("output.xlsx", index=False)