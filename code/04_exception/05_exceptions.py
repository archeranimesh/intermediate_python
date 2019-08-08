# Always name the custom exception as Error or Exception.
class GitHubApiError(Exception):
    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached."
        else:
            message = f"The status code was {status_code}"
        super().__init__(self, message)


if __name__ == "__main__":
    raise GitHubApiError(403)
