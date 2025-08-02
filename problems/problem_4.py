"""
This module analyzes company registration data to calculate and plot
aggregating registration counts over past 10 years by principal Business activity.

It reads data from the 'company_data.csv' and 'pincode.csv' files,
maps pincodes to districts, counts registrations, and displays
the result in a bar chart.
"""
import csv
import matplotlib
import matplotlib.pyplot as plt

# Set backend immediately after importing matplotlib
matplotlib.use('TkAgg')


def calculate_top_five_business_activity_past_ten_year():
    """
    Calculates the number of company registrations for the top 5 business activities 
    over the past 10 years.

    Reads data from 'company_data.csv', determines the top 5 most frequent business 
    activities by total registration count, and aggregates their yearly registration counts 
    for the most recent 10 years.

    Returns:
        dict: A dictionary where keys are top business activity names and values are 
              dictionaries of year-wise registration counts sorted by year.
    """
    activity_total_count = {}
    top_business_activity_count = {}
    years = []
    with open("../required_data/company_data.csv", encoding="utf-8") as company_file:
        company_data = list(csv.DictReader(company_file))

        for company in company_data:
            year = company["CompanyRegistrationdate_date"][:4]
            business_activity = company["CompanyIndustrialClassification"]
            activity_total_count[business_activity] =activity_total_count.get(str(business_activity),0) + 1

            if year not in years:
                years.append(year)

        years.sort(reverse=True)
        years = years[:10]
        sorted_five_business_activity = dict(sorted(activity_total_count.items(), key=lambda item : item[1],reverse=True)[:5])
        top_five_business_activity = [key for key in sorted_five_business_activity.keys()]

        for company in company_data:
            business_activity = company["CompanyIndustrialClassification"]
            year = company["CompanyRegistrationdate_date"][:4]

            if business_activity in top_five_business_activity and year in years:
                if business_activity not in top_business_activity_count:
                    top_business_activity_count[business_activity] = {}
                if year not in top_business_activity_count[business_activity]:
                    top_business_activity_count[business_activity][year] = 0
                top_business_activity_count[business_activity][year] += 1

    sorted_top_business_activity_count_by_year = {
        activity: dict(sorted(year_data.items(), key=lambda item: int(item[0])))
        for activity, year_data in top_business_activity_count.items()
    }

    return sorted_top_business_activity_count_by_year


def plot_top_five_business_activity_past_ten_year(data):
    """
    Plots a grouped bar chart of the top 5 business activities by registration count 
    over the past 10 years.

    Args:
        data (dict): A dictionary where keys are business activity names and values are 
                     dictionaries of year-wise registration counts.
    
    Displays:
        A grouped bar chart with years on the x-axis and number of registrations on the y-axis.
    """
    years = sorted(next(iter(data.values())).keys(), key=int)
    activities = list(data.keys())

    num_years = len(years)
    num_activities = len(activities)
    bar_width = 0.15
    group_gap = 0.25  # extra gap between year groups
    spacing = bar_width * num_activities + group_gap

    # Base positions for each year group
    x_positions = [i * spacing for i in range(num_years)]

    fig, ax = plt.subplots(figsize=(15, 7))

    for i, activity in enumerate(activities):
        offsets = [x + i * bar_width for x in x_positions]
        counts = [data[activity].get(year, 0) for year in years]
        ax.bar(offsets, counts, width=bar_width, label=activity)

    # Set x-ticks in the middle of each group
    mid_points = [x + (bar_width * num_activities / 2) for x in x_positions]
    ax.set_xticks(mid_points)
    ax.set_xticklabels(years, rotation=45)

    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Registrations')
    ax.set_title('Top 5 Business Activities by Registrations (Past 10 Years)')
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.show()


def execute():
    """
    Executes the full analysis pipeline.

    Calculates the top 5 business activities by company registrations over the past 10 years 
    and plots the result in a bar chart.
    """
    top_five_business_activity = calculate_top_five_business_activity_past_ten_year()
    plot_top_five_business_activity_past_ten_year(top_five_business_activity)


if __name__ == "__main__":

    execute()
