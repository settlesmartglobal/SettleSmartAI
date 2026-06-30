from app.utils.http_client import get


def test():
    url = "https://www.emiratesgroupcareers.com"

    response = get(url)

    print("=" * 60)
    print("Website Connected Successfully")
    print("=" * 60)
    print("Status Code:", response.status_code)
    print(response.text[:500])