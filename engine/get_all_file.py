import os



def get_all_file_name(file_path):
    file_list = os.listdir(file_path)
    return file_list