import json
import requests

import sender
from msg_sender import MsgSender


class WxPusherV2(MsgSender):
    """
    微信推送服务V2
    接口文档：http://wxpusher.zjiecode.com/docs
    支持一对多推送
    支持HTML语法
    支持MD语法
    """

    def __init__(self):
        pass

    def send_msg(self, to_user=None, title=None, content=None, **kwargs):
        """
        WxPusher发送文本消息
        :param to_user: 接收用户的ID，多个用户ID请用英文半角逗号分隔开。就是关注号，发送给你的那个ID。
        :param title: 标题
        :param content: 内容
        :param kwargs: token 应用token, type 1-文本消息 2-HTML消息 3-MD消息, url 详情url
        :return:
        """
        if to_user is None:
            to_user = sender.config.get_config('ids', 'wx_pusher_v2')
        if content is None:
            content = title
        token = kwargs['api_token'] if 'api_token' in kwargs and kwargs[
            'api_token'] is not None else sender.config.get_config('api_token', 'wx_pusher_v2')
        push_type = kwargs['sender_type'] if 'sender_type' in kwargs and kwargs[
            'sender_type'] is not None else 1
        url = "http://wxpusher.zjiecode.com/api/send/message"
        detail_url = kwargs['url'] if 'url' in kwargs else None
        data = {
            "appToken": token,
            "content": content,
            "contentType": push_type,  # 内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown
            # topicIds开发未完成
            # "topicIds": [  # 发送目标的topicId，是一个数组！！！
            #     123
            # ],
            "uids": to_user.split(',')  # 发送目标的UID，是一个数组！！！
        }
        headers = {
            "Content-Type": "application/json"
        }
        if detail_url is not None:
            data["url"] = detail_url  # 原文链接，可选参数

        response = requests.post(url, data=json.dumps(data), headers=headers)
        result = json.loads(response.text)
        code = result['code']
        if code != 1000:
            print("Wx Pusher V2 Err - response[%s]" % response.text)
            return False
        return True
