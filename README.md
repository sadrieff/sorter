# FileSorter-Python 📂

A professional, event-driven Python utility that automatically organizes your Downloads folder in real-time. Stop manual sorting and let the script handle the chaos.

## ✨ Features
- **Live Monitoring**: Uses `watchdog` to detect new files and move them instantly.
- **Smart Collision Handling**: Automatically renames duplicates (e.g., `file(1).jpg`) to prevent data loss.
- **External Configuration**: Manage file mappings and extensions easily via `config.json`.
- **Robust Logging**: Keeps a detailed history of all operations in `file_sorter.log`.
- **Cross-Platform**: Seamlessly works on Windows, macOS, and Linux thanks to `pathlib`.

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher.

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/Sadrieff/sorter]
2. Install required dependencies::
   ```bash
   pip install -r requirements.txt
3. Run the application:
    ```bash
    python main.py

## ⚙️ Configuration
```json
{
"mapping": {
"Images": [".jpg", ".png"],
"Documents": [".pdf", ".txt"]
}
}
```
## 🗺️ Roadmap

- **[x] Cross-platform support (macOS/Linux/Windows).

- **[x] Duplicate handling (Safe renaming).

- **[x] Logging system.

- **[x] External JSON configuration.

- **[x] Real-time file system monitoring.