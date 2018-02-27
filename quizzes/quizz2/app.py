from flask import Flask, request, Response
import json

app = Flask(__name__)
l = {}

@app.route('/', methods = ['GET'])
def user():
    if request.method == 'GET':
        r = Response("OK")
        return str(r.status)+"\n"

@app.route('/users/<int:uid>', methods = ['POST'])
def users(uid):
    if request.method == 'POST':
        c = {"id":uid}
        l[uid] = json.dumps(request.get_json())
        d = {}
        for pair in str(l[uid]).replace('"','').split(','):
            k,v = pair.split(':')
            d[k[1:]] = v[1:-1]
        z = {**c, **d}
        l[uid] = z
        r = Response(status=201, mimetype='application/json')
        return str(r.status)+"\n"+str(z)+"\n"

@app.route('/users/<int:uid>', methods = ['GET'])
def user_id(uid):
    if request.method == 'GET':
        try:
            r = Response("OK")
            return str(r.status)+"\n"+str(l[uid])+"\n"
        except KeyError:
            r = Response(status=404, mimetype='application/json')
            return str(r.status)+"\nUser not found\n"

@app.route('/users/<int:uid>', methods = ['DELETE'])
def user_delete(uid):
    if request.method == 'DELETE':
        try:
            l.pop(uid)
            if bool(l):
                r = Response(status=206, mimetype='application/json')
                return str(r.status)+"\nUser Deleted\n"
            else:
                r = Response(status=204, mimetype='application/json')
                return str(r.status)+"\n"
        except KeyError:
            r = Response(status=404, mimetype='application/json')
            return str(r.status)+"\nUser not found\n"

if __name__ == '__main__':
    app.run(debug=True)