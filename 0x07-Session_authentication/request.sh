curl "http://0.0.0.0:5000/"
wait
curl "http://0.0.0.0:5000/" --cookie "_my_session_id=Holberton"
wait
curl "http://0.0.0.0:5000/" --cookie "_my_session_id=9d1648aa-da79-4692-8236-5f9d7f9e9485"

