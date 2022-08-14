# BC-Menu-Bot

This bot uses the Twilio SMS API to recieve and send messages.

A user can send a message asking for a specific BC Dining Hall and the menu. The bot will web scrape the menu data and dynamically curate a specific message based off of the request. This provides the user with convenience as the BC Dining website is not very easy to use. 


In this example you can see the user requested the "Eagle's Nest" dining hall and the breakfast menu.
<img width="639" alt="Screen Shot 2022-08-14 at 2 38 26 PM" src="https://user-images.githubusercontent.com/99039782/184550506-c1839da9-09a2-4548-917f-2acd0988dad3.png">

In this example you can see that the bot recognized that the dining hall "Lower Live" was closed so it sent a message back alerting the user that it was closed for the day.

<img width="647" alt="Screen Shot 2022-08-14 at 2 40 45 PM" src="https://user-images.githubusercontent.com/99039782/184550590-8fbdce52-1278-45ef-b248-8956ce962f07.png">
