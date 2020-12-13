import requests
from fastapi import FastAPI

app = FastAPI()


def is_alive_host(hostname):
    """Checking if the host returns http status 100<=x<400."""
    try:
        r = requests.get(f'https://{hostname}')
        return 100 <= r.status_code < 400
    except requests.ConnectionError:
        return False


@app.get("/healthz")
async def read_item(hostname: str):
    resp = "up" if is_alive_host(hostname) else "down"
    item = {'status': resp}
    return item


if __name__ == '__main__':
    is_alive_host()
