from github import Github

# First create a Github instance:

# using username and password
g = Github("flz17", "Saadmin13q1w2e3r4t5y6u7")

# or using an access token
#g = Github("d3ed56816a8f674ec722c00477f764b78be8ae8d")

# Github Enterprise with custom hostname
#g = Github(base_url="https://github.com/api/v3", login_or_token="d3ed56816a8f674ec722c00477f764b78be8ae8d")

# Then play with your Github objects:
#for repo in g.get_user().get_repos():
#    print(repo.name)

curl 'https://api.github.com/user/repos'
