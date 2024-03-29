import sender
from mail_def import MailServer
from mail_server_md import MailMdSender
from mail_server_smtp import MailSmtpSender
from server_chan import ServerChan
from wx_pusher import WxPusher
from wx_pusher_v2 import WxPusherV2


class SenderType(object):
    MAIL_SMTP = 1
    MAIL_MD = 2
    SERVER_CHAN = 3
    WX_PUSHER = 4
    WX_PUSHER_V2 = 5


class SenderFactory(object):

    @staticmethod
    def get_msg_sender(sender_type: SenderType, **kwargs):
        """
        获取消息发送接口
        :param sender_type:
        :param kwargs:
        :return:
        """
        mail_from_addr = sender.config.get_config('mail_from_addr', 'mail')
        mail_pwd = sender.config.get_config('mail_pwd', 'mail')
        mail_server = eval(sender.config.get_config('mail_server', 'mail'))
        if int(sender_type) is SenderType.MAIL_SMTP:
            return MailSmtpSender(mail_from_addr, kwargs['mail_name'], mail_pwd, mail_server)
        elif int(sender_type) is SenderType.MAIL_MD:
            return MailMdSender(mail_from_addr, mail_pwd, mail_server)
        elif int(sender_type) is SenderType.SERVER_CHAN:
            return ServerChan()
        elif int(sender_type) is SenderType.WX_PUSHER:
            return WxPusher()
        elif int(sender_type) is SenderType.WX_PUSHER_V2:
            return WxPusherV2()
        else:
            return None
