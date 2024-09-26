"""
@Author: Sarah Williams
Assingment: Project 1 AQI
Date: 18 September 2024
"""
# Function to print the Air Quality Index Table as a reference at the start of the program.
def air_quality_index(scale):
    print("\t\t\tAir Quality Index Scale")
    for row in scale:
        print(f"{row[0]:<30}{row[1]:<30}{row[2]:<0}")


    scale = [
        ["Pollution Measurement", "Classification", "Color"],
        ["0 - 50", "Good", "Green"],
        ["51 - 100", "Moderate", "Yellow"],
        ["101 - 150", "Unhealthy for Sensitive", "Orange"],
        ["151 - 200", "Unhealthy", "Red"],
        ["201 - 300", "Very Unhealthy", "Purple"],
        ["301 - 500", "Hazardous", "Maroon"]
    ]

    air_quality_index(scale)
    return

pollution_scale = {
    "Low": {range: (0, 50), "Color" : "Green"},
    "Moderate": {range: (51, 100), "Color" : "Yellow"},
    "Unhealthy for Sensitive" : {range: (101, 150), "Color" : "Orange"},
    "Unhealthy": {range: (151, 200), "Color" : "Red"},
    "Very Unhealthy" : {range: (201, 300), "Color" : "Purple"},
    "Hazardous": {range: (301, 500), "Color" : "Maroon"}
}

# Function to get the category and color based on the measurement.
def category_and_color(pollution_measurement):
    for category, details in pollution_scale.items():
        if details[range][0] <= pollution_measurement <= details[range][1]:
            return category, details["Color"]
    return

# Getting the number of reports and getting the polution measurement for each one.
report_quantity = int(input("Enter the number of reports: "))
if report_quantity < 0:
        print("Error. Must be a positive number")
for report_number in range(1, report_quantity + 1):
    pollution_measurement = int(input("Enter the pollution measurement: "))
    print(f"\nReport Number: {report_number}")
    print(f"Pollution Measurement: {pollution_measurement}")
    print(f"Category: {pollution_scale[0]}")
    print(f"Color: {pollution_scale[1]}\n")



