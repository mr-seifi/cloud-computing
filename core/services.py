import pika
from django.conf import settings
import requests


class AMPQService:

    def __init__(self, queue='default'):
        self._ampq_url = settings.AMPQ_URL
        self._queue = queue

    def _make_channel(self):
        self._con = pika.BlockingConnection(pika.URLParameters(self._ampq_url))
        channel = self._con.channel()
        channel.queue_declare(queue=self._queue)

        return channel

    def publish(self, body):
        channel = self._make_channel()

        channel.basic_publish(exchange='', routing_key=self._queue, body=body)
        print(f"[+] Sent {body}")
        self._con.close()

    def consume(self):
        connection = self._con
        channel = connection.channel()

        channel.queue_declare(queue=self._queue)

        def callback(ch, method, properties, body):
            print(f"[+] Received {body}")

        channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

        print('[*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()


class ImageProcessingService:

    def __init__(self):
        self._api_key = settings.IMAGGA_API_KEY
        self._api_sec = settings.IMAGGA_API_SECRET
        self._endpoint = settings.IMAGGA_ENDPOINT_URL

    def tags(self, image_url):
        response = requests.get(
            'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
            auth=(self._api_key, self._api_sec)
        )

        print(response, response.text)
        tags = response.json()['result']['tags']
        for tag in tags:
            confidence = tag['confidence']
            tag_name = tag['tag']['en']
            print(f'Confidence: {confidence}, tag: {tag_name}')

        return tags[0]['tag']['en']
