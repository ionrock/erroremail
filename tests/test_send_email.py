import sys

from mock import patch, ANY
from erroremail import ErrorEmail


class TestSend(object):

    def setup(self):
        self.config = {
            'SERVER': 'MYHOST',
            'TO': ['my@email.com'],
            'FROM': 'your@email.com',
            'SUBJECT': 'ERR: {host}:{port} {message}',
        }
        self.err = ErrorEmail(self.config, host='x1', port=9999)

    @patch('erroremail.smtplib.SMTP')
    def test_send(self, SMTP):
        try:
            with self.err:
                raise Exception('Whoa')
        except:
            pass

        server = SMTP()
        server.sendmail.assert_called_with(
            self.config['TO'],
            self.config['FROM'],
            ANY
        )

    def test_get_subject(self):
        try:
            tuple()[0]
        except:
            subject = self.err.get_subject(sys.exc_info())
            assert subject == 'ERR: x1:9999 IndexError: tuple index out of range'

    def test_create_message(self):
        try:
            tuple()[0]
        except:
            info = sys.exc_info()

        message = self.err.create_message_from_traceback(info)
        subject = self.err.get_subject(info)

        assert message['Content-Type'] == 'multipart/alternative'
        assert message['Subject'] == subject
        assert message['To'] == 'my@email.com'
        assert message['From'] == 'your@email.com'
