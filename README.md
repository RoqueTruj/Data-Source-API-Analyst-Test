# Data Source API Analyst Test

This repository contains the solution for the technical assignment for the **Data Source API Analyst** position. The goal was to demonstrate API knowledge by using GitHub’s public REST API for authenticated requests, pagination handling, rate limit management, and data extraction.

---

## 📌 Objective

The purpose of this project is to demonstrate the ability to:

- Understand and use REST APIs (GitHub API)
- Make authenticated requests using tokens
- Extract relevant information: repositories, commits, file contents
- Troubleshoot common issues (e.g., errors, rate limits)
- Document and organize work professionally

---

## 🛠️ Technologies Used

- [Google Colab](https://colab.research.google.com/) (Python + requests)
- [GitHub REST API](https://docs.github.com/en/rest)
- Postman (optional)
- Git and GitHub

---


---

## 📓 Notebook Description

The file `github_api_test.ipynb` includes:

1. **Authentication** using a personal GitHub token
2. **Data extraction**:
   - Public repository search (by keyword)
   - Commit listing per repository
   - File content extraction (e.g., README.md)
3. **Error handling** for status codes (401, 403, 404)
4. **Rate limit verification** using the `/rate_limit` endpoint

---

## 🔍 Key Details

- Modular Python functions were created for reuse and clarity.
- GitHub’s required headers (`X-GitHub-Api-Version`) were used.
- Token is stored securely using variables within the notebook.
- Each API call prints sample responses for validation.

---

## 🔧 Troubleshooting Guide

See the file [`Content/troubleshooting.md`](Content/troubleshooting.md) for how common issues were addressed, such as:

- ❌ `401 Unauthorized`
- 🚫 `403 Rate Limit Exceeded`
- 🛑 `404 Not Found`

---

## 🧠 Final Thoughts

This was a very practical and interesting task that allowed me to demonstrate hands-on experience with REST APIs, data extraction, and clean documentation.  
Google Colab was chosen for its flexibility and ease of sharing.

---

**Author:** [Your Name]  
**Date:** [Submission Date]  




#### 🔐 Autenticación

- Se utiliza un **Personal Access Token (PAT)** generado en GitHub.
- Se debe agregar al header de las peticiones:
  ```http
  Authorization: Bearer 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

