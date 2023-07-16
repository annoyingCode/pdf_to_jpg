import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def display_files():

    file_directory = "./static"

    jpg_files = [file for file in os.listdir(
        file_directory) if file.endswith('.jpg')]

    return render_template('index.html', jpg_files=jpg_files)


if __name__ == '__main__':
    app.run()
