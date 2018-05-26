import os

def rename_files():
    saved_path = os.getcwd()
    dir = "/Users/waqasahmed/Documents/Udacity/full-stack-nanodegree/python-course/exercises/03/secret_message"
    os.chdir(dir)
    file_list = os.listdir(dir)

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    
rename_files()
