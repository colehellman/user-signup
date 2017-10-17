from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('signup.html')

@app.route("/", methods=['get','post'])
def signup():
    user_error = ''
    pword_error = ''
    ver_error = ''
    email_error = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']
        if not val_input(username):
            user_error = "That does not seem to be a valid username"
        if not val_input(password):
            pword_error = "Invalid password"
        if password != verify:
            ver_error = "Passwords do not match"
        if not val_email(email):
            email_error = "Not a valid email"
        if user_error!='' or pword_error!='' or ver_error!='' or email_error!='':
            return render_template('signup.html', username=username,email=email,user_error=user_error,pword_error=pword_error,ver_error=ver_error,email_error=email_error)
        else:
            return render_template('success.html',username=username)

def val_input(string):
    length = len(string)
    if length<20 and length>3:
        if " " not in string:
            return True
    else:
        return False

def val_email(string):
    at_num = 0
    dot_num = 0
    if string =="":
        return True
    if val_input(string):
        for char in string:
            if char == '@':
                at_num+=1
            if char == '.':
                dot_num+=1
        if dot_num == 1 and at_num == 1:
            return True
        else:
            return False

if __name__ == '__main__':
    app.run()
