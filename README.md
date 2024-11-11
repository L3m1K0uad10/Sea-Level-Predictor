## Sea Level Predictor

This project is about analyzing a dataset of the global average sea level change since 1880


#### Goal
predict the sea level change through year 2050.


#### Project content
* Using Pandas to import the data from __epa-sea-level.csv__.
* Using matplotlib to create a scatter plot using the Year column as the x-axis and the __CSIRO Adjusted Sea Level__ column as the y-axis.
* Using the __linregress__ function from __scipy.stats__ to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
* Plotting a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
* Setting The x label to __Year__, the y label to __Sea Level (inches)__, and the title to __Rise in Sea Level__.