from flask import Flask, render_template, redirect, url_for
import csv, urllib.request

app = Flask(__name__)


@app.route('/')
def main():
    results = []
    url = 'https://s3.amazonaws.com/rawstore.datahub.io/27e05e0885fe41e0d9dfa87e87892458.csv'
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)

    for row in cr:
        results.append(row)

    return render_template('index.html', 'news.html', 'support.html','table.html', results=results)
