from flask import Flask, request, flash, render_template, redirect, url_for
import string
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pqKsBMgJoNZRueiuhCOm'

@app.route('/', methods = ["GET", "POST"])
def generatePass():
    characters = ""
    use_password = ""
    if request.method == "POST":
        # get password length
        length = request.form.get('length')
        lengths = int(length)

        # get password condition
        use_lowercase = True if request.form.get('lowercase') else False
        use_uppercase = True if request.form.get('uppercase') else False
        use_numbers = True if request.form.get('numbers') else False
        use_symbols = True if request.form.get('symbols') else False

        if lengths > 0:
            if not any([use_lowercase, use_uppercase, use_numbers, use_symbols]):
                flash("ERROR PLEASE CHOOSE AT LEAST ONE SETTING")
                return redirect(url_for('generatePass'))
            else:
                if use_lowercase:
                    characters += string.ascii_lowercase
                if use_uppercase:
                    characters += string.ascii_uppercase
                if use_numbers:
                    characters += string.digits
                if use_symbols:
                    characters += string.punctuation
                
                use_password = ''.join(random.choice(characters) for i in range(lengths))
        else:
            flash("ERROR PLEASE CHOOSE MORE THAN 0 LENGTH")
            return redirect(url_for('generatePass'))

    return render_template('index.html', user_password = use_password)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)