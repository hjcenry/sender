import argparse
import json

from config import Config
import sender_factory

config = Config('config.ini')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='消息推送参数.')
    parser.add_argument('-st', '--send-type', type=str, default='4',
                        help='消息发送类型，可发送多个，以英文逗号分隔:1-邮件 2-markdown邮件 3-Server酱 4-WxPusher 5-WxPushV2')
    parser.add_argument('-u', '--user', type=str, help='接收人')
    parser.add_argument('-t', '--title', required=True, type=str, help='消息标题')
    parser.add_argument('-c', '--content', type=str, help='消息内容')
    parser.add_argument('-ct', '--content-type', type=str, help='消息类型：1-文本，2-HTML，3-Markdown')
    parser.add_argument('-token', '--token', type=str, help='token，针对需要token的发送处理')
    parser.add_argument('-url', '--url', type=str, help='详情url')
    parser.add_argument('--mail_name', type=str, help='邮件发送人名字（仅type包含1有效）')
    args = parser.parse_args()
    print(args)
    sender_types = args.send_type
    title = args.title
    content = args.content
    mail_name = args.mail_name
    user = args.user
    content_type = args.content_type
    api_token = args.token
    url = args.url
    for sender_type in sender_types.split(','):
        sender = sender_factory.SenderFactory.get_msg_sender(sender_type, mail_name=mail_name)
        if sender is not None:
            sender.send_msg(to_user=user, title=title, content=content, sender_type=content_type, api_token=api_token,
                            url=url)
            sender.quit()
