curl "http://0.0.0.0:5000"
wait
curl "http://0.0.0.0:5000" --cookie "_my_session_id=Hello"
wait
curl "http://0.0.0.0:5000" --cookie "_my_session_id=C is fun"
wait
curl "http://0.0.0.0:5000" --cookie "_my_session_id_fake"
