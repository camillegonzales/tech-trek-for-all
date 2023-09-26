from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user)) #redirect user to page telling them submission was successful
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)