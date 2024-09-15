import pandas as pd

file_name = "2017.csv"
df = pd.read_csv(file_name)

#1. Remove whitespace and Create a list of unique breeds

df['NormalizedBreed'] = df['Breed'].str.replace(' ', '').str.lower()
unique_breeds = df['NormalizedBreed'].unique().tolist()
print("Unique Breeds:", unique_breeds)

#2. Create a list of number of licenses by LicenseType of each unique breed

breed_license_counts_series = df.groupby(['NormalizedBreed', 'LicenseType']).size()
breed_license_counts = pd.DataFrame({'NormalizedBreed': breed_license_counts_series.index.get_level_values(0),
                                     'LicenseType': breed_license_counts_series.index.get_level_values(1),
                                     'Count': breed_license_counts_series.values})
breed_license_counts_list = breed_license_counts.values.tolist()
print("\nNumber of Licenses by LicenseType of Each Unique Breed:")
for item in breed_license_counts_list:
    print(item)

#3. Find the top 5 popular dog names

top_dog_names_series = df['DogName'].value_counts().nlargest(5)
top_dog_names = pd.DataFrame({'DogName': top_dog_names_series.index, 'Count': top_dog_names_series.values})
top_dog_names_list = top_dog_names.values.tolist()
print("\nTop 5 Popular Dog Names and Their Counts:")
for item in top_dog_names_list:
    print(item)