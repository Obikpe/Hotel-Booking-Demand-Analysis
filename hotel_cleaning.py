import pandas as pd
import numpy as np
df = pd.read_excel('Hotel bookings.xlsx', sheet_name='hotel_booking',engine='openpyxl')
df.head(2)
df.describe()
df.info()

# Dropping ireelevant columns for present analysis
df.drop(columns=['agent','company'], inplace=True)
df.head(2)
df.drop(columns = ['email','phone-number','credit_card'], inplace=True)

#filling missing values in the 'children' column with 0, as it is reasonable to assume that if the number of children is not specified, it is likely that there are no children in the booking.
df.fillna({'children': 0}, inplace=True)
#filling missing values in the 'country' column with 'Unknown', as it is reasonable to assume that if the country is not specified, it is unknown. This helps to maintain data integrity and allows for better analysis of the dataset without losing rows due to missing values.
df.fillna({'country': 'Unknown'}, inplace=True)

# Creating a Total Kids and Total Guest Column

df['total_kids'] = df['children'] + df['babies']
df['total_guests'] = df['adults'] + df['total_kids']
df['total_nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']

#Saving Cleaned Data to a new csv file
df.to_csv('CLEANED_DATA.csv', index=False)