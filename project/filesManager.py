import json
import os
import shutil


def create_new_folder(routing, folder_name):
    try:
        os.makedirs(routing + "\\" + folder_name)
        print(f"the folder {folder_name} create successfully")
    except:
        print("you have error")


def create_file(routing, file_name):
    if os.path.exists(routing + "\\" + file_name):
        print("this file is exists")
    else:
        f = open(routing + "\\" + file_name, "w")
        f.close()


def write_to_json_file(routing, text):
    with open(routing, "w") as file:
        json.dump(text, file)


def delete_folder_content(routing):
    if not os.path.exists(routing):
        print("error: your path not exists")
    else:
        files = os.listdir(routing)
        for f in files:
            os.remove(os.path.join(routing, f))


def copy_folder(source, target, name_folder):
    shutil.copytree(source, os.path.join(target, name_folder))


def copy_file(source, target, name_file_target):
    shutil.copyfile(source, os.path.join(target, name_file_target))


def is_empty_folder(routing):
    dir = os.listdir(routing)
    if len(dir) == 0:
        return True
    return False


def delete_file(routing, file_name):
    os.remove(os.path.join(routing, file_name))


def last_name_folder(routing):
    if is_empty_folder(routing):
        return 0
    folders = os.listdir(routing)
    folders.sort(key=int)
    return folders[-1]
