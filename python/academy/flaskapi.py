#!/usr/bin/env python

import json

from flask import Flask, Response

app = Flask(__name__)


def get_course_data():
    courses = {'Linux': 'LPIC-1', 'AWS': "Devops Pro"}
    return courses


courses = get_course_data()


@app.route('/')
def information():
    return """ This application gives information about the Linux Academy courses 
    by webscrapping and returning the output as JSON """


@app.route('/course')
def all_courses():
    js = json.dumps(courses, sort_keys=True, indent=4)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

