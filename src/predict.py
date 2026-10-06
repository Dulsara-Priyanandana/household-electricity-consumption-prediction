import joblib
import pandas as pd
from datetime import datetime
from pathlib import Path


#  Load trained model
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "electricity_model.pkl"
DATA_PATH = BASE_DIR / "data" / "cleaned_data.csv"

model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATA_PATH)

# Create District -> Province mapping
mapping = (
    df[["District", "Province"]]
    .drop_duplicates()
    .sort_values(["Province", "District"])
)

district_to_province = (
    mapping.set_index("District")["Province"].to_dict()
)

# Get valid categories directly from the dataset
household_types = sorted(
    df["Household_Type"].dropna().unique()
)

solar_options = sorted(
    df["Solar_PV"].dropna().unique()
)

def get_district(district_to_province):

    districts = sorted(district_to_province.keys())

    while True:

        print("\nSelect district:")

        for i, district in enumerate(districts, start=1):
            print(f"{i}. {district}")

        try:
            choice = int(input("Enter district number: "))

            if 1 <= choice <= len(districts):

                district = districts[choice - 1]

                province = district_to_province[district]

                print(f"\nSelected District : {district}")
                print(f"Province          : {province}")

                return district, province

            else:
                print(
                    f"Please enter a number from 1 to {len(districts)}."
                )

        except ValueError:
            print("Please enter a valid number.")



#  INPUT VALIDATION FUNCTIONS

def get_solar_capacity(solar_pv):

    if solar_pv.lower() == "no":
        print("Solar PV is not available.")
        print("Solar capacity automatically set to 0 kW.")
        return 0.0

    while True:
        try:
            capacity = float(
                input("Enter solar capacity (kW): ")
            )

            if capacity <= 0:
                print("Solar capacity must be greater than 0.")
            else:
                return capacity

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_integer(prompt, minimum=0):
    while True:
        try:
            value = int(input(prompt))

            if value < minimum:
                print(f"Please enter a value >= {minimum}.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_float(prompt, minimum=0, maximum=None):
    while True:
        try:
            value = float(input(prompt))

            if value < minimum:
                print(f"Please enter a value >= {minimum}.")

            elif maximum is not None and value > maximum:
                print(f"Please enter a value between {minimum} and {maximum}.")

            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_yes_no(prompt):
    while True:
        value = input(prompt).strip().lower()

        if value in ["yes", "y"]:
            return "Yes"

        elif value in ["no", "n"]:
            return "No"

        else:
            print("Please enter Yes or No.")


def get_choice(prompt, choices):
    while True:
        value = input(prompt).strip()

        for choice in choices:
            if value.lower() == choice.lower():
                return choice

        print("Invalid choice.")
        print("Available choices:", ", ".join(choices))


def get_month():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:

        print("\nSelect month:")

        for i, month in enumerate(months, start=1):
            print(f"{i}. {month}")

        try:
            choice = int(input("Enter month number: "))

            if 1 <= choice <= 12:
                return months[choice - 1]

            print("Please enter a number from 1 to 12.")

        except ValueError:
            print("Please enter a valid number.")





#  PROGRAM TITLE


print()
print("==========================================")
print(" HOUSEHOLD ELECTRICITY PREDICTION")
print("==========================================")
print()



#  CATEGORICAL INPUTS


month = get_month()


district, province = get_district(district_to_province)

household_type = get_choice(
    "Enter household type: ",
    household_types
)

solar_pv = get_choice(
    "Solar PV available? ",
    solar_options
)


#  NUMERICAL INPUTS


household_size = get_integer(
    "Enter household size: ",
    minimum=1
)

house_area = get_float(
    "Enter house area (m²): ",
    minimum=1
)

bedrooms = get_integer(
    "Enter number of bedrooms: ",
    minimum=1
)

fans = get_integer(
    "Enter number of fans: ",
    minimum=0
)

if fans == 0:
    fan_hours = 0.0
    print("No fans → Fan usage hours automatically set to 0.")
else:
    fan_hours = get_float(
        "Enter average daily fan usage hours: ",
        minimum=0,
        maximum=24
    )




refrigerators = get_integer(
    "Enter number of refrigerators: ",
    minimum=0
)

tvs = get_integer(
    "Enter number of TVs: ",
    minimum=0
)

if tvs == 0:
    tv_hours = 0.0
    print("No TVs → TV usage hours automatically set to 0.")
else:
    tv_hours = get_float(
        "Enter average daily TV usage hours: ",
        minimum=0,
        maximum=24
    )

washing_machines = get_integer(
    "Enter number of washing machines: ",
    minimum=0
)

water_heaters = get_integer(
    "Enter number of water heaters: ",
    minimum=0
)

computers = get_integer(
    "Enter number of computers: ",
    minimum=0
)

other_appliances = get_integer(
    "Enter number of other high-power appliances: ",
    minimum=0
)

ac_units = get_integer(
    "Enter number of AC units: ",
    minimum=0
)

if ac_units == 0:
    ac_hours = 0.0
    print("No AC units → AC usage hours automatically set to 0.")
else:
    ac_hours = get_float(
        "Enter average daily AC usage hours: ",
        minimum=0,
        maximum=24
    )

cooking_hours = get_float(
    "Enter average daily cooking hours: ",
    minimum=0,
    maximum=24
)



#  OTHER NUMERICAL INPUTS


solar_capacity = get_solar_capacity(solar_pv)

temperature = get_float(
    "Enter average temperature (°C): ",
    minimum=0,
    maximum=50
)

previous_month = get_float(
    "Enter previous month consumption (kWh): ",
    minimum=0
)



#  CREATE DATAFRAME


household = pd.DataFrame([{

    "Month": month,
    "Province": province,
    "District": district,
    "Household_Type": household_type,

    "Household_Size": household_size,
    "House_Area_m2": house_area,
    "Bedrooms": bedrooms,
    "AC_Units": ac_units,
    "Fans": fans,
    "Refrigerators": refrigerators,
    "TVs": tvs,
    "Washing_Machines": washing_machines,
    "Water_Heaters": water_heaters,
    "Computers": computers,
    "Other_High_Power_Appliances": other_appliances,

    "Avg_Daily_AC_Hours": ac_hours,
    "Avg_Daily_Fan_Hours": fan_hours,
    "Avg_Daily_TV_Hours": tv_hours,
    "Avg_Daily_Cooking_Hours": cooking_hours,

    "Solar_PV": solar_pv,
    "Solar_Capacity_kW": solar_capacity,

    "Avg_Temperature_C": temperature,
    "Previous_Month_kWh": previous_month

}])


# ==========================================
# 9. MAKE PREDICTION
# ==========================================

prediction = model.predict(household)

predicted_kwh = prediction[0]

prediction_time = datetime.now()

if predicted_kwh < 200:
    usage_level = "Low"
elif predicted_kwh < 400:
    usage_level = "Moderate"
else:
    usage_level = "High"
# ==========================================
# 10. DISPLAY RESULT
# ==========================================

print()
print("==========================================")
print(" PREDICTION RESULT")
print("==========================================")
print()

print(
    f"Predicted Monthly Electricity Consumption: "
    f"{prediction[0]:.2f} kWh"
)

print()
print("==========================================")

report = f"""
==========================================
 HOUSEHOLD ELECTRICITY PREDICTION REPORT
==========================================

Prediction Date and Time:
{prediction_time.strftime("%Y-%m-%d %H:%M:%S")}

------------------------------------------
 HOUSEHOLD INFORMATION
------------------------------------------

Month              : {month}
District           : {district}
Province           : {province}
Household Type     : {household_type}
Household Size     : {household_size}
House Area         : {house_area:.1f} m²
Bedrooms           : {bedrooms}

------------------------------------------
 APPLIANCE INFORMATION
------------------------------------------

AC Units                    : {ac_units}
Fans                        : {fans}
Refrigerators               : {refrigerators}
TVs                         : {tvs}
Washing Machines            : {washing_machines}
Water Heaters               : {water_heaters}
Computers                   : {computers}
Other High-Power Appliances : {other_appliances}

------------------------------------------
 USAGE INFORMATION
------------------------------------------

Average Daily AC Hours      : {ac_hours:.2f}
Average Daily Fan Hours     : {fan_hours:.2f}
Average Daily TV Hours      : {tv_hours:.2f}
Average Daily Cooking Hours : {cooking_hours:.2f}

------------------------------------------
 SOLAR AND WEATHER INFORMATION
------------------------------------------

Solar PV                    : {solar_pv}
Solar Capacity              : {solar_capacity:.2f} kW
Average Temperature         : {temperature:.2f} °C

Previous Month Consumption  : {previous_month:.2f} kWh

------------------------------------------
 PREDICTION
------------------------------------------

Predicted Monthly Consumption : {predicted_kwh:.2f} kWh
Estimated Usage Level         : {usage_level}

==========================================
"""

print(report)

# Create reports folder path
report_dir = Path(__file__).resolve().parent.parent / "reports"

# Create the folder if it does not exist
report_dir.mkdir(exist_ok=True)

# Create a unique filename using date and time
filename = f"electricity_prediction_{prediction_time.strftime('%Y%m%d_%H%M%S')}.txt"

report_path = report_dir / filename

# Save report
with open(report_path, "w", encoding="utf-8") as file:
    file.write(report)

print("\nReport saved successfully!")
print("Report location:", report_path)









