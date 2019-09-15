import argparse

from config import Config
import sender_factory

config = Config('config.ini')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='消息推送参数.')
    parser.add_argument('-st', '--send-type', type=str, default='4',
                        help='消息发送类型，可发送多个，以英文逗号分隔:1-邮件 2-markdown邮件 3-Server酱 4-WxPusher')
    parser.add_argument('-u', '--user', type=str, help='接收人')
    parser.add_argument('-t', '--title', required=True, type=str, help='消息标题')
    parser.add_argument('-c', '--content', type=str, help='消息内容')
    parser.add_argument('--mail_name', type=str, help='邮件发送人名字（仅type包含1有效）')
    args = parser.parse_args()
    print(args)
    sender_types = args.send_type
    title = args.title
    content = args.content
    mail_name = args.mail_name
    user = args.user
    for sender_type in sender_types.split(','):
        sender = sender_factory.SenderFactory.get_msg_sender(sender_type, mail_name=mail_name)
        if sender is not None:
            sender.send_msg(title=title, content=content)
            sender.quit()
