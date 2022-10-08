def app(environ, start_response):
	data = "\n".join(environ.get('QUERY_STRING').split('&'))
	status = '200 OK'
	response_h = [('Content_type', 'text\plain')]
	start_response(status, response_h)
	return data.encode('utf-8')
