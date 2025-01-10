import os

# Define list of directories, target text, and replacement text
directories = ["/Users/isaacbevers/sensein/reproschema-wrapper/b2ai-redcap2rs"]
search_text = "NaN"
replace_text = "\"NaN\""

# Iterate over each directory in the list
for directory in directories:
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            suffixes = [".DS_Store", ".jpeg", "index", ".pack", ".idx"]
            if not file_path.endswith(tuple(suffixes)):
                # Open the file and replace text
                print(file_path)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = content.replace(search_text, replace_text)
                # Write updated content back to file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

print("Find and replace completed in all directories.")