from urllib.parse import urlencode


# URL
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


# URL CREATOR
class UrlCreator:

    __eq__ = Url.__eq__
    __str__ = Url.__str__

    def __init__(self, scheme, authority, path=None, query=None, fragment=None):
        self.scheme = scheme
        self.authority = authority
        self.path = path if path else []
        self.query = query
        self.fragment = fragment

    def _create(self):
        return Url(self.scheme, self.authority, self.path, self.query, self.fragment)

    def __getattr__(self, attr):
        self.path.append(attr)
        return self

    def __call__(self, *args, **kwargs):
        if args:
            self.path = list(args)
        if kwargs:
            self.query = kwargs
        return self


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

    # URL CREATOR class assertion
    url_creator = UrlCreator(scheme='https', authority='docs.python.org')
    assert url_creator.docs.v1.api.list == 'https://docs.python.org/docs/v1/api/list'
    assert url_creator(
        'api', 'v1', 'list') == 'https://docs.python.org/api/v1/list'
    assert url_creator(
        'api', 'v1', 'list', q='my_list') == 'https://docs.python.org/api/v1/list?q=my_list'
    assert url_creator('3').search(q='getattr', check_keywords='yes', area='default')._create() == \
        'https://docs.python.org/3/search?q=getattr&check_keywords=yes&area=default'
