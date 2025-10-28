
from petstore_client import PetStoreClient
from data_analyzer import PetDataAnalyzer
import json

def main():
    print("🚀 EXERCISE 2: DATA HANDLING IN API's")
    print("=" * 50)
    
    # Initialize the client
    client = PetStoreClient()
    
    # 1. Create a user and retrieve their data
    print("\n📝 STEP 1: Creating and retrieving user")
    print("-" * 40)
    
    user_response = client.create_user(
        username="john_doe123",
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com"
    )
    
    # Retrieve the user data
    user_data = client.get_user("john_doe123")
    if user_data:
        print(f"📋 User Details:")
        print(f"   Username: {user_data.get('username')}")
        print(f"   Name: {user_data.get('firstName')} {user_data.get('lastName')}")
        print(f"   Email: {user_data.get('email')}")
    
    # 2. Get sold pets and list them as tuples
    print("\n🐾 STEP 2: Retrieving sold pets")
    print("-" * 40)
    
    sold_pets = client.get_sold_pets_names()
    
    print(f"📊 Found {len(sold_pets)} sold pets")
    print("\n🔹 Sold pets (id, name):")
    for pet_id, pet_name in sold_pets[:10]:  # Show first 10
        print(f"   ({pet_id}, '{pet_name}')")
    
    if len(sold_pets) > 10:
        print(f"   ... and {len(sold_pets) - 10} more")
    
    # 3. Analyze pet names
    print("\n📊 STEP 3: Analyzing pet names")
    print("-" * 40)
    
    analyzer = PetDataAnalyzer(sold_pets)
    
    # Count pets with same names
    name_counts = analyzer.count_same_names()
    
    print("🔢 Pets sharing the same name:")
    for name, count in sorted(name_counts.items(), key=lambda x: x[1], reverse=True)[:15]:
        print(f"   '{name}': {count}")
    
    # Show summary statistics
    print(f"\n📈 Summary Statistics:")
    print(f"   Total pets sold: {analyzer.get_total_pets()}")
    print(f"   Unique names: {analyzer.get_unique_names_count()}")
    
    # Show most common names
    print(f"\n🏆 Top 5 most common pet names:")
    for name, count in analyzer.get_most_common_names(5):
        print(f"   '{name}': {count}")
    
    # Format output as requested
    print("\n🎯 FINAL OUTPUT (as requested):")
    print("-" * 40)
    print("📋 Sold pets (id, name) tuples:")
    for pet_id, pet_name in sold_pets[:5]:  # Show first 5 as example
        print(f"   {{{pet_id}, '{pet_name}'}}")
    
    print(f"\n🔢 Name counts (formatted):")
    formatted_counts = {k: v for k, v in sorted(name_counts.items(), key=lambda x: x[1], reverse=True)[:10]}
    print(f"   {json.dumps(formatted_counts, indent=2)}")

if __name__ == "__main__":
    main()