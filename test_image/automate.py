import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        print(f'File created: {event.src_path}')
        
        # Execute your Python script when a new file is written
        subprocess.run(["py", "C:\\py\\Vision\\test_image\\project.py"])

if __name__ == "__main__":
    path = "C:\\py\\Vision\\media\\images"  # directory being monitored

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

