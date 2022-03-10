"""Module to munge and create additional information"""

class DataMunger():
    """Data MUnger Class"""

    def calculate_bmi(self, data):
        """
        Calculates bmi based on height and weight
        param: data, pandas dataframe of the input data
        return: dataframe, pandas dataframe with calculated bmi values
        """
        # Calculates bmi based on standard formula
        data["BMI"] = data["WeightKg"] / ((data["HeightCm"]/100) ** 2)
        data = data.round({"BMI":1})
        return data

    def calculate_bmi_category(self, data):
        """
        Calculates bmi category and health risk based on bmi value
        param: data, pandas dataframe of the input data
        return: dataframe, pandas dataframe with calculated values
        """
        def category_mapper(bmi):
            """User defined serivce to calculate bmi catergory and health indicator"""
            if bmi <=18.4:
                return "Underweight", "Malnutrition risk"
            elif bmi >=18.5 and bmi <=24.9:
                return "Normal Weight", "Low risk"
            elif bmi >=25 and bmi <=29.9:
                return "Overweight", "Enhanced risk"
            elif bmi >=30 and bmi <=34.9:
                return "Moderately obese", "Medium risk"
            elif bmi >=35 and bmi <=29.9:
                return "Severly obese", "High risk"
            else:
                return "Very Severly obese", "Very high risk"

        data["BMI Category"], data["HealthRisk"] = zip(*data["BMI"].apply(category_mapper))
        return data