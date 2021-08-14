curl "http://0.0.0.0:5000/api/v1/status"
wait
curl "http://0.0.0.0:5000/api/v1/auth_session/login" # not found but not "blocked" by an authentication system
wait
curl "http://0.0.0.0:5000/api/v1/users/me"
wait
curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh" # Won't work because the environment variable AUTH_TYPE is equal to "session_auth"
wait
curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=5535d4d7-3d77-4d06-8281-495dc3acfe76"
