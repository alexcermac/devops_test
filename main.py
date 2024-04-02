from api_client import APIClient

def main():
    print("test")
    api_client = APIClient('http://localhost:30000/drivers-licenses/list', 150)

    results = api_client.fetch()
    print(results)

if __name__ == "__main__":
    main()