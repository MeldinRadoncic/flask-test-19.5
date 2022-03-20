from boggle import Boggle
from flask import Flask , request ,render_template , session

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mynameismeldin'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False



@app.route("/")
def homepage():
    """Show board."""

    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    return render_template("index.html", board=board, highscore=highscore, nplays=nplays)


@app.route("/post-score", methods=["POST"])
def post_score():
    """Receive score, update nplays, update high score if appropriate."""
    score = request.json["score"]
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)
    session['nplays'] = nplays + 1
    session['highscore'] = max(score, highscore)
    return jsonify(brokeRecord=score > highscore)