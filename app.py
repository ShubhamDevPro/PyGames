from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main game page"""
    return render_template('index.html')

@app.route('/game')
def game():
    """Serve the game page"""
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True, port=5006)
