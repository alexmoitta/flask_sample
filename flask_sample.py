# curl -H "Content-Type: application/json" -X POST -d@body.json localhost:5000/transform/1
# $ cat body.json
# {"name":"santos"}
# curl localhost:5000/transform/1
# Gleicon Moraes (https://github.com/gleicon) has made it!!!


from flask import Flask,request

app = Flask(__name__)

all_jsons = {}

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/transform/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.get_json()

    if request.method == "POST":
        all_jsons[uuid] = content
        return str(content)
    else:
        return str(all_jsons.get(uuid, ""))


if __name__ == "__main__":
    app.debug = True
    app.run()
