import requests

# Define the API URL (Using JSONPlaceholder for fake data)
API_URL = "https://jsonplaceholder.typicode.com/posts/1"

try:
    # Send GET request to fetch data from API
    response = requests.get(API_URL)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        data = response.json()  # Convert response to JSON format

        # Print the fetched data
        print("✅ API Response:")
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
    else:
        print(f"❌ Error: API returned status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"❌ An error occurred: {e}")