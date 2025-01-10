import os

# Define list of directories, target text, and replacement text
directories = ['./generic', './mood']
search_text = "24cbb461c2ff6556f047dd4bc1275b4b08d52eb8"
replace_text = "1f54c6e4b0afc2f0cad65ab1da9b7c73730d06b9"

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