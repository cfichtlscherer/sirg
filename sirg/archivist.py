"""
Feb 17, 2020
Christopher Fichtlscherer (fichtlscherer@mailbox.org)
GNU General Public License
"""

import git as git
import time as time
import os as os
import shutil as shutil


def archivist(function):
    """
    This decorator can be used for every function.
    All the results of this function will be stored in a apecial archive.
    """
    def wrapper(*args, **kwargs):

        # calculating the results of the function
        results = function(*args, **kwargs)

        # generating the file name
        repo = git.Repo(search_parent_directories=True)
        sha = repo.head.object.hexsha[:10]
        time_now = time.strftime("%H:%M:%S-%d%m%y_")
        name = function.__name__
        args = str(args).replace(" ", "")
        file_name = time_now + sha + "_" + name + args

        # open file and writing everything in it
        f = open(file_name, "w+")
        f.write(str(results))
        f.close()

        # generate archive folder if it dosen't exist
        cwd = os.getcwd()
        start_sirg = cwd.find("sirg")
        archive_path = cwd[:start_sirg] + "sirg_archive"
        if not os.path.exists(archive_path):
            os.makedirs(archive_path)

        # move the file to the archive
        start = cwd + "/" + file_name
        end = archive_path + "/" + file_name
        shutil.move(start, end)

        return results

    return wrapper
