# project-one

    The goal of this project was to find the most suitable location for PyResorts, a fictional company, to build a new resort in. 

First step: Data collection

    Make a weather api call for cities. Change timestamp to date time.

    Export as csv 

Second Step: Data Cleaning and additional collection 

    Read in cities csv file 

   Set temperature, humidity, Wind Speed, and cloudiness parameters to determine appropriate locations based on cliamte criteria. 
    
    Add columns for geoapi call to be placed into 

    Make geoapi call to find out what development is in the area. Make sure destinations have an airport present. Set a limit of how many hotels are present. Drop rows that don't fit criteria and make a new dataframe.  
    
    Make a bar graph of the cities with the fewset number of hotels
    Make two scatterplots with number of hotels and the x value and number of resturants and tourist attractions as the y values.

Third step: Find Crime rates in countries 
    Merge cities_airports_hotel_lim.csv (rename country column to ccs2 so it can merge with crime data) with crime_country_data_2023.csv 
    
    Replace cca2 with Country Tag in merged dataframe 

    Drop Countires with travel bans: Saudi Arabia and Iran 


Fourth Step: Make visuals for cities crime & hotels 
    Make a bar graph for the number of countries in the list of cities
    Make a bargraph for number of hotels in each city 
    Create a Scatterplot and lineregress for crime index and population 


Fifth Step: Final sorting to determine best locations 
    Set crimeindex lower than 55 
    Sort remaining rows in dataframe from lowest to highest 
    Make a new dataframe with the following columns: City	country	crimeIndex	pop2023	Max Temp	Humidity	Number of Hotels	Number of Resturants	Bodies of Water	Natural Places	Hospital	Date

    Sort by number of hotels lowest to hightest 

    Drop extra index row and re-assign index

Sixth Step: Create final visuals 
    Number of hotels in final city locations
    hv plot of cities to see where they are located  

Give recommentation based on locations that firstly have the lowest crime rate and then the lowest number of hotels. 