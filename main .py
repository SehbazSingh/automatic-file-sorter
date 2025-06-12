import os
import shutil

# Input and normalize path
path = input("Enter the path of the folder: ").replace('\\', '/')
if not path.endswith('/'):
    path += '/'

# File type to folder mapping
file_mappings = {
    'images': ['.jpg', '.jpeg', '.png'],
    'excel_files': ['.xls', '.xlsx'],
    'python_files': ['.py'],
    'pdfs': ['.pdf'],
    'word_files': ['.doc', '.docx'],
    'videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'text_files': ['.txt', '.md'],
    'archives': ['.zip', '.rar', '.7z', '.tar.gz'],
    'executables': ['.exe', '.bat', '.sh'],
    'web_files': ['.html', '.css', '.js']
}

# Create folders if they don't exist
for folder in file_mappings:
    os.makedirs(os.path.join(path, folder), exist_ok=True)

# Move files into respective folders
for file in os.listdir(path):
    full_path = os.path.join(path, file)
    if os.path.isfile(full_path):
        moved = False
        for folder, extensions in file_mappings.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                shutil.move(full_path, os.path.join(path, folder, file))
                moved = True
                break
        if not moved:
            print(f"File '{file}' does not match any category.")
