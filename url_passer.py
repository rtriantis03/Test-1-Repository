import re

class URLParser:
    def __init__(self, url):
        self.url = url
        self.scheme = None
        self.hostname = None
        self.path = None
        self.parse_url()

    def parse_url(self):
        regex = r'^(https?)://([^/]+)(/.*)?$'
        match = re.match(regex, self.url)
        if match:
            self.scheme, self.hostname, self.path = match.groups()
        else:
            self.scheme = 'http'
            self.hostname = self.url
            self.path = '/'

    def get_hostname(self):
        return self.hostname

    def get_path(self):
        return self.path if self.path else '/'

    def get_scheme(self):
        return self.scheme
