import os
import sentry_sdk
from flask import Flask

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN", ""),
    traces_sample_rate=1.0,
)

app = Flask(__name__)

@app.route("/")
def index():
    return """<h1>Demo Shop</h1>
<p>Everything works, except... <a href="/checkout">checkout</a>.</p>
<button onclick="location.href='/checkout'">Checkout</button>"""

@app.route("/checkout")
def checkout():
    payment_methods = []
    if not payment_methods:
        return "No payment methods available", 400
    fee = 100 / len(payment_methods)
    return f"Checkout complete, fee: {fee}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
