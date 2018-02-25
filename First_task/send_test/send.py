#!/usr/bin/env python3
import pika
import time
import sys

if __name__ == "__main__":

	print("Start sending...")
	print()

	time.sleep(20)

	connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))

	channel = connection.channel()

	channel.queue_declare(queue='hello_2')

	while True:
		l = sys.stdin.readline()
		if not l:
			#channel.basic_publish(exchange='', routing_key='hello_2', body='\0')
			print(' [x] Good bye)')
			break
		channel.basic_publish(exchange='', routing_key='hello_2', body=l)
		print(" [x] Sent {}".format(l))
	connection.close()
