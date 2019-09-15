## sender
消息推送服务
包含以下参数：

usage: sender.py [-h] [-st SEND_TYPE] [-u USER] -t TITLE [-c CONTENT]
                 [--mail_name MAIL_NAME]

消息推送参数.

optional arguments:
  -h, --help            show this help message and exit
  -st SEND_TYPE, --send-type SEND_TYPE
                        消息发送类型，可发送多个，以英文逗号分隔:1-邮件 2-markdown邮件 3-Server酱
                        4-WxPusher
  -u USER, --user USER  接收人
  -t TITLE, --title TITLE
                        消息标题
  -c CONTENT, --content CONTENT
                        消息内容
  --mail_name MAIL_NAME
                        邮件发送人名字（仅type包含1有效）

### 目前实现的消息推送有以下几种类型：
1. 邮件 
2. markdown邮件 
3. Server酱
4. WxPusher
