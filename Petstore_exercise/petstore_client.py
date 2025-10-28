import requests
import json
from typing import List, Tuple, Dict

class PetStoreClient:
    def __init__(self, base_url: str = "https://petstore.swagger.io/v2"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def create_user(self, username: str, first_name: str, last_name: str, email: str) -> Dict:
        """Create a new user in the pet store"""
        user_data = {
            "username": username,
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "password": "test123",
            "phone": "123-456-7890",
            "userStatus": 1
        }
        
        response = self.session.post(
            f"{self.base_url}/user",
            json=user_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            print(f"✅ User '{username}' created successfully!")
            return response.json()
        else:
            print(f"❌ Failed to create user: {response.status_code} - {response.text}")
            return {}
    
    def get_user(self, username: str) -> Dict:
        """Retrieve user data by username"""
        response = self.session.get(f"{self.base_url}/user/{username}")
        
        if response.status_code == 200:
            print(f"✅ User data retrieved successfully!")
            return response.json()
        else:
            print(f"❌ Failed to retrieve user: {response.status_code} - {response.text}")
            return {}
    
    def get_pets_by_status(self, status: str = "sold") -> List[Dict]:
        """Retrieve pets by their status"""
        response = self.session.get(
            f"{self.base_url}/pet/findByStatus",
            params={'status': status}
        )
        
        if response.status_code == 200:
            print(f"✅ Retrieved {len(response.json())} pets with status '{status}'")
            return response.json()
        else:
            print(f"❌ Failed to retrieve pets: {response.status_code} - {response.text}")
            return []
    
    def get_sold_pets_names(self) -> List[Tuple[int, str]]:
        """Get sold pets as tuples of (id, name)"""
        sold_pets = self.get_pets_by_status("sold")
        pet_tuples = []
        
        for pet in sold_pets:
            pet_id = pet.get('id')
            pet_name = pet.get('name', 'Unknown')
            pet_tuples.append((pet_id, pet_name))
        
        return pet_tuples