from urllib.parse import urlencode


class Url:
    def __init__(self, scheme, authority, path=None, query=None, fragment=''):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __eq__(self, other):
        return str(self) == str(other)

    def __str__(self):
        path = '/' + '/'.join(self.path) if self.path else ''
        query = '?' + urlencode(self.query) if self.query else ''
        fragment = '#' + self.fragment if self.fragment else ''
        return f"{self.scheme}://{self.authority}{path}{query}{fragment}"


class HttpsUrl(Url):
    def __init__(self, authority, path=None, query=None, fragment=''):
        super().__init__("https", authority, path, query, fragment)


class HttpUrl(Url):
    def __init__(self, authority, path=None, query=None, fragment=''):
        super().__init__("http", authority, query, query, fragment)


class GoogleUrl(HttpsUrl):
    def __init__(self, path=None, query=None, fragment=None):
        super().__init__("google.com", path, query, fragment)


class WikiUrl(HttpsUrl):
    def __init__(self, path=None, query=None, fragment=None):
        super().__init__("wikipedia.org", path, query, fragment)


if __name__ == '__main__':
    # URL class assertion
    assert GoogleUrl() == HttpsUrl(authority='google.com')
    assert GoogleUrl() == Url(scheme='https', authority='google.com')
    assert GoogleUrl() == 'https://google.com'
    assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
    assert WikiUrl(path=['wiki', 'python']
                   ) == 'https://wikipedia.org/wiki/python'
    assert GoogleUrl(query={'q': 'python', 'result': 'json'}
                     ) == 'https://google.com?q=python&result=json'
