from api_client import APIClient
from process_data import ProcessData

def main():
    api_client = APIClient('http://localhost:30000/drivers-licenses/list', 10)
    results = api_client.fetch()
    print(results)

    process_data = ProcessData(results)

    while True:
        print("What do you want to do with data?")
        print("1. List suspended licenses by the authority")
        print("2. Extract valid licenses issued until today's date")
        print("3. Find licenses based on category and their count")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            process_data.list_suspended_licenses()
        elif choice == "2":
            process_data.extract_valid_licenses()
        elif choice == "3":
            print("3. Call Function 3")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
    

if __name__ == "__main__":
    main()