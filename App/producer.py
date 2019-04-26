 #!/usr/bin/env python
import pika
import sys
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')
message = raw_input("Send a message>")  
channel.basic_publish(exchange='logs', routing_key='', body=message)
while message != 'exit':
	message = raw_input("Send a message>")
	channel.basic_publish(exchange='logs', routing_key='', body=message)
	print(" [x] Sent %r" % message)
connection.close()
