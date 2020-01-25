These two files need to be executed BEFORE the main script in order to collect data.

I used the scrapy library: https://scrapy.org/ I didn't need to touch a lot to the template they give on their front page, but keep in mind you'll need to install the library to use these scripts.
Be also extremely careful to execute these scripts where the library has been installed. You also need to think about exporting the results to a .json file (for example, the command I used to run the characters-spiders.py script and export the results to a .json file is "scrapy runspider nietzsche-spiders-eng.py -o quotes.json", which gave the quotes.json file I'm using with main.py)
