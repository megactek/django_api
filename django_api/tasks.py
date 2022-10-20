from celery import task
import time
import requests



@task()
def test(value):
    time.sleep(5)
    print(value)



@task()
def populate_dog():
    url = 'https://dog.ceo/api/breeds/image/random'
    try:
        res = requests.get(url)
    except requests.ConnectionError as e:
        raise Exception('Connection failed: %s' % e.message)
    if res.status_code in [200, 201]:
        #create dog entry
        data = res.json()
        image_url = data.get('message', '')
        from event_controller.models import Dog
        Dog.objects.create(url=image_url)


