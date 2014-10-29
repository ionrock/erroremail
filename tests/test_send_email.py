from erroremail import ErrorEmail


class TestSend(object):

    def setup(self):
        config = {
            'SERVER': 'MYHOST',
            'TO': ['my@email.com'],
            'FROM': 'your@email.com',
        }
        self.err = ErrorEmail(config)

    def test_send(self):
        with self.err:
            raise Exception('Whoa')
