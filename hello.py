

def web_application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    result = ['{}\n'.format(item).encode() for item in environ['QUERY_STRING'].split('&')]
    start_response(status, response_headers)
    return result
