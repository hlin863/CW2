from pydriller import Repository

# traverse all commits and check the commit size
for commit in Repository('https://github.com/ishepard/pydriller').traverse_commits():

    print("The commit size is: ", commit.size)