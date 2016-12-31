"""
jak to rozjet:
    - toto mit nainstalovane:
        pip install -U "celery[redis]"
    - pusteny redis, me to jede takto:
        $ redis-server
    - pusteny celery:
        $ celery worker -A sazime_korenovou_zeleninu -l info
    - skript jako takovy poustim klasicky:
        $ python sazime_korenovou_zeleninu.py
"""

from celery import Celery

# instance celery
# prvni argument je nazev modulu
# broker je to co celery pouziva (redis, rabbitmq...)
# do backend arguemntu zatim nevidim
app = Celery('sazime_korenovou_zeleninu',
             backend='rpc://',
             broker='redis://localhost:6379')


@app.task
def add(x, y):
    return x + y

x = add.delay(1, 1)

# todle vypise jakysi hash
print x

# tohle vypise False
print x.ready()

# tohle konecne! vypise 2
print x.get()
