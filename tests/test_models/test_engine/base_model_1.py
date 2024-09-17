#!/usr/bin/python3
"""Unittest for BaseModel class."""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_save_method(self):
        """Test if the save method updates 'updated_at'."""
        # Create a new instance of BaseModel
        instance = BaseModel()
        
        # Save the initial value of updated_at
        initial_updated_at = instance.updated_at
        
        # Wait for some time to ensure a difference in time
        time.sleep(0.1)
        
        # Call the save method
        instance.save()
        
        # Check if updated_at has changed
        self.assertNotEqual(initial_updated_at, instance.updated_at)
        
        # Check if updated_at is of type datetime
        self.assertIsInstance(instance.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
