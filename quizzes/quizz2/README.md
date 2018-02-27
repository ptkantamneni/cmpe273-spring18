### How to Setup

```sh
virtualenv my-venv
. my-venv/bin/activate
pip3 install -r requirements.txt
```

### How to run?
```sh
python app.py
```

### GET /

```sh
curl -i http://127.0.0.1:5000/
```

### POST users

```sh
curl -X POST http://localhost:5000/users/1 -H 'Cache-Control: no-cache' -H 'Content-Type: application/json' -d '{"name":"foo"}'
```

__Response__

```sh
HTTP/1.0 201 Created
...
{
    "id": 1,
    "name": "foo"
}
```

### GET users

```sh
curl -X GET http://localhost:5000/users/1 -H 'Cache-Control: no-cache' -H 'Content-Type: application/json' 
```

__Response__

```sh
HTTP/1.0 200 OK
...
{
    "id": 1,
    "name": "foo"
}
```

### DELETE users

```sh
curl -X DELETE http://localhost:5000/users/1 -H 'Cache-Control: no-cache' -H 'Content-Type: application/json'
```

__Response__

```sh
HTTP/1.0 204 No Content
...
```
