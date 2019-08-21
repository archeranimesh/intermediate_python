import requests
import repos

GITHUB_API_URL = "https://api.github.com/search/repositories"

def create_query(languages, min_stars):
    """
    Create the query string for a Github search API,
    based on the minimum amout of stars for a project, and
    the provided languages.
    """
    # Notice we are calling .strip() on each languages.
    # to clear it of leading and trailing whitespace.
    query = " ".join(f"language:{languages.strip()}" for language in languages)
    query = query + f" stars:>{min_stars}"
    return query

def repos_with_most_stars(languages, min_stars=40000, sort="stars", order="desc"):
    query = create_query(languages, min_stars)
    parameters = {"q": query, "sort": sort, "order": order}

    print(parameters)
    response = requests.get(GITHUB_API_URL, params=parameters)

    if response.status_code != 200:
        raise repos.exceptions.GitHubApiError(response.status_code)

    response_json = response.json()
    items = response_json["items"]
    return [repos.models.GitHubRepo(item["name"], item["language"], item["stargazers_count"]) for item in items]