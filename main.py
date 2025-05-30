from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about.html')
def about():
    return render_template('about.html')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)