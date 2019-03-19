from Task import Task
import time
from flask import Flask, request, jsonify
from db import Db
import json
from multiprocessing import Process

app = Flask(__name__)
db = Db()


def work():
    while True:
        starttime = time.time()
        try:
            r = db.all()
        except TypeError as e:
            print(e)
            return 1
        else:
            for entry in r:
                print("[TASK] : setting 'presence' for user " + entry['firstname'] + " " + entry['lastname'])
                Task(entry['on'], entry['off'], entry['firstname'], entry['lastname'])
            time.sleep(60.0 - ((time.time() - starttime) % 60.0))


@app.route('/')
def allentries():
    try:
        r = db.all()
    except TypeError as e:
        return e
    else:
        return json.dumps(r)


@app.route('/new', methods=['POST'])
def new():
    content = request.json
    if db.findfirst(content['firstname']) is None:
        return json.dumps({'failed': db.findfirst(content['firstname'])}), 400, {
            'ContentType': 'application/json'}

    db.newuser(content['firstname'], content['lastname'], content['on'], content['off'])

    if db.findfirst(content['firstname']) is not None:
        return json.dumps({'success': 'the user has been added to the tinyDB'}), 201, {
            'ContentType': 'application/json'}
    else:
        return json.dumps({'failed': 'ye fok up ya daft kun, ge get my some drank to teh bengah ya foker'}), 400, {
            'ContentType': 'application/json'}


if __name__ == '__main__':
    p = Process(target=work)
    p.start()
    app.run(debug=True, host='0.0.0.0')
    p.join()


