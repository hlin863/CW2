from pydriller import Repository
import requests # import the requests library to get the list of repositories from the Apache GitHub site.

repos = [] # initalise a list of repositories to be analysed.

# mine the repositories from Apache GitHub.
apache_site = "https://github.com/orgs/apache/repositories" # the URL of the Apache GitHub site.

# get the list of repositories from the Apache GitHub site.
r = requests.get(apache_site)

# extract the repository names from the list of repositories.
for line in r.text.splitlines():

    if "href=\"/apache/" in line:
        repo_name = line.split("/")[2]
        repos.append(repo_name)

print("There are {} repositories in the Apache GitHub site.".format(len(repos)))