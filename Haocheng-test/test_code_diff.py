from pydriller import Repository

for commit in Repository('https://github.com/hlin863/Supervised_Learning_CW2_group_repo').traverse_commits():
    for m in commit.modified_files:
        print(
            "Author {}".format(commit.author.name),
            " modified {}".format(m.filename),
            " with a change type of {}".format(m.change_type.name),
            " and the complexity is {}".format(m.complexity)
        )