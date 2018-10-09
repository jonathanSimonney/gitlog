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


def draw_picture(data_array, x_legend, y_legend, title):

    fig, ax = pyp.subplots()
    im = ax.imshow(data_array)

    # We want to show all ticks...
    ax.set_xticks(np.arange(53))
    ax.set_yticks(np.arange(7))
    # ... and label them with the respective list entries
    ax.set_xticklabels(x_legend)
    ax.set_yticklabels(y_legend)

    # Rotate the tick labels and set their alignment.
    # pyp.setp(ax.get_xticklabels(), rotation=90, ha="right",
    #          rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    # for i in range(len(x_legend)):
    #     for j in range(len(y_legend)):
    #         text = ax.text(i, j, data_array[j, i],
    #                        ha="center", va="center", color="w", )

    ax.set_title(title)
    fig.tight_layout()
    pyp.show()


repo_path = sys.argv[1]

# we get the list of all the commits
repo = Repo(repo_path)
list_commits = list(repo.iter_commits())

# some configurations vars
commit_intensity = 10
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
scattered_plot_array = np.zeros((7, 24))
timeline_array = np.zeros((7, 53))

# we fill our dict and our ndarray
for commit in list_commits:
    week_committed = int(time.strftime("%U", time.gmtime(commit.committed_date))) - 1

    day = time.strftime("%a", time.gmtime(commit.committed_date))
    day_int = day_number_correspondances[day]
    hour_int = int(time.strftime("%H", time.gmtime(commit.committed_date)))
    scattered_plot_array[day_int, hour_int] += 1
    timeline_array[day_int, week_committed] += commit_intensity

# we print them
print(timeline_array)
print(scattered_plot_array)

# pyp.imshow(timeline_array, origin="upper", extent=[0, 53, 0, 7],
#                    interpolation="nearest")
# pyp.draw()
# pyp.show()
draw_picture(timeline_array, months_array, ["", "Mon", "", "Wed", "", "Fri", ""], "Timeline.png")
