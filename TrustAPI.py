from flask import Flask, jsonify, request
import requests
import time


app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'value': u'test'
    }
]
def get_username(user):
    #When function is called. Send signal that new score needs to be calculated.
    print("passed user: %s" %user)

def pass_score(score):

    headers = {
        'Content-Type': 'application/json'
    }

    data = '{"value": "%s"}' %score

    return requests.put('http://192.168.1.103:5000/2', headers=headers, data=data)


@app.route('/<int:task_id>', methods=['GET', 'PUT'])
def update_task(task_id):

    if request.method == 'GET':

        return jsonify({'tasks': tasks})


    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)

    tasks[0]['value'] = request.json.get('value', tasks[0]['value'])
    get_username(tasks[0]['value'])
    #time.sleep(5)
    return jsonify({'tasks': tasks[0]})

time.sleep(5)
pass_score(95)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(host='192.168.1.103', port=5001, debug=True)

#Query Command
# curl -i -H "Content-Type: application/json" -X PUT -d "{\"JWT\":\"VALUE\"}" http://localhost:5000/1

# curl -i http://localhost:5000/1


