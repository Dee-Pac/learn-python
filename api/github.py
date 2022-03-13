import requests, enum, os, json
from requests.auth import HTTPBasicAuth

class Environment(enum.Enum):
    DEV, QA, PROD = 1, 2, 3

class Github:
    """Helper Utility to handle Github operations.

        #-- Initiate Github -- #

        Specify User and Basic OAUTH Key
        github = Github("<USER>", "<PERSONAL_ACCESS_TOKEN>", Environment.PROD)
        Pick User and OAUTH key from runtime environment
        github = Github(Environment.PROD) 

        #-- LIST Pull Request -- #

        pullRequests = github.listPullRequests("<ORG>", "<REPO>")
        print(pullRequests)

        #-- CREATE Pull Requests -- #

        pullId, url, resp = github.createPullRequest("<ORG>", "<REPO>", "del1", "del2", "API Test", "Test Body")
        print(pullId, url, resp)

        #-- UPDATE an existing Pull Request -- #

        github.updatePullRequest("<ORG>", "<REPO>", pullRequestId = pullId, state = "close")

        #-- MERGE Pull Request -- #

        respDict = json.loads(resp)
        sha = respDict["head"]["sha"]
        resp = github.mergePullRequest("<ORG>", "<REPO>", pullId, sha, "Merge", "Test")
        print(resp)
    """

    def __init__(self, user = None, personal_access_token = None, env = Environment.PROD):
        self.user = user if user else os.environ.get('USER')
        self.personal_access_token = personal_access_token if personal_access_token else os.environ.get('PERSONAL_ACCESS_TOKEN')
        self.env = env
        self.host = None
        self.rootPath = "api/v3/repos"
        if (self.env == Environment.PROD):
            self.host = "https://github.paypal.com"
        else:
            raise Exception("Only Production Environment is currently supported.")
        self.rootUrl = self.host + "/" + self.rootPath
        self.auth = HTTPBasicAuth(self.user, self.personal_access_token)
        self.requestHeader = {"Accept" : "application/vnd.github.v3+json"}
        
    def listPullRequests(self, org, repo):
        """
        Lists pull requests in the given repo.
        More details on Github API : https://docs.github.com/en/rest/reference/pulls#list-pull-requests
        """
        requestUrl = "{}/{}/{}/pulls".format(self.rootUrl, org, repo)
        resp = requests.get(url = requestUrl, auth = self.auth, headers = self.requestHeader)
        
        if (resp.status_code != 200):
            raise Exception(resp.text)
        else:
            print("List Pull Request - Success.")

        return resp.text

    def createPullRequest(self, org, repo, head, base, title, body, moreOptions = dict()):
        """
        Creates Pull Request as specified.
        Returns Tuple : PR_ID, PR_HTML_URL, FULL_RESPONSE_TEXT
        More details on Github API : https://docs.github.com/en/rest/reference/pulls#create-a-pull-request
        """

        requestUrl = "{}/{}/{}/pulls".format(self.rootUrl, org, repo)
        requestBody = dict()
        requestBody["head"] = head
        requestBody["base"] = base
        requestBody["title"] = title
        requestBody["body"] = body
        requestBody["bodmaintainer_can_modifyy"] = True
        requestBody.update(moreOptions)

        resp = requests.post(url = requestUrl, headers = self.requestHeader, data = json.dumps(requestBody), auth = self.auth)
        
        if (resp.status_code != 201):
            raise Exception(resp.status_code, resp.text)
        else:
            print("Create Pull Request - Success.")

        respJson = json.loads(resp.text)
        print("Pull Request [{}] created. Url [{}]".format(respJson["number"], respJson["html_url"]))

        return respJson["number"], respJson["html_url"], resp.text

    def updatePullRequest(self, org, repo, pullRequestId, head = None, base = None, title = None, body = None, state = None, moreOptions = dict()):
        """
        Updates Pull Request as specified.
        More details on Github API : https://docs.github.com/en/rest/reference/pulls#update-a-pull-request
        """

        requestUrl = "{}/{}/{}/pulls/{}".format(self.rootUrl, org, repo, pullRequestId)
        requestBody = dict()
        if (head): requestBody["head"] = head
        if (base): requestBody["base"] = base
        if (title): requestBody["title"] = title
        if (body): requestBody["body"] = body
        if (state): requestBody["state"] = state
        requestBody.update(moreOptions)

        resp = requests.post(url = requestUrl, headers = self.requestHeader, data = json.dumps(requestBody), auth = self.auth)
        
        if (resp.status_code != 200):
            raise Exception(resp.text)
        else:
            print("Update Pull Request {} - Success.".format(pullRequestId))

        return resp.text

    def mergePullRequest(self, org, repo, pullRequestId, sha, commitTitle , commitMessage , mergeMethod = "squash", moreOptions = dict()):
        """
        Merges Pull Request as specified.
        More details on Github API : https://docs.github.com/en/rest/reference/pulls#merge-a-pull-request
        """

        requestUrl = "{}/{}/{}/pulls/{}/merge".format(self.rootUrl, org, repo, pullRequestId)
        requestBody = dict()
        requestBody["pull_number"] = pullRequestId
        requestBody["sha"] = sha
        requestBody["commit_title"] = commitTitle
        requestBody["commit_message"] = commitMessage
        requestBody["merge_method"] = mergeMethod
        requestBody.update(moreOptions)

        print(requestBody)

        resp = requests.put(url = requestUrl, headers = self.requestHeader, data = json.dumps(requestBody), auth = self.auth)
        if (resp.status_code != 200):
            raise Exception(resp.text)
        else:
            print("Merge Pull Request {} - Success.".format(pullRequestId))

        return resp.text



