#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
password_new = 'MyPwdOfBobujlk'
auth = Auth()

auth.register_user(email, password)
id_session = auth.create_session(email)
reset_token_pwd = auth.get_reset_password_token(email=email)
try:
    auth.update_password(reset_token=reset_token_pwd, password=password_new)
except Exception as e:
    print('no fue posible')
print(f'session id: {id_session}')
print(f'reset_token_pwd: {reset_token_pwd}')
# print(auth.get_user_from_session_id(auth.create_session(email)))
# print(auth.get_user_from_session_id(auth.create_session('dd')))
# auth.get_reset_password_token(email)
# print(auth.create_session("unknown@email.com"))
# auth.update_password(reset_token="32h32i3u", password="11232")
