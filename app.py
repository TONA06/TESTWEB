from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

messages = [
    "Hôm nay bạn gặp may mắn 🍀",
    "Cẩn thận mất tiền 😏",
    "Có người đang nhớ bạn ❤️",
    "Code hôm nay không bug đâu 😎",
    "Người yêu tương lai đang đến gần 👀"
]

html = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Vận mệnh hôm nay</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #1e1e2f, #3a3a5f);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: white;
        }

        .card {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(10px);
            padding: 40px;
            border-radius: 20px;
            width: 400px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            animation: fadeIn 0.8s ease-in-out;
        }

        h1 {
            margin-bottom: 20px;
            font-weight: 700;
        }

        input {
            width: 80%;
            padding: 12px;
            border-radius: 10px;
            border: none;
            outline: none;
            margin-bottom: 15px;
            font-size: 14px;
        }

        button {
            padding: 12px 25px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            background: #ff4b8b;
            color: white;
            font-weight: bold;
            transition: 0.3s;
        }

        button:hover {
            background: #ff2e73;
            transform: scale(1.05);
        }

        .result {
            margin-top: 25px;
            font-size: 18px;
            font-weight: 500;
            animation: pop 0.5s ease;
        }

        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(20px);}
            to {opacity: 1; transform: translateY(0);}
        }

        @keyframes pop {
            from {transform: scale(0.8);}
            to {transform: scale(1);}
        }

        footer {
            margin-top: 20px;
            font-size: 12px;
            opacity: 0.6;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🔮 Bói vận mệnh hôm nay</h1>

        <form method="post">
            <input type="text" name="name" placeholder="Nhập tên của bạn..." required>
            <br>
            <button type="submit">Xem vận mệnh</button>
        </form>

        {% if result %}
            <div class="result">
                <p>Xin chào <b>{{name}}</b> 👋</p>
                <p>{{result}}</p>
            </div>
        {% endif %}

        <footer>
            ✨ Powered by Flask ✨
        </footer>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    name = ""
    if request.method == "POST":
        name = request.form["name"]
        result = random.choice(messages)
    return render_template_string(html, result=result, name=name)
import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))


