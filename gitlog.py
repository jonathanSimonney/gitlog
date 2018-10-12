import numpy as np
import matplotlib
import sys
import time
from git import Repo
matplotlib.use('TkAgg')
import matplotlib.pyplot as pyp


def generate_months_array():
    twelve_months_array = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan']
    ret = ["" for _ in range(53)]
    acc = 0
    month_number = 0
    for i in range(len(ret)):
        acc += 7
        if (acc + 15) > 30:
            ret[i] = twelve_months_array[month_number]
            month_number += 1
            acc -= 30
    return ret


def draw_picture(data_array, x_legend, y_legend, title, x_axis_on_top=False):

    fig, ax = pyp.subplots()
    im = ax.imshow(data_array)

    # We want to show all ticks...
    ax.set_xticks(np.arange(len(x_legend)))
    ax.set_yticks(np.arange(len(y_legend)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(x_legend)
    ax.set_yticklabels(y_legend)

    ax.set_title(title)
    if x_axis_on_top:
        ax.xaxis.tick_top()
    fig.tight_layout()
    pyp.savefig(title)


def draw_scatter(data_array, x_legend, y_legend, title, x_axis_on_top=False):
    x_coords = []
    y_coords = []
    density_array = []

    # we populate the arrays useful for our scatter with the one parameter given
    for i in range(len(data_array)):
        for j in range(len(data_array[i])):
            if data_array[i, j] != 0:
                x_coords.append(i)
                y_coords.append(j)
                density_array.append(data_array[i, j])

    fig, ax = pyp.subplots()
    im = ax.scatter(x_coords, y_coords, density_array)

    # We want to show all ticks...
    ax.set_xticks(np.arange(len(x_legend)))
    ax.set_yticks(np.arange(len(y_legend)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(x_legend)
    ax.set_yticklabels(y_legend)

    ax.set_title(title)
    if x_axis_on_top:
        ax.xaxis.tick_top()
    fig.tight_layout()
    pyp.savefig(title)


repo_path = sys.argv[1]

# we get the list of all the commits
repo = Repo(repo_path)
list_commits = list(repo.iter_commits())

# some configurations vars
commit_intensity = 1
max_number_commiters = 25
months_array = generate_months_array()
day_number_correspondances = {
    "Sun": 0,
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5,
    "Sat": 6,
}

# we prepare vars to be filled by our for loop
# contribution_timeline_dict = {}
commits_scattered_plot_array = np.zeros((7, 24))
timeline_array = np.zeros((7, 53))
committers_name_dict = {}
committers_name_array = []

# we fill our dict and our ndarray
for commit in list_commits:
    week_committed = int(time.strftime("%U", time.gmtime(commit.committed_date))) - 1

    day = time.strftime("%a", time.gmtime(commit.committed_date))
    day_int = day_number_correspondances[day]
    hour_int = int(time.strftime("%H", time.gmtime(commit.committed_date)))

    commits_scattered_plot_array[day_int, hour_int] += 1
    timeline_array[day_int, week_committed] += commit_intensity

    committer_name = commit.author.name
    if committer_name not in committers_name_dict and len(committers_name_array) < max_number_commiters:
        committers_name_dict[committer_name] = len(committers_name_array)
        committers_name_array.append(committer_name)

commiters_scattered_plot_array = np.zeros((24, len(committers_name_array)))
# we iterate once more to get another scatter_plot with the contributor this time
for commit in list_commits:
    hour_int = int(time.strftime("%H", time.gmtime(commit.committed_date)))

    committer_name = commit.author.name
    if committer_name in committers_name_dict:
        committer_int = committers_name_dict[committer_name]

        commiters_scattered_plot_array[hour_int, committer_int] += 1

# we use them to draw our pictures
draw_picture(timeline_array, months_array, ["", "Mon", "", "Wed", "", "Fri", ""], "Timeline.png", True)
draw_scatter(commits_scattered_plot_array, ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], [str(i) for i in range(24)],
             "commits.png")
draw_scatter(commiters_scattered_plot_array, [str(i) for i in range(24)], committers_name_array,
             "commits_per_person.png")
