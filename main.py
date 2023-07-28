from flask import Flask, jsonify, request
import csv

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader) 
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)
@app.route('/get-article')

def get_article():
    return jsonify({
        'data': all_articles[0],
        'status': 'success',
    })

@app.route('/liked_article', methods=['POST'])

def liked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        'status': 'success'
    })

@app.route('/not_liked_articles', methods=['POST'])

def not_liked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        'status': 'success'
    })

if __name__ == "__main__":
    app.run()

