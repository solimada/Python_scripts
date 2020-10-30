import ssl, sys
from argparse import ArgumentParser

try:
	from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
	from SimpleHTTPServer import SimpleHTTPRequestHandler
except:
	from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler

def parse_args():
	parser = ArgumentParser()
	
	parser.add_argument('-p',dest='port',help='port number to listen on',default=80,type=int)
	parser.add_argument('-c',dest='certname',help='certificate file name')
	
	return parser.parse_args()



if __name__=='__main__':
	args = parse_args()
	httpd = HTTPServer(('0.0.0.0',args.port),SimpleHTTPRequestHandler)
	
	#uncomment for https listener
	#httpd.socket = ssl.wrap_socket(httpd.socket, cerftfile=args.certname, serve_side=True)
	
	print("http listener on port %d..."%args.port)
	httpd.serve_forever()
