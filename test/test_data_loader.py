from src.bmi_service.data_loader import DataLoader
import unittest
import pandas as pd
from unittest.mock import MagicMock

class TestDataLoader(unittest.TestCase):

    def test_get_data(self):
        """Test the get data functonality"""
        loader = DataLoader()
        loader.get_data = MagicMock(return_value=pd.DataFrame({"WeightKg": [96], "HeightCm": [171]}))
        actual_data = loader.get_data()
        assert len(actual_data) == 1
        assert actual_data["WeightKg"].iloc[0] == 96
