# This file experiments with the pydriller library

from pydriller import Repository
import glob

modified_files = 0

repos = ["https://github.com/hlin863/Supervised_Learning_CW2_group_repo", "https://github.com/ishepard/pydriller"]

for commit in Repository(path_to_repo=repos).traverse_commits():

    print("Project {}, commit {}, date {}".format(
           commit.project_path, commit.hash, commit.author_date))

"""
# traverse all commits in the repository and displays the commit has, the commit message, the author name and the modified files
for commit in Repository('https://github.com/ishepard/pydriller').traverse_commits():
    # print(commit.hash)
    # print(commit.msg)
    # print(commit.author.name)

    commit_file_names = [] # list to track the modified files in each commit.

    n_test_files = 0 # initialise a number to track the testing files for each commit.

    for file in commit.modified_files:
        # check if filename contains the word "test"
        if "test" in file.filename:
            n_test_files += 1 # increments the number of test files modified during each commit.

        commit_file_names.append(file.filename)

        # print(file.filename, ' has changed')
        modified_files += 1

    print("The number of test files modified in this commit is: ", n_test_files)

print("Total modified files: ", modified_files)
"""