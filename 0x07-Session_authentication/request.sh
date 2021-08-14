curl "http://0.0.0.0:5000/api/v1/status"
wait
curl "http://0.0.0.0:5000/api/v1/status/"
wait
curl "http://0.0.0.0:5000/api/v1/users"
wait
curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
