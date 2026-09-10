<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora</title>
    <style>
        * { box-sizing: border-box; }
        body {
            margin: 0;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #0f172a, #1e293b);
            color: #e2e8f0;
        }
        .card {
            width: min(92vw, 480px);
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(148, 163, 184, 0.25);
            border-radius: 22px;
            padding: 30px 28px;
            box-shadow: 0 20px 45px rgba(0,0,0,0.4);
        }
        h1 {
            margin: 0 0 20px;
            text-align: center;
            color: #f8fafc;
            font-size: 2rem;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        label {
            font-weight: 700;
            color: #cbd5e1;
        }
        input, select {
            width: 100%;
            padding: 12px 14px;
            border-radius: 12px;
            border: 1px solid #475569;
            background: #0f172a;
            color: #f8fafc;
            font-size: 1rem;
        }
        .buttons {
            display: flex;
            gap: 12px;
            margin-top: 6px;
        }
        .btn {
            flex: 1;
            border: none;
            border-radius: 14px;
            padding: 14px 18px;
            font-size: 1rem;
            font-weight: 700;
            cursor: pointer;
            transition: 0.15s ease;
        }
        .btn-calc {
            background: linear-gradient(135deg, #38bdf8, #2563eb);
            color: white;
            box-shadow: 0 12px 20px rgba(37, 99, 235, 0.35);
        }
        .btn-clear {
            background: linear-gradient(135deg, #64748b, #475569);
            color: white;
            box-shadow: 0 12px 20px rgba(71, 85, 105, 0.3);
        }
        .resultado {
            margin-top: 22px;
            padding: 14px 16px;
            text-align: center;
            border-radius: 12px;
            font-weight: 700;
            background: rgba(34, 197, 94, 0.12);
            border: 1px solid rgba(34, 197, 94, 0.4);
            color: #bbf7d0;
        }
        .erro {
            background: rgba(239, 68, 68, 0.12);
            border-color: rgba(239, 68, 68, 0.4);
            color: #fecaca;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Calculadora</h1>

        <form id="calcForm" method="POST" action="/">
            <input type="hidden" name="confirmar_codigo" id="confirmar_codigo" value="nao">
            <div>
                <label for="num1">Número 1:</label>
                <input type="number" step="any" name="num1" required>
            </div>

            <div>
                <label for="operacao">Operação:</label>
                <select name="operacao" required>
                    <option value="soma">Soma</option>
                    <option value="subtracao">Subtração</option>
                    <option value="multiplicacao">Multiplicação</option>
                    <option value="divisao">Divisão</option>
                    <option value="potencia">Potência</option>
                    <option value="raiz">Raiz Quadrada</option>
                </select>
            </div>

            <div>
                <label for="num2">Número 2:</label>
                <input type="number" step="any" name="num2" id="num2" required>
            </div>

            <div class="buttons">
                <button class="btn btn-calc" type="submit">Calcular</button>
                <button class="btn btn-clear" type="button" onclick="limparFormulario()">Limpar</button>
            </div>
        </form>

        {% if resultado is not none %}
            <div class="resultado{% if resultado is string and resultado.startswith('Erro:') %} erro{% endif %}">
                Resultado: {{ resultado }}
            </div>
        {% endif %}

    </div>

    <script>
        const operacao = document.querySelector("select[name='operacao']");
        const num1 = document.querySelector("input[name='num1']");
        const num2 = document.getElementById("num2");
        const form = document.getElementById("calcForm");
        const confirmarCodigo = document.getElementById("confirmar_codigo");

        function limparFormulario() {
            const form = document.getElementById("calcForm");
            form.reset();
            confirmarCodigo.value = "nao";
            ajustarNum2();
        }

        function ajustarNum2() {
            const raizSelecionada = operacao.value === "raiz";
            num2.disabled = raizSelecionada;
            num2.required = !raizSelecionada;
            if (raizSelecionada) {
                num2.value = "";
            }
        }

        function codigoSecretoDetectado() {
            if (operacao.value !== "soma" && operacao.value !== "subtracao" && operacao.value !== "multiplicacao") {
                return false;
            }

            const valor1 = parseFloat(num1.value);
            const valor2 = parseFloat(num2.value);
            return valor1 === 0 && valor2 === 0;
        }

        form.addEventListener("submit", function (event) {
            if (codigoSecretoDetectado()) {
                const desejaUsarCodigo = window.confirm("Você quer usar o código secreto?");
                if (!desejaUsarCodigo) {
                    event.preventDefault();
                    confirmarCodigo.value = "nao";
                } else {
                    confirmarCodigo.value = "sim";
                }
            }
        });

        operacao.addEventListener("change", ajustarNum2);
        ajustarNum2();
    </script>
</body>
</html>
