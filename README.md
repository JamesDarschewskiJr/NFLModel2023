# NFLModel2023
Model designed for predicting NFL playoff games

A few years ago, I started sports betting and learned about sportsbooks use probabilities to create the odds for which team will win or not. Starting with the 2021 postseason, I decided to create an algorithm for predicting which team will win. From the jump, this process predicted that the Bengals and Rams were capable of deep playoff runs, and they ended up playing for the Super Bowl in Inglewood, CA. Last season, the algorithm accurately predicted 9/13 spreads and 11/13 games straight up. This season, 9/13 games have been picked correctly, as well as 6/13 spreads per ESPN Bet.

Some of the numbers in the process are familiar to most football fans, like points per game and points given up a game. There are some more advanced numbers courtesy of FTN Fantasy (formerly Football Outsiders) such as team and unit DVOA (Defense-Adjusted Value Over Average). I also created a statistic for measuring total team strength with regards to the rest of the league called Standard Relative Strength or SRS. To calculate SRS, I multiplied FTN's strength of schedule by a team's point differential to get a relative strength of teh team, and then standardized that group of numbers so that an SRS of 100 represents an average team, with higher numbers indicating better teams and lower numbers indicating worse teams.

There are also some drawbacks to the code. This is a manual process, which means that results are not calculated unless I input the data. The data collection process is also manual, which means I am the one aggregating the data from different sources and compiling it into a spreadsheet before downloading the pared down version that the model takes. One last drawback is that while there is great success in predicting playoff games, regular season games and regular season spreads are not as accurate.

While this model has had its successes, that does not mean that I will be sitting on my laurels and not trying to improve this algorithm. In the regular season, home teams win between 50% and 60% of the time, while in the postseason home teams have won 67% of the time (since 1981, not including Super Bowls). The ultimate goal of this project is to be able to consistently pick games at a higher rate than those two clips. Currently, I am working on adding factors for travel, quarterback, and expected team performance (xSRS in the data) for making predictions, and automating the process to scrap the data and format it the way I need it to be formatted to run this model. These changes should be made in time for the start of the 2024 season, so there is more on the way. 

Hopefully this project is a good insight into how I've been predicting NFL games and the data behind it.
