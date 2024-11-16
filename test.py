import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, app_path):
        super().__init__()
        self.app_path = app_path
        self.process = None
        self.restart_app()

    def on_modified(self, event):
        if event.src_path.endswith(self.app_path):
            self.restart_app()

    def restart_app(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        self.process = subprocess.Popen([sys.executable, self.app_path])

if __name__ == "__main__":
    app_path = "test_ui.py"
    event_handler = ChangeHandler(app_path)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    try:
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
        if event_handler.process:
            event_handler.process.terminate()