import os

# Define list of directories, target text, and replacement text
directories = ["b2aiprotocol/generic/q_generic_demographics"]
search_text = "b2ai_redcap2rs_activities:"
replace_text = "b2ai_redcap2rs_activities:q_generic_demographics/items/"

# Iterate over each directory in the list
for directory in directories:
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if ".DS_Store" not in file_path and ".jpeg" not in file_path:
                # Open the file and replace text
                print(file_path)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = content.replace(search_text, replace_text)
                # Write updated content back to file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

print("Find and replace completed in all directories.")