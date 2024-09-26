"""
@Author: Sarah Williams
Assingment: Project 1 AQI
Date: 18 September 2024
"""


# Dictionary for pollution levels. Classification (low, moderate, etc) is key. Color is value. 
# User will input a value and the program will look through the dictionary, and assign the category and color to the report.
pollution_levels_dictionary = {
    "Low": {"range": (0, 50), "color": "Green"},
    "Moderate": {"range": (51, 100), "color": "Yellow"},
    "Unhealthy for Sensitive Groups": {"range": (101, 150), "color": "Orange"},
    "Unhealthy": {"range": (151, 200), "color": "Red"},
    "Very Unhealthy": {"range": (201, 300), "color": "Purple"},
    "Hazardous": {"range": (301, 500), "color": "Maroon"}
}

# Function to get the classification and color based on the measurement.
def get_classification_and_color(pollution_measurement):
    for classification, details in pollution_levels_dictionary.items():
        if details["range"][0] <= pollution_measurement <= details["range"][1]:
            return classification, details["color"]
    return

def main():
    
    report_quantity = int(input("Enter the amount of reports: "))
    if report_quantity < 0:
        print("Error. Report quantity must be at least 0")

    # Iterations for each report
    for report_number in range(1, report_quantity + 1):
        pollution_measurement = int(input(f"Enter the pollution measurement for report {report_number}: "))
        if pollution_measurement < 0 or pollution_measurement > 500:
            print("Invalid. Pollution levels must be between 0 and 500.")
            return
        classification, color = get_classification_and_color(pollution_measurement)


        print(f"\n{"Report Number":<30} AQI{report_number}")
        print(f"{"Pollution Measurement":<30} {pollution_measurement}")
        print(f"{"Classification":<30} {classification}")
        print(f"{"Color":<30} {color}\n")
main()
