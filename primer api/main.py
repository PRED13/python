import webbrowser
import os
import tempfile

# --- 1. DEFINICIÓN DEL CÓDIGO WEB COMPLETO (HTML, CSS y JavaScript) ---

# TODO: La lógica de cálculo (z = x*y+10, x_final = x+1) se mueve a JavaScript
# para que no necesite un servidor de backend (Flask) para funcionar.

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Examen - Automatas I</title>
    <!-- Tailwind CSS para estilos modernos -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .resultado-box {
            white-space: pre-wrap;
            font-family: 'Courier New', monospace;
        }
        /* Estilos del código original adaptados a Tailwind */
        .container {
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        }
    </style>
</head>
<body class="bg-gray-100 flex justify-center items-start min-h-screen p-6">

    <div class="container bg-white text-gray-800 p-8 md:p-10 rounded-xl shadow-2xl w-full max-w-md mt-10">
        <h1 class="text-3xl font-extrabold text-center mb-6 text-blue-600">
            === Examen ===
        </h1>

        <!-- El formulario ya NO hace un POST a un servidor de Python, sino que lo maneja JavaScript -->
        <form id="calcForm" class="space-y-6">
            <div>
                <label for="x" class="block text-lg font-semibold text-gray-700 mb-2">Valor de X:</label>
                <input type="number" id="x" value="0" required 
                       class="w-full p-3 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 text-lg transition duration-150">
            </div>

            <div>
                <label for="y" class="block text-lg font-semibold text-gray-700 mb-2">Valor de Y:</label>
                <input type="number" id="y" value="0" required 
                       class="w-full p-3 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 text-lg transition duration-150">
            </div>

            <button type="submit" 
                    class="w-full py-3 bg-blue-600 hover:bg-blue-700 text-white font-bold text-lg rounded-xl shadow-md transition duration-200 transform hover:scale-[1.01]">
                Calcular Operaciones
            </button>
        </form>

        <div id="resultContainer" class="hidden">
            <div class="resultado-box bg-gray-50 border border-gray-200 text-gray-900 p-5 mt-8 rounded-lg text-sm">
                <!-- Resultados aquí -->
            </div>
        </div>

        <footer class="text-center mt-8 text-xs text-gray-400">
            Aplicación de Cálculos - Automatas I (Autónoma)
        </footer>
    </div>

    <script>
        const form = document.getElementById('calcForm');
        const xInput = document.getElementById('x');
        const yInput = document.getElementById('y');
        const resultContainer = document.getElementById('resultContainer');
        const resultBox = resultContainer.querySelector('.resultado-box');

        /**
         * Realiza los cálculos en el frontend (navegador) sin necesidad de Flask.
         */
        function calculate(event) {
            event.preventDefault(); 
            
            // Obtener valores y asegurar que sean enteros
            const x0 = parseInt(xInput.value) || 0;
            const y0 = parseInt(yInput.value) || 0;

            // --- Lógica de Operaciones (Ahora en JavaScript) ---
            
            // z = x * y + 10
            const z = x0 * y0 + 10;
            
            // x = x + 1 (usando el valor original x0)
            const x_final = x0 + 1;

            // --- Generación del Resultado ---

            const resultadoTexto = `# Resultados de las operaciones:
x  = ${x0}
y  = ${y0}

z = x * y + 10
z = ${z}

x = x + 1
x = ${x_final}`;

            resultBox.textContent = resultadoTexto;
            resultContainer.classList.remove('hidden');
        }

        form.addEventListener('submit', calculate);
    </script>
</body>
</html>
"""

# --- 2. LÓGICA DE EJECUCIÓN DEL SCRIPT PYTHON ---

def crear_y_abrir_aplicacion_web_autonoma():
    """
    Crea un archivo HTML temporal con el contenido web y lo abre en el navegador
    sin iniciar ningún servidor web (ni Flask, ni http.server).
    """
    print("Iniciando aplicación web autónoma...")
    
    # Crea un archivo temporal en el sistema operativo
    # Usamos delete=False para que el archivo no se elimine inmediatamente después de cerrarse
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as tmp_file:
        tmp_file.write(HTML_CONTENT)
        filepath = tmp_file.name

    print(f"Archivo temporal generado en: {filepath}")
    
    # Abre el archivo en el navegador predeterminado
    # Esto es seguro y no requiere un servidor web
    webbrowser.open_new_tab('file://' + os.path.abspath(filepath))
    
    # NOTA: En este entorno de desarrollo, el archivo podría no abrirse
    # por restricciones de seguridad del sandbox, pero funcionará en un entorno local.
    print("\n¡Listo! La aplicación ha sido abierta en tu navegador predeterminado.")
    print("Cierra el navegador para terminar de usar la aplicación.")

if __name__ == "__main__":
    # Eliminamos el uso de threading para una ejecución simple y limpia
    crear_y_abrir_aplicacion_web_autonoma()