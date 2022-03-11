from src.bmi_service.data_munger import DataMunger
import unittest
import pandas as pd
from unittest.mock import MagicMock
from src.bmi_service.data_loader import DataLoader
from src.bmi_service.data_munger import DataMunger

class TestApplicationRunner(unittest.TestCase):

    def test_analysis(self):
        """Test the main application runner."""
        dataloader = DataLoader()
        datamunger = DataMunger()
        df_raw = pd.DataFrame({"WeightKg": [96], "HeightCm": [171]})
        bmi_df = pd.DataFrame({"WeightKg": [96, 82], 
        "HeightCm": [171, 167], 
        "BMI": [32.8, 29.4]})
        final_df = pd.DataFrame({"WeightKg": [96, 82], 
        "HeightCm": [171, 167], 
        "BMI": [32.8, 29.4],
        "BMI Category":["Moderately obese", "Overweight"],
        "HealthRisk": ["Medium risk", "Enhanced risk"]})
        dataloader.get_data = MagicMock(return_value=df_raw)
        datamunger.calculate_bmi = MagicMock(return_value=bmi_df)
        datamunger.calculate_bmi_category = MagicMock(return_value=final_df)
        dataloader.get_data()
        dataloader.get_data.assert_called_once()


