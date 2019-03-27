#!/usr/bin/python3
from Task import Task
import time
import datetime
from flask import Flask, request, jsonify
from db import Db
import json
from multiprocessing import Process
import logging

app = Flask(__name__)
db = Db()


def work():
    while True:
        if datetime.datetime.today().weekday() < 5:
            starttime = time.time()
            try:
                r = db.all()
            except TypeError as e:
                print(e)
                return 1
            else:
                for entry in r:
                    print(time.strftime("%H:%M:%S ") + "[TASK] : setting 'presence' for user " + entry[
                        'firstname'] + " " +
                          entry['lastname'])
                    Task(entry['on'], entry['off'], entry['firstname'], entry['lastname'], entry['password'])
                time.sleep(60.0 - ((time.time() - starttime) % 60.0))
        else:
            print(datetime.datetime.today().weekday())
            time.sleep(120)


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
    if db.findUser(content['lastname'], content['firstname']) is None:
        return json.dumps({'failed': db.findUser(content['firstname'], content['lastname'])}), 400, {
            'ContentType': 'application/json'}

    db.newuser(content['firstname'], content['lastname'], content['password'], content['on'], content['off'])

    if db.findUser(content['lastname'], content['firstname']) is not None:
        return json.dumps({'success': 'the user has been added to the tinyDB'}), 201, {
            'ContentType': 'application/json'}
    else:
        return json.dumps({'failed': 'ye fok up ya daft kun, ge get my some drank to teh bengah ya foker'}), 400, {
            'ContentType': 'application/json'}


@app.route('/<lastname>/<firstname>', methods=['DELETE'])
def delete(lastname, firstname):
    if db.findUser(lastname, firstname) is None:
        return json.dumps({'failed': db.findUser(lastname, firstname)}), 400, {
            'ContentType': 'application/json'}
    elif db.findUser(lastname, firstname) is not None:
        db.remove(lastname, firstname)
        return json.dumps({'success': 'the user has been deleted from the tinyDB'}), 201, {
            'ContentType': 'application/json'}


@app.route('/<lastname>/<firstname>', methods=['PUT'])
def edit(lastname, firstname):
    content = request.json
    if 'on' in content:
        db.update(firstname, lastname, 'on', content['on'])
    if 'off' in content:
        db.update(firstname, lastname, 'off', content['off'])
    return json.dumps({'success': db.findUser(lastname, firstname)}), 201, {
        'ContentType': 'application/json'}


if __name__ == '__main__':
    p = Process(target=work)
    p.start()
    app.run(debug=True, host='0.0.0.0')
    p.join()
