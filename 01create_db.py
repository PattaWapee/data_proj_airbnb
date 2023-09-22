#############################
### Create MySQL database ###
#############################
import pandas as pd
import connect_MySQL


#Myconnect = connect_MySQL.create_server_connection("localhost", "user_proj", "Data3333!")
Myconnect = connect_MySQL.create_server_connection("localhost", "user_proj", "Data3333!", "airbnb_db")
#cursor = connect_MySQL.create_database(Myconnect, "airbnb_db")

create_table_query = """
    CREATE TABLE `Host` (
        `host_id` int,
        `host_url` varchar(255),
        `host_name` varchar(255),
        `host_since` datetime,
        `host_location` varchar(255),
        `host_is_superhost` boolean,
        `host_listing_count` int,
        `host_response_rate` numeric,
        `host_response_time` numeric,
        PRIMARY KEY (`host_id`)
    );
    CREATE TABLE `Listing` (
        `listing_id` int,
        `host_id` int,
        `listing_url` varchar(255),
        `price` int,
        `number_of_reviews` int,
        `review_scores_rating` numeric,
        `review_scores_accuracy` numeric,
        PRIMARY KEY (`listing_id`)
    );
    CREATE TABLE `Calendar` (
        `listing_id` int,
        `date` datetime,
        `available` boolean,
        `price` numeric,
        `minimum_nights` int,
        `maximum_nights` int,
        PRIMARY KEY (`listing_id`)
    );
    CREATE TABLE `Review` (
        `review_id` int,
        `listing_id` int,
        `reviewer_id` int,
        `date` datetime,
        `comment` varchar(255),
        PRIMARY KEY (`review_id`)
    );
    CREATE TABLE `Property` (
        `listing_id` Int,
        `address` varchar(255),
        `neighbourhood` varchar(255),
        `property_type` varchar(255),
        `room_type` varchar(255),
        `latitude` numeric,
        `longtitude` numeric,
        `bathrooms` int,
        `bedrooms` int,
        `beds` int,
        `accommodates` int,
        `minimum_nights_avg_ntm` numeric,
        `maximum_nights_avg_ntm` numeric,
        PRIMARY KEY (`listing_id`)
    );"""


cursor = connect_MySQL.execute_query(Myconnect, create_table_query, multi=True)

connect_MySQL.close_connection(Myconnect, cursor)