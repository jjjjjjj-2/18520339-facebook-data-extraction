from github import Github
import requests

# file path on the repository
file_path = "README.md"

# enter your API token generated from Github
token = input("Please enter your Github token: ")
key = Github(token)

# repository format: author/project
repo = key.get_repo("18520339/facebook-data-extraction")
file = repo.get_contents(file_path, ref="master")

# decode the content in utf-8
data = file.decoded_content.decode("utf-8")

# write content to a local disk file
with open(file_path, 'w', encoding='utf-8') as f:
	f.write(data)

print("Github data collection completed!")