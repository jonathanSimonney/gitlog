import numpy as np
import matplotlib as mlp
import sys
from git import Repo

mlp.use('TkAgg')
repo_path = a = sys.argv[1]

repo = Repo(repo_path)
print(repo)
