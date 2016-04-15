# Python & Docker API playground

## Usage

To launch the service
```bash
# On a Mac you might need to populate docker's environment variables
$ eval $(docker-machine env)

# Launch your service
python3 server.py
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Then simply execute HTTP requests against the service.

## Endpoints

### GET /containers
Return a list of all the known containers
```bash
curl http://127.0.0.1:5000/containers
```

And you'll get something like
```json
[
	{
		"Status": "Up 10 minutes",
		"Id": "4391ad187af1851641d0a48583c6d1166e8e79279a4bad319883dfa3c3f06a15",
		"Image": "ubuntu"
	}
]
```

### GET /containers/id
Return aditional information about a specific container
```bash
curl http://127.0.0.1:5000/containers/4391ad187af1
```

```json
{
	"Id": "4391ad187af1851641d0a48583c6d1166e8e79279a4bad319883dfa3c3f06a15",
	"State": {
		"Error": "",
		"ExitCode": 0,
		"Status": "running",
		"OOMKilled": false,
		"FinishedAt": "2016-04-15T02:17:40.281574062Z",
		"StartedAt": "2016-04-15T02:17:50.333913649Z",
		"Running": true,
		"Paused": false,
		"Pid": 5215,
		"Dead": false,
		"Restarting": false
	}
}
```

### POST /containers/id/start
Starts the container
```bash
curl -i --data "" http://127.0.0.1:5000/containers/4391ad187af1/start
```

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 0
Server: Werkzeug/0.11.7 Python/3.5.1
Date: Fri, 15 Apr 2016 02:32:45 GMT

```

### POST /containers/id/stop
Stops the container

```bash
curl -i --data "" http://127.0.0.1:5000/containers/4391ad187af1/stop
```

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 0
Server: Werkzeug/0.11.7 Python/3.5.1
Date: Fri, 15 Apr 2016 02:32:45 GMT

```
