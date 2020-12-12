import requests

def is_alive_host(hostname):
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""
    try:
        r = requests.head(hostname)
        print(r.status_code)
    except requests.ConnectionError:
        print("Failed to connect")



if __name__ == '__main__':
    is_alive_host("https://semrush.com")

