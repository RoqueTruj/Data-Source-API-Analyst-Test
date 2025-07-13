# 🧩 Guía de resolución de problemas – GitHub API

## Errores comunes

### ❌ 401 Unauthorized
- El token es inválido, ha expirado o no se envió correctamente.
- Verifica que uses el header:

### ⚠️ 403 Rate Limit Exceeded
- Has superado el límite de peticiones (60/hora sin token, 5000/hora con token).
- Espera o cambia de token.
- Puedes revisar tu límite actual con:

### ❗ 404 Not Found
- El repositorio o archivo no existe, o la ruta está mal escrita.
- Verifica el nombre del owner, repo y path.

## Recomendaciones
- Siempre usa un token autenticado.
- Maneja errores con `try/except` y revisa el código de estado (`response.status_code`)
