#################################
# Insert data to MySQL database #
#################################
import pandas as pd


calendar_dat = pd.read_csv('data/calendar.csv.gz')
listing_dat = pd.read_csv('data/listings.csv.gz')
reviews_dat = pd.read_csv('data/reviews.csv.gz')