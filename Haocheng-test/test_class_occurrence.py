# This file experiments with the pydriller library

from pydriller import Repository
import pandas as pd # import the pandas library to convert the commit messages into a dataframe for storage and analysis.
import glob

modified_files = 0

repos = ["https://github.com/hlin863/Supervised_Learning_CW2_group_repo", "https://github.com/ishepard/pydriller"]

apache_repos = ['https://github.com/apache/camel-website'] # initialise to list for storing and analysing the Apache repositories.

commit_msgs = [] # initialise a list to store the commit messages.

for commit in Repository(apache_repos).traverse_commits():

    commit_msgs.append(commit.msg) # append the commit message to the list.

    # print(commit.msg)
    # print(commit.hash)
    # print(commit.insertions)
    # print(commit.deletions)

# convert the commit messages into a dataframe for storage and analysis.
commit_msgs_df = pd.DataFrame(commit_msgs, columns=['commit_msg'])

# save the commit messages as a csv file.
commit_msgs_df.to_csv('Data/commit_msgs.csv', index=False)