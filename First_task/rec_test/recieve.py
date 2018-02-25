#!/usr/bin/env python
import pika
import time
#import postgresql
import psycopg2

if __name__ == "__main__":
	print("Start receive...")
	print()

	time.sleep(40)

	connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
	channel = connection.channel()

	channel.queue_declare(queue='hello_2')

	#db = postgresql.open('pq://postgres:qwerty@db:5432/postgres')
	#db.execute("CREATE TABLE IF NOT EXIST strings (str CHAR(255))")

	#ins = db.prepare("INSERT INTO strings (str) VALUES ($1)")

	def callback(ch, method, properties, body):
		conn = psycopg2.connect(dbname='postgres', user='postgres', host='db', password='qwerty', port='5432')
		cur = conn.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS strings (ID serial PRIMARY KEY, str VARCHAR(255));")
		s = str(body, 'utf-8')
		print(" [x] Received {}".format(s), flush=True)

		#ins(str(body))
		#print("INSERT INTO strings (str) VALUES ({})".format("'" + s + "'"), flush=True)
		cur.execute("INSERT INTO strings (str) VALUES ({});".format("'" + s + "'"))
		print(" [x] INsert, Printing db", flush=True)
		cur.execute("SELECT * FROM strings")
		for row in cur:
			print(row, flush=True)
		conn.close()

	channel.basic_consume(callback, queue='hello_2', no_ack=True)
	# cur.execute("SELECT * FROM strings")
	# for row in cur:
	# 	print(row, flush=True)
	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()
