"""
This module analyzes company registration data to calculate and plot
the number of companies registered in the year 2015 by district.

It reads data from the 'company_data.csv' and 'pincode.csv' files,
maps pincodes to districts, counts registrations, and displays
the result in a bar chart.
"""
import csv
import matplotlib
import matplotlib.pyplot as plt

# Set backend immediately after importing matplotlib
matplotlib.use('TkAgg')


def calculate_company_registration_by_the_district_in_2015():
    """
    Calculates the number of company registrations in the year 2015 grouped by district.

    Reads pincode-to-district mapping from 'pincode.csv' and company data from 'company_data.csv'.
    Extracts the pincode from the registered office address of each company,
    maps it to a district, and counts registrations that occurred in 2015.

    Returns:
        dict: A dictionary where keys are district names and values are registration counts in 2015.
    """
    company_registration_in_2015 = {}
    pincode_and_district = {}

    with open("../required_data/pincode.csv", encoding="utf-8") as pincode_file:
        pincode_data = csv.DictReader(pincode_file)

        for pincodes in pincode_data:
            pincode = pincodes["Pin_Code"]
            district = pincodes["District"].strip()

            if district not in pincode_and_district:
                pincode_and_district[district] = []

            if pincode not in pincode_and_district[district]:
                pincode_and_district[district].append(pincode)
    reversed_pincode_and_district = {}

    for district, pincode_list in pincode_and_district.items():
        for pincode in pincode_list:
            reversed_pincode_and_district[pincode] = district


    with open("../required_data/company_data.csv", encoding="utf-8") as company_file:
        company_data = csv.DictReader(company_file)

        for company in company_data:
            pincode = company["Registered_Office_Address"][-12:-6].strip()
            year = company["CompanyRegistrationdate_date"][:4]
            if year == "2015" and pincode in reversed_pincode_and_district:
                district = reversed_pincode_and_district[pincode]
                if district not in company_registration_in_2015:
                    company_registration_in_2015[district] = 0
                company_registration_in_2015[district] += 1

    return company_registration_in_2015


def plot_company_registration_by_the_district_in_2015(total_company_registration):
    """
    Plots a bar chart of company registrations in 2015 for each district.

    Args:
        total_company_registration (dict): A dictionary with district names as keys
                                           and registration counts as values.
    """
    plt.figure(figsize=(14,6))
    plt.title("Company Registration for the year 2015")
    plt.bar(total_company_registration.keys(), total_company_registration.values(), color="yellow")
    plt.xlabel("Distict")
    plt.ylabel("Number of Registration")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def execute():
    """
    Executes the full pipeline: data processing and visualization.

    Calls the function to calculate company registrations by district in 2015,
    then plots the result as a bar chart.
    """
    company_registration = calculate_company_registration_by_the_district_in_2015()
    plot_company_registration_by_the_district_in_2015(company_registration)  


if __name__ == "__main__":

    execute()
