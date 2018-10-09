import numpy as np
import matplotlib as mlp
import sys
import time
from git import Repo

mlp.use('TkAgg')
repo_path = sys.argv[1]

# we get the list of all the commits
repo = Repo(repo_path)
list_commits = list(repo.iter_commits())

# some configurations vars
commit_intensity = 10

# we prepare vars to be filled by our for loop
# contribution_timeline_dict = {}
scattered_plot_array = np.zeros((7, 24))
timeline_array = np.zeros((53, 7))
day_number_correspondances = {
    "Sun": 0,
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5,
    "Sat": 6,
}

# we fill our dict and our ndarray
for commit in list_commits:
    week_committed = int(time.strftime("%U", time.gmtime(commit.committed_date))) - 1

    day = time.strftime("%a", time.gmtime(commit.committed_date))
    day_int = day_number_correspondances[day]
    hour_int = int(time.strftime("%H", time.gmtime(commit.committed_date)))
    scattered_plot_array[day_int, hour_int] += 1
    timeline_array[week_committed, day_int] += commit_intensity

# we print them
print(timeline_array)
print(scattered_plot_array)
