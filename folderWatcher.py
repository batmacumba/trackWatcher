import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from gameController import GameController


class Watcher:
    PATH = ""

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.PATH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):
    ControllerThread = None
    MIN_SIZE = 495e+6

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            if '.trk' in event.src_path[-4:]:
                if Handler.ControllerThread:
                    Handler.ControllerThread.stop()
                    Handler.ControllerThread = None

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            if '.trk' in event.src_path[-4:]:
                trackSize = Path(event.src_path).stat().st_size
                if trackSize > Handler.MIN_SIZE:
                    print("Trying to restart IL2 track recording...")
                    if not Handler.ControllerThread: 
                        Handler.ControllerThread = GameController()
                        Handler.ControllerThread.start()
                    
if __name__ == '__main__':
    w = Watcher()
    w.run()