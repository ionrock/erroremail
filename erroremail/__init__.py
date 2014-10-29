# -*- coding: utf-8 -*-
__author__ = 'Eric Larson'
__email__ = 'eric@ionrock.org'
__version__ = '0.1.0'

import cgitb
import smtplib
import traceback

from cStringIO import StringIO
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class ErrorEmail(object):

    def __init__(self, config):
        self.config = config

    def __enter__(self):
        return self

    def send_email(self, message):
        server = smtplib.SMTP(self.config['SERVER'],
                              self.config.get('PORT', 25))
        to = self.config['TO']
        frm = self.config['FROM']
        server.sendmail(to, frm, message)
        server.quit()

    def get_plain_traceback(self, exc_info):
        fh = StringIO()
        traceback.print_tb(exc_info[2], fh)
        return MIMEText(fh.getvalue(), 'plain')

    def get_html_traceback(self, exc_info):
        return MIMEText(cgitb.html(exc_info), 'html')

    def create_message_from_traceback(self, exc_info):
        msg = MIMEMultipart('alternative')

        msg['To'] = ', '.join(self.config['TO'])
        msg['From'] = self.config['FROM']

        # TODO: Make this configurable
        msg['Subject'] = 'ErrorEmail'

        msg.attach(self.get_plain_traceback(exc_info))
        msg.attach(self.get_html_traceback(exc_info))

        return msg.as_string()

    def __exit__(self, *args):
        if args:
            msg = self.create_message_from_traceback(args)
            self.send_email(msg)
            return False
        return True
