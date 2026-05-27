# dev_runner.py
import os
import sys
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
  def __init__(self, script_name):
    self.script_name = script_name
    self.process = None
    self.runner_path = os.path.abspath(__file__)
    self.start_process()

  def start_process(self):
    """Launches the Tkinter application as a separate subprocess."""
    if self.process:
      self.process.terminate()  # Kill the existing application safely
      self.process.wait()
      print("\n[Watcher] Code change detected! Restarting app...\n")
    
    # Start a brand new instance of your script
    self.process = subprocess.Popen([sys.executable, self.script_name])

  def on_modified(self, event):
    """Triggered automatically whenever any file or folder is modified."""
    # Convert the modified file path to an absolute path
    abs_modified_path = os.path.abspath(event.src_path)
    
    # 1. Ignore directories
    if event.is_directory:
        return
        
    # 2. Only reload for Python files
    # 3. Ensure the modified file isn't this dev_runner script
    if abs_modified_path.endswith(".py") and abs_modified_path != self.runner_path:
        time.sleep(0.2)  # Short cooldown to allow your text editor to finish writing
        self.start_process()

if __name__ == "__main__":
  TARGET_SCRIPT = "main.py"  # Your Tkinter file name
  
  event_handler = ChangeHandler(TARGET_SCRIPT)
  observer = Observer()
  observer.schedule(event_handler, path=".", recursive=True)
  observer.start()
  
  print(f"[Watcher] Monitoring changes for {TARGET_SCRIPT}. Press Ctrl+C to stop.")

  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()
    if event_handler.process:
      event_handler.process.terminate()
  observer.join()
