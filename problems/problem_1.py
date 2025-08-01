"""
This module analyzes Company data to calculate and plot
Authorized capital.

It reads data from the 'company.csv' file, processes the
Authorized capital, and displays the results in a bar chart.
"""
import csv
import matplotlib
import matplotlib.pyplot as plt

# Set backend immediately after importing matplotlib
matplotlib.use('TkAgg')


def calculate_authorized_capital():
    """
    Reads the company data from a CSV file and categorizes each company
    into predefined ranges based on its authorized capital.

    Returns:
        dict: A dictionary with keys as authorized capital ranges 
        and values as the count of companies in each range.
              Example:
              {
                  "<=1L": 239781,
                  "1L to 10L": 186407,
                  ...
              }
    """
    authorized_capital = {"<=1L": 0, "1L to 10L": 0, "10L to 1Cr": 0, "1Cr to 10Cr": 0, ">10Cr": 0}

    with open("../required_data/company_data.csv") as data:
        company_data = csv.DictReader(data)

        for company in company_data:
            capital = float(company["AuthorizedCapital"])

            if capital <= 100000:
                authorized_capital["<=1L"] += 1
            elif capital > 100000 and capital <= 1000000:
                authorized_capital["1L to 10L"] += 1
            elif capital > 1000000 and capital <= 10000000:
                authorized_capital["10L to 1Cr"] += 1
            elif capital > 10000000 and capital <= 100000000:
                authorized_capital["1Cr to 10Cr"] += 1
            else:
                authorized_capital[">10Cr"] += 1
    return authorized_capital

def plot_authorized_capital(total_authorized_capital):
    """
    Plots a bar chart showing the distribution of companies by their authorized capital range.

    Args:
        total_authorized_capital (dict):A dictionary with capital range
        labels as keys and the number of companies in each range as values.
    """
    plt.figure(figsize=(14,6))
    plt.title("Company With Authorized Capital Count")
    plt.bar(total_authorized_capital.keys(),
             total_authorized_capital.values(), color="skyblue", width=1)
    plt.xlabel("Authorized Capital")
    plt.ylabel("Company_count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

def execute():
    """
    Main execution function that:
    - Calculates the authorized capital distribution.
    - Plots the result as a bar chart.
    """
    authorized_capital = calculate_authorized_capital()
    plot_authorized_capital(authorized_capital)

if __name__ == "__main__":

    execute()
