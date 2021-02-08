import requests
from django.shortcuts import render
from .forms import UserForm


def index(request):
    userform = UserForm()
    return render(request, "MainPage.html", {"form": userform})


def result(request):
    if request.method == "POST":
        try:
            name = request.POST.get("login")
            url = 'https://api.github.com/graphql'
            json = {'query': '{ user(login:"' + name + '") {repositories(first: 50) { nodes { name }}}}'}
            api_token = "949a52be341f76e28cd765b3e61da4cc02c3d21b"
            headers = {'Authorization': 'token %s' % api_token}
            r = requests.post(url=url, json=json, headers=headers)
            c = r.json()
            remaining_rate_limit = c["data"]["user"]["repositories"]["nodes"]
            repositories = []
            for key in remaining_rate_limit:
                values = key.values()
                for i in values:
                    repositories.append(i)
            # render as partial view at the same route
            return render(request, "result.html", {"repositories": repositories})
        except Exception as e:
            return index(request)
    else:
        return index(request)
