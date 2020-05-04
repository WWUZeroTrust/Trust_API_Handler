from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'JWT': u'test'
    }
]
#Need to implement PUT. The Handler will pass JWT here.
@app.route('/todo/api/v1.0/tasks', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'JWT' in request.json and type(request.json['JWT']) != unicode:
        abort(400)
    
    tasks[0]['JWT'] = request.json.get('JWT', tasks[0]['JWT'])
    return jsonify({'tasks': tasks[0]})