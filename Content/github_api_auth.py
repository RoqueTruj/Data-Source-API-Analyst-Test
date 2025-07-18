# Este archivo será usado para autenticarse con la API de GitHub
# github_api_auth.py
# Módulo de autenticación para usar la API de GitHub

import requests

# Token de acceso personal (PAT)
GITHUB_TOKEN = "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"

# Headers necesarios para autenticación
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}

def test_auth():
    response = requests.get("https://api.github.com/user", headers=HEADERS)
    if response.status_code == 200:
        print("✅ Autenticación exitosa.")
    else:
        print(f"❌ Error de autenticación: {response.status_code}")

# Ejecutar test
if __name__ == "__main__":
    test_auth()
