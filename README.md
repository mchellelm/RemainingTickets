# RemainingTickets

## What is RemainingTickets?

RemainingTickets is a Python program used to determine how many tickets are still available for purchase. It does this by iteratively opening incognito windows and adding all available tickets to cart, until it no longer can. It tracks how many tickets have been added in all the windows and returns the number of tickets available.

This program uses Python, Selenium, and ChromeDriver to achieve its goal. At time of writing, I'm using Python 3.9.9, Selenium 4.9.1 and ChromeDriver 113.0.5672.63 for Chrome version 113.

Currently, the code has been designed for Ticketbooth (namely [this](https://events.ticketbooth.com.au/event/marlo-altitude-sydney) event). As a result, there are hard coded values specifically for this event, such as element ids.

## How to Run

To run this program, make sure you have Python and Selenium installed. I would also replace the chromedriver_mac64 directory for one that corresponds with your system ([download here](https://chromedriver.chromium.org/downloads)).

Then all you have to do is run `python RemainingTickets.py` 
