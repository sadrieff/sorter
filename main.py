from pathlib import Path
import os  
import logging

username = os.environ.get("USERNAME")
downloads_path = Path('C:/Users/'+username+'/Downloads')

mapping = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.heic'],
    'Videos': ['.mp4', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar.gz', '.7z'], 
    'Executables': ['.exe', '.msi'],
    'Spreadsheets': ['.xlsx', '.csv'],
    'Presentations': ['.pptx', '.ppt'],
    'Torrents': ['.torrent'],
    'Applications': ['.apk', '.app', '.dmg']

}

for file in downloads_path.iterdir():
    if file.is_file():
        file_extension = file.suffix.lower()
        for folder, extensions in mapping.items():
            if file_extension in extensions:
                destination_folder = downloads_path / folder
                destination_folder.mkdir(exist_ok=True)
                file.rename(destination_folder / file.name)
                print(f"Файл {file.name} перемещен в {destination_folder}")
                break