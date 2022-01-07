import flask
import json

app = flask.Flask(__name__)

with open('data.json') as f:
    data = json.loads(f.read())


@app.route('/', methods=['GET'])
def choose_lang():
    print(list(data.keys()))
    length = len(list(data.keys()))
    languages = list(data.keys())
    return flask.render_template('choose_lang.html', data=data)


@app.route('/choose_genre')
def return_genre_page():
    lang = flask.request.args.get('language')

    if lang:
        genres = data[lang]
        return flask.render_template('choose genre.html', genres=genres, lang=lang)
    else:
        return 'That page doesn\'t exist, sorry :('


@app.route('/choose_song')
def return_song_page():
    genre = flask.request.args.get('genre')
    language = flask.request.args.get('language')
    songs = data[language][genre]
    print(songs)
    return flask.render_template('choose_song.html', songs=songs)


app.run('0.0.0.0', port=8080)
