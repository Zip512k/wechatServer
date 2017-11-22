import time
import xml.etree.ElementTree as ET

def handleMessage(oriData):
    xmldata = ET.fromstring(oriData)
    fromUserName = xmldata.find("FromUserName").text
    toUserName = xmldata.find("ToUserName").text
    content = xmldata.find("Content").text
    xmlDict = {"FromUserName": fromUserName,"ToUserName": toUserName, "Content": content}
    return xmlDict

def responseMessage(content_dict={"": ""}, type="text"):
    toName = content_dict["FromUserName"]
    fromName = content_dict["ToUserName"]
    resContent = "Sorry, this account is under development."
    reply = """
    <xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[%s]]></Content>
        <FuncFlag>0</FuncFlag>
    </xml>
	"""
    resStr = reply % (toName, fromName, int(time.time()), resContent)
    return resStr