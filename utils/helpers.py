import os
import random
import string
import shutil
from datetime import datetime


def get_collections_names():
    """
    :return: Just use it and it will generate random collection names
    """
    curr_date = str(datetime.now())
    date = curr_date.split('.')[0].replace(':', '-')
    random_letters = random.choices(string.ascii_letters, k=4)
    return "".join(random_letters) + date


def copy_to_project_folder(uploaded_files):
    """
    :param uploaded_files: Takes uploaded files to be copied to project folder
    :return:
    """
    # Set the destination folder in your project
    destination_folder = "data-files"

    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Construct the destination path
    for uploaded_file in uploaded_files:
        destination_path = os.path.join(destination_folder, uploaded_file.name)

        # Copy the uploaded file to the destination path
        with open(destination_path, "wb") as dest_file:
            dest_file.write(uploaded_file.getvalue())


def custom_files_loader(zip_file_path):
    """
    :param zip_file_path: This function takes a zip file path in your project folder
    :return: It just unzips the zip file into same folder
    """
    shutil.unpack_archive(zip_file_path, 'data-files/')
