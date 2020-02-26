"""
Feb 17, 2020
Christopher Fichtlscherer (fichtlscherer@mailbox.org)
GNU General Public License
"""

import git as git
import time as time


def archivist(function):
    def wrapper(*args, **kwargs):

        results = function(*args, **kwargs)

        repo = git.Repo(search_parent_directories=True)
        sha = repo.head.object.hexsha[:10]

        time_now = time.strftime("%H:%M:%S-%d%m%y_")

        name = function.__name__

        args = str(args).replace(" ", "")

        file_name = time_now + sha + "_" + name + args
    
        print(file_name)
    
        # datei öffnen mit dem namen
        # results da rein packen
        # datei schließen 
        # datei an ort packen wo gut
        
    return wrapper

@archivist
def add(a, b):
    return a + b

add(1, 2)
