from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import logging
import json
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("file_sorter.log", encoding="utf-8"), 
        logging.StreamHandler() 
    ]
)

def load_config():
    config_path = Path(__file__).parent / "config.json"
    if not config_path.exists():
        logging.error("Config file not found.")
        return {}
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing config file: {e}")
        return {}

class DownloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        time.sleep(2)
        self.process_folder()
    def process_folder(self):
        config = load_config()
        mapping = config.get("mapping", {})
        downloads_path = Path.home() / "Downloads"

        for file in downloads_path.iterdir():
            if not file.is_file() or file.name == "file_sorter.log":
                continue
            file_extension = file.suffix.lower()
            target_folder = None

            for folder, extensions in mapping.items():
                if file_extension in extensions:
                    target_folder = downloads_path / folder
                    break
            if target_folder:
                self.move_file(file, target_folder)
    def move_file(self, file, target_folder):
        try:
            target_folder.mkdir(exist_ok=True)
            new_name = file.name
            destination = target_folder / new_name
            counter = 1
            while destination.exists():
                new_name = f"{file.stem} ({counter}){file.suffix}"
                destination = target_folder / new_name
                counter += 1
            shutil.move(str(file), str(destination))
            logging.info(f"File {file.name} moved to folder {target_folder.name}")
        except Exception as e:
            logging.error(f"Failed to move {file.name}: {e}")

if __name__ == "__main__":
    path_to_watch = Path.home() / "Downloads"
    event_handler = DownloadHandler()
    event_handler.process_folder()
    observer = Observer()
    observer.schedule(event_handler, str(path_to_watch), recursive=False)
    observer.start()
    logging.info("Started monitoring Downloads folder.")
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()