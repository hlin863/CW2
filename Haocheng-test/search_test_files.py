from pydriller import Repository
import requests # import the requests library to get the list of repositories from the Apache GitHub site.

repos = [] # initalise a list of repositories to be analysed.

# mine the repositories from Apache GitHub.
apache_site = "https://github.com/orgs/apache/repositories" # the URL of the Apache GitHub site.

# get the list of repositories from the Apache GitHub site.
repos_list = requests.get(apache_site).text

print(repos_list)