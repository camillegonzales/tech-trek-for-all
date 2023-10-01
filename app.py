from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
# client = MongoClient("mongodb://username:password@cluster.mongodb.net/database")
# db = client.mydatabase
# collection = db.survey_data

@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/mentee-survey")
def mentee_signup():
    return render_template("mentee-survey.html")


@app.route("/mentor-survey")
def mentor_signup():
    return render_template("mentor-survey.html")


@app.route('/success/<name>')
def success(name):
    return 'Submission successful!'


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user)) #redirect user to a page telling them submission was successful
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)
