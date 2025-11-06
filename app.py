from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'simple_key'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        session['user'] = name
        return redirect('/calendar')
    return '''
    <form method="post" style="text-align:center; margin-top:100px;">
      <h2>Study Calendar</h2>
      <input name="name" placeholder="Your Name" required style="padding:10px; width:200px;"><br><br>
      <button style="padding:10px 20px; background:#4a90e2; color:white; border:none;">Login</button>
    </form>
    '''

@app.route('/calendar')
def calendar():
    if 'user' not in session:
        return redirect('/')
    return render_template('calendar.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)