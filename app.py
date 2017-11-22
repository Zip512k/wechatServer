from flask import Flask, request, make_response
import hashlib

from resMessage import handleMessage, responseMessage

app = Flask(__name__)

@app.route('/')
def test():
    return 'Hello World!'

@app.route('/wechat', methods=['GET', 'POST'])
def weixin():
    if request.method == 'GET':
        if (request.args):
            secret = []
            token = "pandarealm"
            signature = request.args["signature"]
            timestamp = request.args["timestamp"]
            nonce = request.args["nonce"]
            echostr = request.args["echostr"]
            secret.append(token)
            secret.append(timestamp)
            secret.append(nonce)
            secret.sort()
            connectedStr = "".join(secret)
            sha1Str = hashlib.sha1(connectedStr)
            EncodedStr = sha1str.hexdigest()
            if signature == temp:
                return echostr
            else:
                return "Wrong App Token"
        else:
            return "Na Argument received"
    elif request.method == 'POST':
        xmlDict = handleMessage(request.data)
        reply = responseMessage(xmlDict)
        response = make_response(reply)
        response.content_type = 'application/xml'
        return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000,debug=True)
