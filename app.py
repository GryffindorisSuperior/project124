from flask import Flask

#constructor of class Flask
app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'name': u'Person 1',
        'number': u'1234567890',
        'done': False
    },

    {
        'id': 2,
        'name': u'Person 2',
        'number': u'0987654321',
        'done': False
    }
]

#defining route code
@app.route("/")
def hello_world():
    return "Hello World"

# check data (if no data, give 400 error)
@app.route("/add-data", methods = ["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data"
        }, 400)

    task = {
        "id": contacts[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status": "Success!",
        "message": "Contact added successfully!"
    })

@app.route("/get-data")
def get_contact():
    return jsonify({
        "data": contacts
    })

#run web app
if __name__ == '__main__':
    app.run()

# http = HyperText Transfer Protocol
# get function gets data from a specified source (default methods used by Flask)
# post function sends data to the server to create/update a resource (multiple copies of same resource).
# put function (one copy of the resource). 
# delete function deletes a resource.