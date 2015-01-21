# -*- coding: utf-8 -*-
__author__ = 'Eric Larson'
__email__ = 'eric@ionrock.org'
__version__ = '0.1.3'

import cgitb
import smtplib
import traceback

from cStringIO import StringIO
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from contextlib import contextmanager


class ErrorEmail(object):

    def __init__(self, config, **kw):
        self.config = config
        self.extra_info = kw

    def __enter__(self):
        return self

    @contextmanager
    def mail_server(self):
        server = smtplib.SMTP(self.config['SERVER'],
                              self.config.get('PORT', 25))
        yield server
        server.quit()

    def send_email(self, message):
        to = self.config['TO']
        if isinstance(to, basestring):
            to = [to]
        frm = self.config['FROM']
        with self.mail_server() as server:
            server.sendmail(to, frm, message)

    def get_plain_traceback(self, exc_info):
        fh = StringIO()
        traceback.print_tb(exc_info[2], fh)
        return MIMEText(fh.getvalue(), 'plain')

    def get_html_traceback(self, exc_info):
        return MIMEText(cgitb.html(exc_info), 'html')

    def get_subject(self, exc_info):
        tmpl = self.config.get('SUBJECT', 'ErrorEmail: {message}')
        message = traceback.format_exception(*exc_info).pop().strip()
        return tmpl.format(message=message, **self.extra_info)

    def create_message_from_traceback(self, exc_info):
        msg = MIMEMultipart('alternative')

        msg['To'] = ', '.join(self.config['TO'])
        msg['From'] = self.config['FROM']

        # TODO: Make this configurable
        msg['Subject'] = self.get_subject(exc_info)

        msg.attach(self.get_plain_traceback(exc_info))
        msg.attach(self.get_html_traceback(exc_info))

        return msg.as_string()

    def __exit__(self, *args):
        if args:
            msg = self.create_message_from_traceback(args)
            self.send_email(msg.as_string())
            return False
        return True
