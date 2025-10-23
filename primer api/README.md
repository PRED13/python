# MiniLang en Django

Instrucciones rápidas para ejecutar la aplicación en Windows (PowerShell):

1. Crear y activar un entorno virtual:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
python -m pip install --upgrade pip; pip install -r requirements.txt
```

3. Ejecutar el servidor de desarrollo:

```powershell
python manage.py runserver
```

4. Abrir en el navegador: http://127.0.0.1:8000/

Notas:
- Este proyecto contiene una app `minilang` que reproduce la funcionalidad de `main.py` y `0101_examen/main.py`.
- Si Django no está instalado en tu entorno, los linters en el editor mostrarán advertencias de importación; sigue los pasos anteriores para resolverlo.
