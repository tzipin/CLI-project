import json
import shutil
from datetime import datetime
import filesManager as fm
import os
import click

from commitDetails import CommitDetails


class Repository:
    def __init__(self, path):
        self.commit = {}
        self.path = path

    def wit_init(self):
        fm.create_new_folder(self.path, ".wit")
        fm.create_new_folder(os.path.join(self.path, ".wit"), "staging")
        fm.create_new_folder(os.path.join(self.path, ".wit"), "commits")

    def wit_add(self, file_name):
        fm.copy_file(os.path.join(self.path, file_name), os.path.join(self.path, ".wit\staging"), file_name)

    def wit_commit(self, message):
        if len(self.commit) == 0:
            self.start()
        index = int(fm.last_name_folder(os.path.join(self.path, ".wit\commits"))) + 1
        current_commit = CommitDetails(index, datetime.now().replace(microsecond=0), message)
        self.commit[current_commit.hash_code] = current_commit
        fm.copy_folder(os.path.join(self.path, ".wit\staging"), os.path.join(self.path, ".wit\commits"), str(index))
        fm.create_file(os.path.join(os.path.join(self.path, ".wit\commits"), str(index)), "details.json")
        fm.write_to_json_file(self.path + "\\.wit\commits\\" + str(index) + "\\details.json",
                              json.loads(str(self.commit[current_commit.hash_code])))
        fm.delete_folder_content(os.path.join(self.path, ".wit\staging"))

    def wit_log(self):
        if len(self.commit) == 0:
            self.start()
        for key in self.commit:
            print(f"{self.commit[key]}")

    def wit_status(self):
        if fm.is_empty_folder(os.path.join(self.path, ".wit\staging")):
            print("There are no files that have been COMMITed and ADDed")
        else:
            files = os.listdir(os.path.join(self.path, ".wit\staging"))
            for f in files:
                print(f)

    def wit_checkout(self, hash_code):
        folders = os.listdir(os.path.join(self.path, ".wit\commits"))
        working_files = os.listdir(self.path)
        for f in folders:
            routing = ".wit\commits\\" + str(f)
            with open(os.path.join(self.path, routing, "details.json"), "r") as file:
                details = json.load(file)
                if details["hash_code"] == hash_code:
                    commit_files = os.listdir(os.path.join(self.path, routing))
                    break
        temp = set(working_files) & set(commit_files)
        for f1 in temp:
            fm.delete_file(self.path, f1)
        for f1 in commit_files:
            if not f1 == "details.json":
                shutil.copy(os.path.join(self.path, routing, f1), self.path)

    def start(self):
        folders = os.listdir(os.path.join(self.path, ".wit\commits"))
        for f in folders:
            routing = ".wit\commits\\" + str(f)
            with open(os.path.join(self.path, routing, "details.json"), "r") as file:
                details = json.load(file)
                self.commit[details["hash_code"]] = details


