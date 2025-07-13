# data_extraction.py
# Extracción de datos desde la API de GitHub

import requests
from github_api_auth import HEADERS

def buscar_repositorios(query):
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def obtener_commits(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def obtener_contenido(owner, repo, path):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

# Ejemplo de uso
if __name__ == "__main__":
    print(buscar_repositorios("machine learning")["items"][0]["full_name"])
    print(obtener_commits("octocat", "Hello-World")[0]["commit"]["message"])
    print(obtener_contenido("octocat", "Hello-World", "README.md")["name"])
