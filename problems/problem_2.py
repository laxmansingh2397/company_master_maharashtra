"""
This module analyzes company data to calculate and plot
the number of company registrations per year.

It reads data from the 'company_data.csv' file, extracts
the registration year from the 'CompanyRegistrationdate_date' column,
counts companies registered each year, and visualizes this in a bar chart.
"""
import csv
import matplotlib
import matplotlib.pyplot as plt

# Set backend immediately after importing matplotlib
matplotlib.use('TkAgg')


def calculate_company_registration_by_year():
    """
    Reads the company data from a CSV file and counts the number of
    company registrations per year based on the 'CompanyRegistrationdate_date' field.

    Returns:
        dict: A dictionary with years (as strings) as keys and the count of
              company registrations in each year as values, sorted by year.
              Example:
              {
                  "1991": 5115,
                  "1992": 5631,
                  ...
              }
    """
    total_companies_by_year = {}

    with open("../required_data/company_data.csv",encoding="utf-8") as data:
        company_data = csv.DictReader(data)

        for company in company_data:
            year = company["CompanyRegistrationdate_date"][:4]

            total_companies_by_year[year] = total_companies_by_year.get(
                year, 0) + 1

    sorted_total_companies_by_year = dict(sorted(total_companies_by_year.items()))
    return sorted_total_companies_by_year


def plot_company_registration_by_year(total_company_registered):
    """
    Plots a bar chart showing the number of company registrations per year.

    Args:
        total_company_registered (dict): A dictionary where keys are years (str)
                                         and values are the number of companies
                                         registered in that year.
    """
    plt.figure(figsize=(16, 6))
    plt.bar(total_company_registered.keys(), total_company_registered.values(), color="blue")
    plt.title("Number of Company Registrations by Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Companies")
    plt.xticks(rotation=90, fontsize=8)
    plt.tight_layout()
    plt.show()


def execute():
    """
    Executes the analysis pipeline:
    - Calculates company registration counts by year.
    - Plots the result as a bar chart.
    """
    company_registration_by_year = calculate_company_registration_by_year()
    plot_company_registration_by_year(company_registration_by_year)


if __name__ == "__main__":

    execute()
