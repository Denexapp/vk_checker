# vk_checker
## Description:
Vk checker module notifies you about changing status of a person in vk.com social network using messages.

## Requirements:
* Python 3
* Heroku account(it's free)
* Pastebin account (it's free too)

## Setting up:
* Create a new standalone app at vk.com/dev
* Generate access_token:
    * Take the following link, Replace YOUR_APP_ID by your actual app id from vk.com/dev and then open it in your browser.
    'https://oauth.vk.com/authorize?client_id=YOUR_APP_ID&scope=messages,offline&redirect_uri=http://api.vk.com/blank.html&display=page&response_type=token'
    * Grant access by pressing blue button, blank page with text "Do not copy address" should appear.
    * Extract access_token and keep it for a while. DO NOT SEND IT ANYONE.
* Create new paste at Pastebin with your account and remember the link to raw paste data.
* In Heroku create new python app, and deploy vk_checker, [more info]: https://devcenter.heroku.com/categories/deployment
* Add config vars:
    * Go to Settings > Config Variables > Reveal config vars
    * Add following vars:
        * 'access_token' = access_token_you_get_before
        * 'app_id' = your_app_id
        * 'listener' = id_of_person_who_will_be_receiving_notification
            numbers only, for example 'listener' = '12345'
        * 'target' = id_of_person_to_watch_status
            this should be in same format as 'listener'
        * 'captcha_solution_url' = url_to_paste_raw_data
            for example 'captcha_solution_url' = 'http://pastebin.com/raw/abcde'
* Running:
    * In Heroku open your app logs(in top right corner click More > View logs)
    * Open your paste at Pastebin and click edit
    * In another browser tab open page Resources on Heroku
    * Start(restart) 'worker'
    * Check logs until message 'Captcha img available at URL' will appear, if it will not appear in 2 minutes,
    then skip following steps.
    * Quickly follow the link, solve the captcha and put the answer in your paste, don't forget to save.
    * After 60 seconds script will try to get captcha solution from paste.
    * In short time listener should receive a message about status.

## Questions:
### Should i use cloud?
The script was designed for this purposes, clouds give opportunity to run script 24/7, not like on your pc.
But if you want to, feel free to rewrite script to launch it on your own pc, it requires python module named vk.

### Any troubles?
Just ask me any way you want
