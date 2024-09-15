import pandas as pd

# Load the dataset
file_name = "2017.csv"
df = pd.read_csv(file_name)

#1. Remove whitespace and Create a list of unique breeds

df['NormalizedBreed'] = df['Breed'].str.replace(' ', '').str.lower()
# A list of unique breeds is created using the unique() method
unique_breeds = df['NormalizedBreed'].unique().tolist()
print("Unique Breeds:", unique_breeds)

#2. Create a list of number of licenses by LicenseType of each unique breed

breed_license_counts_series = df.groupby(['NormalizedBreed', 'LicenseType']).size()
breed_license_counts = pd.DataFrame({'NormalizedBreed': breed_license_counts_series.index.get_level_values(0),
                                     'LicenseType': breed_license_counts_series.index.get_level_values(1),
                                     'Count': breed_license_counts_series.values})
# Converted to list
breed_license_counts_list = breed_license_counts.values.tolist()
print("\nNumber of Licenses by LicenseType of Each Unique Breed:")
for item in breed_license_counts_list:
    print(item)

#3. Find the top 5 popular dog names
# The top 5 most common dog names are identified using value_counts and nlargest
top_dog_names_series = df['DogName'].value_counts().nlargest(5)
top_dog_names = pd.DataFrame({'DogName': top_dog_names_series.index, 'Count': top_dog_names_series.values})
# Converted to list
top_dog_names_list = top_dog_names.values.tolist()
print("\nTop 5 Popular Dog Names and Their Counts:")
for item in top_dog_names_list:
    print(item)

# 4. Create a method to filter licenses issued within a given date range
def filter_licenses_by_date(start_date, end_date):
    """
    Filters the licenses issued within the specified date range.
    """
    # Convert 'IssueDate' to datetime format
    df['IssueDate'] = pd.to_datetime(df['IssueDate'], format='%Y-%m-%d')

    # Filter the DataFrame based on the provided date range
    mask = (df['IssueDate'] >= start_date) & (df['IssueDate'] <= end_date)
    filtered_df = df[mask]

    return filtered_df

# Example usage of the filter_licenses_by_date method
start_date = '2017-01-01'
end_date = '2017-12-31'
filtered_licenses = filter_licenses_by_date(start_date, end_date)

print("\nFiltered Licenses Issued Between {} and {}:".format(start_date, end_date))
print(filtered_licenses)
