import requests

# 执行 API 调用并存储相应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code)

# 将 API 相应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict["total_count"])

# 探索有关仓库的信息
repo_dicts = response_dict["items"]
print("Repositories returned:", len(repo_dicts))

print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print()
    print("Name:", repo_dict["name"])
    print("Owner:", repo_dict["owner"]["login"])
    print("Stars:", repo_dict["stargazers_count"])
    print("Repository:", repo_dict["html_url"])
    # print("Created:", repo_dict["created_at"])
    # print("Updated:", repo_dict["updated_at"])
    print("Description:", repo_dict["description"])
