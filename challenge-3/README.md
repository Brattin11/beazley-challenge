# File based API

### Running the server
`python3 -m flask run`

To run this in the cloud, I'd probably set up an AWS or Google Cloud instance
and use GitHub Actions for automated testing and deployment. 

### Mock Data - add this to `database.json` for testing purposes
`[{"80": "Apache"}, {"443": "nginx"}, {"8080": "Apache Tomcat"}]`

### Curls

```
curl -X GET http://127.0.0.1:5000/api/data
```

```
curl -X POST http://127.0.0.1:5000/api/data/create \
     -H "Content-Type: application/json" \
     -d '{"8088": "Litespeed web server"}'
```

```
curl -X DELETE http://127.0.0.1:5000/api/data/delete/443 \
     -H "Content-Type: application/json" 
```

```
curl -X PUT http://127.0.0.1:5000/api/data/update/443 \
     -H "Content-Type: application/json" \
     -d '{"443": "nginx2"}'
```

### Unit testing

`python3 -m pytest`

Note: ensure `database.json` has the contents `[]` before running tests.


