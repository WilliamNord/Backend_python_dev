from flask import Flask, render_template, request, redirect, url_for
from db import get_db
from security import encrypt, decrypt, cipher

app = Flask(__name__)

meldinger = []

@app.route("/")
def index():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, encrypted_data, created_at FROM secrets")
    rows = cursor.fetchall()

    conn.close()

    return render_template("secrets.html", rows=rows)

@app.route("/add", methods=["POST"])
def add():
    text = request.form["secret"]
    encrypted_text = encrypt(text)

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO secrets (encrypted_data) VALUES (%s)",
        (encrypted_text,)
    )
    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/dekryptert")
def dekryptert():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, encrypted_data, created_at FROM secrets")
    rows = cursor.fetchall()
    conn.close()

    decrypted_rows = []
    for row in rows:
        decrypted_text = decrypt(row[1])
        decrypted_rows.append((row[0], decrypted_text, row[2]))

    return render_template("dekryptert.html", rows=decrypted_rows)


@app.route("/om")
def om_oss():
    return render_template("om.html")

# @app.route("/gjestebok")
# def gjestebok():
#     return render_template("gjestebok.html", meldinger=meldinger)

# @app.route("/gjestebok/ny", methods=["POST"])
# def ny_melding():
#     navn = request.form["navn"]
#     melding = request.form["melding"]
#     meldinger.append({"navn": navn, "melding": melding})
#     return redirect(url_for("gjestebok"))   

if __name__ == "__main__":
    app.run(debug=True)