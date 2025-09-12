from flask import Flask, request, render_template

app = Flask(__name__)

# Route for home page
@app.route("/")
def home():
    return render_template("index.html")

# Route for your form submission
@app.route("/form", methods=["GET"])
def handle_form():
    # Get all form values
    major = request.args.get('major', '')
    advisor = request.args.get('advisor', '')
    room = request.args.get('room', '')
    time = request.args.get('time', '')
    fullabstract = request.args.get('fullabstract', '')
    posters = request.args.get('posters', '')

    firstname = request.args.get('firstname', '')
    lastname = request.args.get('lastname', '')
    wordsintitle = request.args.get('wordsintitle', '')
    wordsinabstract = request.args.get('wordsinabstract', '')

    # Render template with variables
    return render_template(
        "form_results.html",
        major=major,
        advisor=advisor,
        room=room,
        time=time,
        fullabstract=fullabstract,
        posters=posters,
        firstname=firstname,
        lastname=lastname,
        wordsintitle=wordsintitle,
        wordsinabstract=wordsinabstract
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
