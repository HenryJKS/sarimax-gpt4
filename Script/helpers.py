import os
from Script.config import UPLOAD_PATH


def save_file_in_uploads(filename):
    os.path.join(UPLOAD_PATH, filename)
