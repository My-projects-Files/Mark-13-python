import requests

url=f"https://api.github.com/repos/kubernetes/kubernetes/pulls"

response=requests.get(url)
status= response.status_code

if status == 200:
    complete=response.json()
    pull_cr={}
    for i in complete:
        cr= i ['user']['login']
        if cr in pull_cr:
            pull_cr[cr]+=1
        else:
            pull_cr[cr]=1
    print(pull_cr)
    print("pull request created and counts:")
    for cr,count in pull_cr.items():
        print(f"pull requests for {cr}:{count}")
else:
    print(f"failed to fetch data.error code:{status}")