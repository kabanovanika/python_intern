# Python-Intern test

Test task from Semrush. This service checks if the host is up or down. 

## Getting Started

You may clone the repository and run it on your local machine or just use the deployed version via link below http://84.201.141.133:8000/healthz?hostname=semrush.com


### Installing

After cloning the repository you should install requirements.

```
pip install -r requirements.txt
```

### How to use
For running the service you may use the command below

```
uvicorn app.app:app --reload
```

Or you can also use docker-compose

```
docker-compose up 
```

Then it will be callable on the host [localhost:8000/healthz](localhost:8000/healthz)

The endpoint requires the host name, i.e hostname=wiki.com, typed right after the URL using '?' 

```
localhost:8000/healthz?hostname=wiki.com
```
And service gives JSON as result, either status 'up' or 'down' (depends on HTTP Response status code) 

```
{"status":"up"}
```

> **_NOTE:_**  On the Dec 14, 2020 - the day I submitted the code - I had difficulties with very long response times when testing locally.
I still don't know exactly what happened, but considering the Yandex.Cloud deployment worked as expected,
I suspect long response times had something to do with a Google outage on the same day. Hopefully, everything will work correctly on your side 🤞

## Built With

* [FastAPI](https://fastapi.tiangolo.com/) - The web framework
* [Docker](https://www.docker.com/) - Container packaging

## Authors

* **Nika Kabanova** - *Initial work* - [kabanovanika](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## Given task requirements

- python 3.9
- В изначальном коде менять можно *всё*, вплоть до структуры файлов. 
- Использовать можно всё что угодно. 
- Таски со звёздочкой можно пропускать (или делать часть из них)
- Решение выложить через fork/копию/etc репозитория на github


## TODO

- реализовать функцию [is_alive_host](app/app.py)

- покрыть функцию [тестами](./tests.py)

- развернуть вокруг функции веб сервис c помощью [fastapi](https://fastapi.tiangolo.com/)
```
>> curl your_service.loc:8001/healthz?hostname=semrush.com
{status: [up|down]}
```

- задача со *звёздочкой*: завернуть приложение в docker
- задача на *две звёздочки*: выложить куда-либо (heroku/DigitalOcean/etc) с помощью github-actions/gitlab/jenkins/etc
