from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
from random import randint
import time
def testar():
    topicos = ['Cachorro', 'Gato', 'Porco']
    for topico in topicos:
        registry = CollectorRegistry()
        print("TOPICO:", topico)
        comentario_size = randint(1, 255)
        comentario = Gauge('comment_size_gauge', 'Tamanho do comentário postado gauge', ["topico"], registry=registry)
        comentario.labels(topico).set(comentario_size)

        resposta_size = randint(1, 255)
        resposta = Gauge('response_size_gauge', 'Tamanho da resposta postada gauge', ["topico"], registry=registry)
        resposta.labels(topico).set(resposta_size)
        push_to_gateway('localhost:9091', job=f'job_comentarios_{topico}', registry=registry)
        print("subiu cometário:", comentario_size)
        print("subiu resposta:", resposta_size)

    
if __name__ == '__main__':
    while True:
        testar()
        time.sleep(10)

