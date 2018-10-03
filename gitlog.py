import numpy as np
import matplotlib as mlp
import sys
import time
from git import Repo

mlp.use('TkAgg')
repo_path = a = sys.argv[1]

repo = Repo(repo_path)
list_commits = list(repo.iter_commits())
print(len(list_commits))

for commit in list_commits:
    print(commit.authored_date)
    print(time.asctime(time.gmtime(commit.authored_date)))
