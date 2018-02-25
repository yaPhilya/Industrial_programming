# Запуск

* docker-compose build
* docker-compose up

В другом терминале

* docker build -t producer ./send_test
* docker run -it --network=firsttask_net_123 producer


Producer отправляет считанные слова, consumer записывает это в базу. 

Чтобы завершить producer'a послать ему EOF(Ctrl+D)
