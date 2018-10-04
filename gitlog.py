import numpy as np
import matplotlib as mlp
import sys
import time
from git import Repo

mlp.use('TkAgg')
repo_path = sys.argv[1]

repo = Repo(repo_path)
list_commits = list(repo.iter_commits())

contribution_timeline_dict = {}

for commit in list_commits:
    print(commit.committed_date)
    day_committed = (time.strftime("%a, %d %b %Y", time.gmtime(commit.committed_date)))
    print(day_committed)
    print(time.strftime("%a, %d %b %Y %H:%M", time.gmtime(commit.committed_date)))
    if day_committed in contribution_timeline_dict:
        contribution_timeline_dict[day_committed] += 1
    else:
        contribution_timeline_dict[day_committed] = 1

print(contribution_timeline_dict)
