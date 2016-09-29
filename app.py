# coding=utf-8
import vk
import time
import os
import requests


def handle_captcha(function, *args, **kwargs):
    try:
        return function(*args, **kwargs)
    except vk.exceptions.VkAPIError as e:
        sid = e.captcha_sid
        img = e.captcha_img
        print("Captcha img available at {}".format(img))
        time.sleep(60)
        key = requests.get(os.environ["captcha_solution_url"]).content
        print("Captcha key is {}".format(key))
        return function(*args, **kwargs, captcha_key=key, captcha_sid=sid)


def get_status(target):
    try:
        return handle_captcha(api.users.get, user_ids=target, fields="status")[0]["status"]
    except requests.exceptions.ReadTimeout:
        return old_status


def send_message(message, target):
    handle_captcha(api.messages.send, user_id=target,
                      message=message, v="4.104")

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
session = vk.Session(access_token=access_token)
api = vk.API(session)
target_info = handle_captcha(api.users.get, user_ids=target, fields="sex")[0]
target_name = target_info["first_name"] + " " + target_info["last_name"]
target_gender = target_info["sex"] == 1
print(target_info)
time.sleep(3)
old_status = None
while True:
    status = get_status(target)
    if status != old_status:
        old_status = status
        time.sleep(3)
        send_message("{} изменил{} свой статус на \"{}\"".format(target_name, "а" if target_gender else "", status), listener)
        time.sleep(7)
    else:
        time.sleep(10)
