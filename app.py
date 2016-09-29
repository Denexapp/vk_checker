# coding=utf-8
import vk
import time
import random
import os
import requests

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
access_token = os.environ["access_token"]
# your login and password, also requires app_id
session = vk.Session(access_token=access_token)
api = vk.API(session)
target_info = None
try:
    target_info = api.users.get(user_ids=target, fields="sex")[0]
except vk.exceptions.VkAPIError as e:
    time.sleep(1)
    sid = e.captcha_sid
    img = e.captcha_img
    print("Captcha img available at {}".format(img))
    time.sleep(60)
    key = requests.get(os.environ["captcha_solution_url"]).content
    print("Captcha key is {}".format(key))
    target_info = api.users.get(user_ids=target, fields="sex", captcha_key=key, captcha_sid=sid)[0]
target_name = target_info["first_name"] + " " + target_info["last_name"]
target_gender = target_info["sex"] == 1
print(target_info)
old_status = None
while True:
    status = get_status(target)
    if status != old_status:
        old_status = status
        send_message("{} изменил{} свой статус на \"{}\"".format(target_name, "а" if target_gender else "", status), listener)
    time.sleep(10)