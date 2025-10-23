from flask import Flask, render_template_string, request
import webbrowser
import threading

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Examen - Autómatas I</title>
<style>
body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    color: #fff;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    height: 100vh;
    margin: 0;
    padding: 40px;
}
.container {
    background-color: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(12px);
    border-radius: 16px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.4);
    padding: 40px;
    width: 450px;
}
h1 {
    text-align: center;
    font-size: 28px;
    margin-bottom: 30px;
    color: #00bcd4;
    letter-spacing: 1px;
}

input[type="number"] {
    width: 100%;
    padding: 12px;
    border-radius: 10px;
    border: none;
    margin-top: 8px;
    font-size: 16px;
    background-color: #23232e;
    color: #fff;
    outline: none;
    transition: all 0.3s ease;
}
input[type="number"]:focus {
    background-color: #333;
    box-shadow: 0 0 5px #00bcd4;
}
button {
    width: 100%;
    padding: 14px;
    border: none;
    border-radius: 10px;
    background: linear-gradient(90deg, #00bcd4, #0097a7);
    color: #fff;
    font-weight: bold;
    font-size: 15px;
    margin-top: 25px;
    cursor: pointer;
    transition: transform 0.2s ease, background 0.3s ease;
}
button:hover {
    transform: scale(1.02);
    background: linear-gradient(90deg, #26c6da, #00acc1);
}
.resultado {
    background-color: rgba(0, 0, 0, 0.3);
    border-left: 4px solid #00bcd4;
    padding: 20px;
    margin-top: 30px;
    border-radius: 10px;
    font-family: 'Courier New', monospace;
    white-space: pre-wrap;
}
footer {
    text-align: center;
    margin-top: 25px;
    font-size: 13px;
    color: #aaa;
}
</style>
</head>
<body>
<div class="container">
    <h1>Examen - Autómatas I</h1>

    <form method="post">
        <label for="x">Valor de X:</label>
        <input type="number" name="x" value="{{ x }}" required>

        <label for="y">Valor de Y:</label>
        <input type="number" name="y" value="{{ y }}" required>

        <button type="submit">Calcular</button>
    </form>

    {% if resultado is not none %}
    <div class="resultado">
Resultados:

x  = {{ x0 }}
y  = {{ y0 }}

z = x * y + 10
z = {{ z }}

x = x + 1
x = {{ x_final }}
    </div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    x = 0
    y = 0
    resultado = None
    z = None
    x_final = None
    x0 = None
    y0 = None

    if request.method == "POST":
        try:
            x_input = int(request.form.get("x", 0))
            y_input = int(request.form.get("y", 0))

            x0 = x_input
            y0 = y_input

            z = x0 * y0 + 10
            x_final = x0 + 1

            x = x0
            y = y0
            resultado = True
        except ValueError:
            resultado = None

    return render_template_string(HTML_TEMPLATE, x=x, y=y, resultado=resultado,
                                  z=z, x_final=x_final, x0=x0, y0=y0)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=False)
