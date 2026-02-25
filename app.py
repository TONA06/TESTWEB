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
<html>
<head>
    <title>Vận mệnh hôm nay</title>
</head>
<body style="text-align:center; font-family:Arial;">
    <h1>🔮 Bói vận mệnh hôm nay 🔮</h1>
    <form method="post">
        <input type="text" name="name" placeholder="Nhập tên bạn" required>
        <button type="submit">Xem ngay</button>
    </form>

    {% if result %}
        <h2>Xin chào {{name}}!</h2>
        <h3>{{result}}</h3>
    {% endif %}
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

if __name__ == "__main__":
    app.run(debug=True)