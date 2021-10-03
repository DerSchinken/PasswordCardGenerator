from PasswordCardGenerator import PasswordCard
from _thread import start_new_thread
from random import randint
from time import sleep
from flask import *
# ^ ik ik bad practice but i dont want a 300 mile long line
import logging
import os

host = "0.0.0.0"
port = 5000
clearing_time = 60 * 60

app = Flask(__name__)


# configure logging
logging.basicConfig(
    format="[%(asctime)s] - %(levelname)s - %(message)s",
    datefmt="%I:%M:%S %p",
    level=logging.DEBUG
)


@app.route("/", methods=['GET', 'POST'])
def index():
    password_len = request.form.get("password_length")
    npl = request.form.get("no_pwd_len", False)
    text = request.form.get("ascii", False)
    seed = request.form.get("seed")

    url = "generate?"
    if any((password_len, npl, text, seed)):
        if not password_len and not npl:
            error = "Password length was not given! (or no password card not activated)"
            return render_template("index.html", error=error)
        if password_len:
            if password_len.isdigit():
                if int(password_len) > 200:
                    error = "Your password length is to big!"
                    return render_template("index.html", error=error)
                url += f"password_length={password_len}&"
            else:
                error = "Password length has to be a number!"
                return render_template("index.html", error=error)
        if npl:
            url += "no_pwd_len=true&"
        if text:
            url += "ascii=true&"
        if seed:
            url += f"seed={seed}&"

        response = make_response(
            redirect(url),
            302,
        )

        return response

    return render_template("index.html")


@app.route("/generate", methods=['GET'])
def generate():
    password_len = request.args.get("password_length")
    npl = request.args.get("no_pwd_len", False)
    text = request.args.get("ascii", False)
    seed = request.args.get("seed")

    if not any((password_len, npl, text, seed)):
        abort(400)

    if password_len:
        if password_len.isdigit():
            if int(password_len) > 200:
                error = "Your password length is to big!"
                return make_response(
                    redirect("/"),
                    302,
                    {"error": error}
                )
        else:
            error = "Password length has to be a number!"
            return make_response(
                redirect("/"),
                302,
                {"error": error}
            )

    if npl and not password_len:
        password_len = 15

    code = f"PasswordCard({password_len}"
    if seed:
        code += f", seed={seed}"
    code += ")"
    card: PasswordCard = eval(code)

    if text:
        return render_template(
            "generate.html",
            text=str(card).replace("\n", "<br />"),
            txt="code",
            warning=""
        )

    filename = f"static/img/cards/card_{randint(1000, 100000000)}.png"
    while os.path.exists(filename):
        filename = f"static/img/cards/card_{randint(1000, 100000000)}.png"

    card.save_png(filename, background="#181818", font_color="white")

    return render_template("generate.html", filename=f"<img src='{filename}' alt='Oh there went something wrong. "
                                                     f"Please try again'>")


# run in thread
def clear_card_dir():
    while True:
        logging.info("Clearing Card directory")
        folder = 'static/img/cards/'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
            except Exception as e:
                logging.error('Failed to delete %s. Reason: %s' % (file_path, e))

        # wait 1h before clearing again
        sleep(clearing_time)


def run(new_port: int = port, debug: bool = False):
    start_new_thread(clear_card_dir, ())
    app.run(
        host=host,
        port=new_port,
        debug=debug,
    )


if __name__ == "__main__":
    start_new_thread(clear_card_dir, ())
    app.run(
        host=host,
        port=port,
        debug=True,
    )
