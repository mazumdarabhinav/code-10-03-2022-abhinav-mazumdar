from src.bmi_service.data_munger import DataMunger
import unittest
import pandas as pd

class TestDataMunger(unittest.TestCase):

    def test_calculate_bmi(self):
        """Test bmi calculation."""
        munger = DataMunger()
        df = pd.DataFrame({"WeightKg": [96], "HeightCm": [171]})
        result_df = munger.calculate_bmi(df)
        assert result_df["BMI"].iloc[0] == 32.8

    def test_calculate_bmi(self):
        """Test bmi category and health indicator calculations"""
        munger = DataMunger()
        df = pd.DataFrame({"WeightKg": [96, 82], "HeightCm": [171, 167], "BMI": [32.8, 29.4]})
        result_df = munger.calculate_bmi_category(df)
        assert result_df["BMI Category"].iloc[0] == "Moderately obese"
        assert result_df["HealthRisk"].iloc[0] == "Medium risk"

        assert result_df["BMI Category"].iloc[1] == "Overweight"
        assert result_df["HealthRisk"].iloc[1] == "Enhanced risk"