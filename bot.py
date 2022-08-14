from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from getMenuData import data
from makeResponse import response
from app import webhook_app

webhook_app = Flask(__name__)


@webhook_app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    outMess = response(incoming_msg, data)
    if len(outMess) > 1600:
        outMess = outMess[:1350] + \
            "...\n\n This message would be too long for the API to handle. If you want more info please select a specific meal time by including it in the message.\n E.g. \"Eagle's Nest Breakfast\""
    msg.body(outMess)
    return str(resp)


if __name__ == '__main__':
    webhook_app.run()
