# coding=utf-8
import vk
import time
import random
import os


def get_status(target):
    response = api.users.get(user_ids=target, fields="status")[0]
    return response["status"]


def send_message(message, target):
    api.messages.send(peer_id=target, random_id=random.randint(0, 1024),
                      message=message, v="5.53")

# you should define vars in your environment
# or simply replace os.environ() calls
# by actual values

# there should be id of people, example:
# target = 12345
# listener = 54321
target = os.environ['target']
listener = os.environ['listener']
target = "id" + str(target)
# your login and password, also requires app_id
print("authorization in progress, app_id is {}, login is {}, password is {}".format(os.environ['app_id'],
                                                                                    os.environ['login'],
                                                                                    os.environ['password']))
try:
    session = vk.AuthSession(app_id=os.environ['app_id'],
                             user_login=os.environ['login'],
                             user_password=os.environ['password'],
                             scope=4096)
except Exception as e:
    print(e, e.args)
    raise
print("authorization completed")
api = vk.API(session)
target_info = api.users.get(user_ids=target, fields="sex")[0]
target_name = target_info["first_name"] + " "+ target_info["last_name"]
target_gender = target_info["sex"] == 1
print(target_info)
old_status = None
while True:
    status = get_status(target)
    if status != old_status:
        old_status = status
        send_message("{} изменил{} свой статус на \"{}\"".format(target_name, "а" if target_gender else "", status), listener)
    time.sleep(10)