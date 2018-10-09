# gitlog

## setup
to use this project, simply run 

    pipenv install
    pipenv shell
    
And in the newly opened shell, 

    gitlog.py path_to_git_repo
    
## prerequisite
you need to have pipenv installed on your computer

## what does it do
it creates different png files on your computer. Be warned : if file with 
these name already exist, they'll be overwritten:

- A ```timeline.png``` week by week, such as "contributions in the last year" on github.  
- A ```commits.png``` file containing a scatter plot where  size of dots depends of the number of commits, on the horizontal axis 
the seven days of the week, and on the vertical axis the 24h of the day.
- Others, if I have some other ideas.
