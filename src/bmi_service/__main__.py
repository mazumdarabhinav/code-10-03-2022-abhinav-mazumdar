"""Main Application Ruuner to Run the BMI Service."""
from .data_loader import DataLoader
from .data_munger import DataMunger

class ApplicationRunner():
    """Main Application Runner"""

    def analysis(self):
        """
        Analyise and calculate the required fields.
        """
        dataloader = DataLoader()
        datamunger = DataMunger()
        # get the data
        data = dataloader.get_data()
        # calculate the bmi
        bmi = datamunger.calculate_bmi(data)
        # calculate the bmi category and health indicator
        final_data = datamunger.calculate_bmi_category(bmi)
        print("New Data after Manipulation")
        print(final_data.to_markdown())

        # count no of people in overweight category
        count_people_overweight = final_data[final_data["BMI Category"] == "Overweight"].shape[0]
        print(f"Total Number of overweight people: {count_people_overweight}")




if __name__ == "__main__":
    runner = ApplicationRunner()
    runner.analysis()
