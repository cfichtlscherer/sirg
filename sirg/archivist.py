"""
Feb 17, 2020
Christopher Fichtlscherer (fichtlscherer@mailbox.org)
GNU General Public License
"""

import git

repo = git.Repo(search_parent_directories=True)
sha = repo.head.object.hexsha

print(sha)
