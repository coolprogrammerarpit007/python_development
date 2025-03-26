# OAuth API Verification
import requests
CLIENT_ID = "Ov23liaLIes6F32s7ikW"
CLIENT_SECRET = "644fbc5f8032c8e93748a6df813dc6c07bc38a91"
REDIRECT_URI = "https://saarthimanage.learnwellpublications.in/dashboard"

def create_outh_link():
    params = {
        "client_id":CLIENT_ID,
        "redirect_uri" : REDIRECT_URI,
        "scope":"user",
        "response_type":"code",
    }

    endpoint = "https://github.com/login/oauth/authorize"
    response = requests.get(endpoint,params=params)
    return response.url


def exchange_code_for_access_token(code=None):
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
    }

    headers = {"Accept":"application/json"}
    endpoint = "https://github.com/login/oauth/access_token"
    response = requests.post(endpoint,params=params,headers=headers).json()
    return response['access_token']

def print_user_info(access_token = None):
    headers = {"Authorization":f"token {access_token}"}
    endpoint = "https://api.github.com/user"
    response = requests.get(endpoint,headers=headers).json()
    name = response['name']
    username = response["login"]
    private_repos_count = response["total_private_repos"]
    print(
        f"{name} ({username}) | public repositories: {private_repos_count}"
    )



link = create_outh_link()
print(f"Follow the link to start the authentication with Github: {link}")
code = input("Github Code: ")
access_token = exchange_code_for_access_token(code)
print(f"Exchanged code {code} with access token: {access_token}")
print_user_info(access_token=access_token)