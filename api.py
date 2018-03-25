import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data
atten = [
    {'subid': 0,
     'subject': 'Computer org and Architecture',
     'attendance': 98},
    {'subid': 1,
     'subject': 'OOPS',
     'attendance': 97},
    {'subid': 2,
     'subject': 'Discrete Structures',
     'attendance': 99}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>My Attendance</h1>
<p>This is lower than you expect. :P </p>'''


@app.route('/api/nit/atten/all', methods=['GET'])
def api_all():
    return jsonify(atten)


@app.route('/api/nit/atten', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'subid' in request.args:
        id = int(request.args['subid'])
    else:
        return "Error: No subject id field provided. Please specify one"

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested subjectID.
    for att in atten:
        if att['subid'] == id:
            results.append(att)

    return jsonify(results)

app.run()
