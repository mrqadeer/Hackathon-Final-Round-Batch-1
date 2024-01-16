import os


from setuptools import setup
import subprocess

# Function to install requirements from requirements.txt
def install_requirements():
    try:
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    except Exception as e:
        print(f"Error installing requirements: {e}")
        raise
if __name__=="__main__":
    os.makedirs("data-files",exist_ok=True)
    install_requirements()