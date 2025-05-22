import requests

BASE_URL = "http://localhost:5001"

def run_test():
    user_id = "jay123"

    # Add a category
    print("Adding category...")
    response = requests.post(f"{BASE_URL}/categories", json={
        "userId": user_id,
        "categoryName": "Pet Supplies"
    })
    print("Add Response:", response.json())

    # Get all categories
    print("\nGetting all categories...")
    response = requests.get(f"{BASE_URL}/categories", params={"userId": user_id})
    categories = response.json()
    print("Get Response:", categories)

    # Delete the custom category we just added
    custom_id = [cat["id"] for cat in categories if cat["type"] == "custom" and cat["name"] == "Pet Supplies"][0]
    print("\nDeleting category...")
    response = requests.delete(f"{BASE_URL}/categories/{custom_id}", params={"userId": user_id})
    print("Delete Response:", response.json())

if __name__ == "__main__":
    run_test()
