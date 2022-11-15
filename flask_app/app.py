from flask import Flask, request
import time
import string
import random
import os

app = Flask(__name__)


@app.route("/")
def index():
    hello_html = "<h1>Homework #4. Flask</h1>"
    links_html = """<ul>
        <li><a href="/whoami">Who Am I</a></li>
        <li><a href="/source_code">Soure Code</a></li>
        <li><a href="/random?length=42&specials=1&digits=0">Random</a></li>
    </ul>
    """
    html = f"{hello_html}{links_html}"
    return html


@app.route("/whoami")
def whoami():
    user_agent = request.headers.get('User-Agent')
    user_agent_html = f"<h4>User Agent: {user_agent}</h4>"

    ip_address = request.remote_addr
    ip_address_html = f"<h4>Your IP Address: {ip_address}</h4>"

    server_time = time.strftime("%d.%m.%Y %H:%M:%S")
    server_time_html = f"<h4>Server Time: {server_time}</h4>"

    back_html = "<br><br><a href='/'>Back</a>"

    html = user_agent_html + ip_address_html + server_time_html + back_html
    return html


@app.route("/source_code")
def source_code():
    header_html = f"<h4>Source Code</h4>"
    back_html = "<br><br><a href='/'>Back</a>"
    with open(__file__, 'r') as file:
        sc = file.read()
        sc_html = f"<pre>{sc}</pre>"
        html = header_html + sc_html + back_html
        return html


@app.route("/random")
def random_string():
    if not 'length' in request.values:
        return """<h1>length value must be in query params!</h1>
        <p>Example query params: ?length=8&specials=1&digits=1</p>
        """
    qvalues = request.values
    length = int(qvalues.get('length', 0))
    specials = int(qvalues.get('specials', 0))
    digits = int(qvalues.get('digits', 0))

    html = ""
    back_html = "<br><br><a href='/'>Back</a>"
    is_valid = True
    if not 1 <= length <= 100:
        html += "<h4 style='color:red;'>Length value must be a number between 1 and 100</h4>"
        is_valid = False
    if not 0 <= specials <= 1:
        html += "<h4 style='color:red;'>Specials value must be a number 0 or 1</h4>"
        is_valid = False
    if not 0 <= digits <= 1:
        html += "<h4 style='color:red;'>Digits value must be a number 0 or 1</h4>"
        is_valid = False
    if not is_valid:
        return html + back_html

    SPECIAL_SYMBOLS = "!\"№;%:?*()_+"
    DIGIT_SYMBOLS = "0123456789"

    possible_symbols = string.ascii_letters
    if digits:
        possible_symbols += DIGIT_SYMBOLS
    if specials:
        possible_symbols += SPECIAL_SYMBOLS
    possible_symbols = list(possible_symbols)
    result = ''.join(random.choice(possible_symbols) for _ in range(length))
    html = f"<h4>Your Random String: {result}</h4>"

    return html + back_html


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
