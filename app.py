# coding=utf-8
import vk
import requests
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
access_token = os.environ["access_token"]
# your login and password, also requires app_id
session = vk.Session(access_token=access_token)
api = vk.API(session)
response = requests.get("https://api.vk.com/method/api.users.get?user_ids" +
                        "={}&fields=sex&access_token={}&v=5.56".format(target, access_token)).content[0]
if response["error"] is not None:
    print(response)
    raise Exception
# try:
#     target_info = api.users.get(user_ids=target, fields="sex")[0]
# except vk.exceptions.VkAPIError:
#     time.sleep(1)
#     response = requests.get("https://api.vk.com/method/api.users.get?user_ids" +
#                             "={}&fields=sex&access_token={}&v=5.56".format(target, access_token)).content
#     print(response)
#     raise
target_info = response[0]
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