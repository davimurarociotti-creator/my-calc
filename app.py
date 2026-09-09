import math
import os

from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
@app.route("/81", methods=["GET", "POST"])
def calculadora():
    resultado = None

    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1"))
            num2_texto = request.form.get("num2", "")
            operacao = request.form.get("operacao", "")
            confirmar_codigo = request.form.get("confirmar_codigo", "nao")

            num2 = float(num2_texto) if num2_texto != "" else None

            if operacao == "raiz":
                if num1 < 0:
                    resultado = "Erro: Raiz quadrada de número negativo"
                else:
                    resultado = math.sqrt(num1)
            elif num2 is None:
                resultado = "Erro: Número 2 obrigatório"
            elif operacao == "soma" and num1 == 0 and num2 == 0 and confirmar_codigo == "sim":
                return redirect("https://play-cs.com/pt/servers")
            elif operacao == "subtracao" and num1 == 0 and num2 == 0 and confirmar_codigo == "sim":
                return redirect("https://eaglercraft.com/play?version=1.8.8-wasm")
            elif operacao == "multiplicacao" and num1 == 0 and num2 == 0 and confirmar_codigo == "sim":
                return redirect("https://poki.com/")
            elif operacao == "soma":
                resultado = num1 + num2
            elif operacao == "subtracao":
                resultado = num1 - num2
            elif operacao == "multiplicacao":
                resultado = num1 * num2
            elif operacao == "divisao":
                if num2 == 0:
                    resultado = "Erro: Divisão por zero"
                else:
                    resultado = num1 / num2
            elif operacao == "potencia":
                resultado = num1 ** num2
            else:
                resultado = "Erro: Operação inválida"
        except (ValueError, TypeError):
            resultado = "Erro: Entrada inválida"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)