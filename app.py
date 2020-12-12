import requests
from fastapi import FastAPI



app = FastAPI()


def is_alive_host(hostname):
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""
    try:
        r = requests.head(f'https://{hostname}')
        if 100 <= r.status_code < 400:
            return 'up'
        else:
            return 'down'
    except requests.ConnectionError:
        message = "Failed to connect"
        return message


@app.get("/healthz")
async def read_item(hostname: str):
    item = {'status': is_alive_host(hostname)}
    return item
