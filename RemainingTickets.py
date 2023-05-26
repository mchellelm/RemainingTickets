from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless") # Enable headless mode

# Set path to chromedriver executable (download and save on your machine)
chromedriver_path = "/chromedriver_mac64/chromedriver"

# Define the desired web page URL
url = "https://events.ticketbooth.com.au/event/marlo-altitude-sydney"

# Variable to store the number of tickets
num_of_tickets = 0

# Variable to store the maximum number of tickets purchaseable at once
max_tickets = 10

# Condition based on known capacity of venue
while num_of_tickets < 20000:
    # Initialize Chrome webdriver with the provided path and options
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

    # Navigate to the desired web page
    driver.get(url)

    # Find the <select> element by ID
    select_element = driver.find_element("id", "select_level_37858542")

    # Create a Select object from the <select> element
    select = Select(select_element)

    # Get the number of options
    num_options = len(select.options)

    # If the number of options is less than max_tickets, exit the loop
    if num_options < max_tickets:
        break

    # Increment the number of tickets
    num_of_tickets += max_tickets

    # Print number of tickets
    print("Current number of tickets: ", num_of_tickets)

    # Select the option with value "10"
    select.select_by_value(str(max_tickets))

    # Find the button by its text
    button = driver.find_element("id", "submit_ticket_request")

    # Click on the button
    button.click()

num_of_tickets += num_options

# Print the final number of tickets
print("Total number of tickets: ", num_of_tickets)

# Close the browser
driver.quit()