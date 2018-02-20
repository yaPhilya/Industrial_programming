#!/usr/bin/env python3
import pika
import time

if __name__ == "__main__":

	print("Start sending...")
	print()

	time.sleep(20)

	connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))

	channel = connection.channel()

	channel.queue_declare(queue='hello_2')

	channel.basic_publish(exchange='',
		              routing_key='hello_2',
		              body='Hello World! :)')

	print(" [x] Sent 'Hello World!'")

	connection.close()
