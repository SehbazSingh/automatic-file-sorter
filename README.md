# 🗂️ File Organizer Script

A Python script that automatically organizes files in a specified folder into categorized subfolders based on file types. It's a great utility to keep directories like Downloads or Desktop tidy.

---

## 🚀 Features

- Automatically detects and moves:
  - Images (`.jpg`, `.png`, etc.)
  - Excel files (`.xls`, `.xlsx`)
  - Python files (`.py`)
  - PDFs (`.pdf`)
  - Word documents (`.doc`, `.docx`)
  - Videos (`.mp4`, `.avi`, `.mkv`, etc.)
  - Text files (`.txt`, `.md`)
  - Archive files (`.zip`, `.rar`, `.7z`, `.tar.gz`)
  - Executables (`.exe`, `.bat`, `.sh`)
  - Web files (`.html`, `.css`, `.js`)
- Creates destination folders automatically if they do not exist.
- Outputs unmatched files that don't fit any category.

---


## 📦 Requirements

This script runs on **Python 3.x** and uses only standard libraries:

- `os`
- `shutil`

No external dependencies required.

---

## 🛠️ Usage

1. **Clone the repository** or copy the script.
2. **Run the script** using Python:

```bash
python file_organizer.py
Enter the path of the folder you want to organize when prompted.
```

📁 Example
If your folder has:

```
project/
├── image1.jpg
├── report.docx
├── video.mp4
├── script.py
```
After running the script, it will become:

```
project/
├── images/
│   └── image1.jpg
├── word_files/
│   └── report.docx
├── videos/
│   └── video.mp4
├── python_files/
│   └── script.py
```
