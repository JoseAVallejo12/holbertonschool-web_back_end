#!/usr/bin/env python3
""" 9-main """
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school
mongo_client = __import__('mongo_connect').mongo_client


if __name__ == "__main__":
    client = mongo_client()
    school_collection = client.Holberton.school
    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('address', "")))
