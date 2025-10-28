from typing import List, Tuple, Dict
from collections import Counter

class PetDataAnalyzer:
    def __init__(self, pet_data: List[Tuple[int, str]]):
        """
        Constructor that requires the pet data structure (list of tuples)
        
        Args:
            pet_data: List of tuples in format (id, name)
        """
        self.pet_data = pet_data
        self.name_counter = None
        self._analyze_names()
    
    def _analyze_names(self):
        """Analyze the pet names and count occurrences"""
        names = [name for _, name in self.pet_data if name]
        self.name_counter = Counter(names)
    
    def count_same_names(self) -> Dict[str, int]:
        """
        Identify how many pets share the same name
        
        Returns:
            Dictionary with names as keys and counts as values
        """
        return dict(self.name_counter)
    
    def get_most_common_names(self, n: int = 10) -> List[Tuple[str, int]]:
        """Get the n most common pet names"""
        return self.name_counter.most_common(n)
    
    def get_total_pets(self) -> int:
        """Get total number of pets"""
        return len(self.pet_data)
    
    def get_unique_names_count(self) -> int:
        """Get number of unique pet names"""
        return len(self.name_counter)