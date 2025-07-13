# Data-Source-API-Analyst-Test
Homework assignment for Data Source API Analyst role.
# Data Source API Analyst - Technical Test

## 📌 Objetivo
Este proyecto es parte de la prueba técnica para la vacante de **Data Source API Analyst**. El objetivo es demostrar habilidades para:
- Investigar y consumir APIs (GitHub API REST v3)
- Extraer información usando Postman o Google Colab
- Documentar el proceso y manejar errores

---

## ✅ Paso 1: Preparar y Probar una Lista de Reportes

### 🔹 1. Necesidades del Cliente

El cliente necesita obtener información clave desde la API de GitHub:

| Requerimiento                 | Descripción |
|------------------------------|-------------|
| Buscar repositorios públicos | Encontrar repositorios según palabra clave, lenguaje o popularidad. |
| Obtener commits               | Ver el historial de cambios (commits) de un repositorio específico. |
| Consultar contenidos          | Leer archivos como README.md, código fuente, etc., dentro de un repositorio. |

---

### 🔹 2. Investigación de la API de GitHub

Se investigaron los endpoints y reglas para cubrir las necesidades del cliente.

#### 📚 Endpoints Identificados

| Acción                | Endpoint GitHub |
|-----------------------|-----------------|
| Buscar repositorios   | `GET https://api.github.com/search/repositories?q=python` |
| Obtener commits       | `GET https://api.github.com/repos/{owner}/{repo}/commits` |
| Obtener contenido     | `GET https://api.github.com/repos/{owner}/{repo}/contents/{path}` |

#### 🔐 Autenticación

- Se utiliza un **Personal Access Token (PAT)** generado en GitHub.
- Se debe agregar al header de las peticiones:
  ```http
  Authorization: Bearer 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

