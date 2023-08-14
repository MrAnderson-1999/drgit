import github
import re
import requests

def add_documentation_comments(repo_url):
    """Adds documentation comments to the whole GitHub repo using ChimeraGPT API."""
    repo = github.Repo(repo_url)
    for file in repo.get_files():
        with open(file.path, "r") as f:
            code = f.read()
        new_code = add_documentation_comments_to_code(code, repo.name, file.name)
        with open(file.path, "w") as f:
            f.write(new_code)

def add_documentation_comments_to_code(code, repo_name, file_name):
    """Adds documentation comments to the given code using ChimeraGPT API."""
    comments = []
    for line in code.splitlines():
        line = line.strip()
        if line.startswith("//"):
            comments.append(line)
        elif line.startswith("/*"):
            comments.append(line)
            while not line.endswith("*/"):
                line = line[1:]
                comments.append(line)
        else:
            response = requests.post("https://api.chimeragpt.com/generate", json={"prompt": f"(Automated GPT comment): {line} for {repo_name}/{file_name}"})
            if response.status_code == 200:
                comments.append(response.json()["text"])
            else:
                comments.append("(Automated GPT comment): Failed to generate documentation comment")
    return "\n".join(comments)

if __name__ == "__main__":
    repo_url = input("Enter the GitHub repo URL: ")
    add_documentation_comments(repo_url)
