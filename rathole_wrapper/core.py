import requests
import os
import zipfile
from subprocess import Popen

# Define the directory path where the current file is located
dir = os.path.dirname(os.path.realpath(__file__))
# Define the path for the rathole.exe file
rathole_exe_path = os.path.join(dir, 'rathole.exe')


# Function to download a file from a specified URL to a specified path
def download_file(url: str, path: str) -> None:
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


# Function to download the rathole executable
def download_rathole() -> None:
    # URL to download the rathole executable from
    url = "https://github.com/rapiz1/rathole/releases/download/v0.4.7/rathole-x86_64-pc-windows-msvc.zip"
    # Define the path for the rathole.zip file
    zip_path = os.path.join(dir, 'rathole.zip')
    # Download the rathole.zip file
    download_file(url, zip_path)
    # Extract the contents of the rathole.zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dir)
    # Remove the rathole.zip file
    os.remove(zip_path)


# Function to initialize the rathole service
def initialize() -> None:
    # If the rathole.exe file does not exist, download it
    if not os.path.exists(rathole_exe_path):
        download_rathole()


# Function to start the rathole service with a specified configuration file
def start(config_path: str) -> None:
    # Start the rathole service with the specified configuration file
    process = Popen([rathole_exe_path, config_path], shell=True)
    return process


# Class to manage the rathole service
class RatholeService:
    def __init__(self, config_path: str):
        # Store the path to the configuration file
        self.config_path = config_path
        # Initialize the process variable to None
        self.process = None

    # Function to start the rathole service
    def start(self) -> None:
        # If the rathole service is not running, start it
        if self.process is None:
            self.process = start(self.config_path)
        else:
            print('Rathole is already running!')

    # Function to stop the rathole service
    def stop(self) -> None:
        # Terminate the rathole service
        self.process.terminate()
        # Set the process variable to None
        self.process = None
    
    # Function to restart the rathole service
    def restart(self) -> None:
        # Start the rathole service
        self.start()
        # Stop the rathole service
        self.stop()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()


# Call the initialize
initialize()
