# CodeChef Profile Scraper
This project is a Python-based web scraper that extracts profile data from CodeChef using the Beautiful Soup library. The script fetches details like user ratings, solved problems, and contest history, making it easier to gather and analyze CodeChef data programmatically.

# Features:
- User Profile Data Extraction: Scrape and extract information such as ratings, number of problems solved, and contest history from a CodeChef profile.
- HTML Parsing: Utilizes the Beautiful Soup library to parse HTML content and efficiently extract relevant data.
- Efficient and Simple: The project is designed to be lightweight, easy to understand, and quick to set up.
# Requirements:
- Python 3.x
- Beautiful Soup 4
- Requests
# Installation:
1. Clone the Repository:
- git clone https://github.com/Catalyst20104/web-scrapping-of-codechef-using-python.git
- cd codechef-profile-scraper
2.Install Dependencies:Ensure you have Python installed, then install the required Python packages:
- pip install beautifulsoup4 requests
# Usage:
1. Run the Script: To scrape a CodeChef profile, simply run the script with the desired username:
1. python python.py <username>
2. Replace <username> with the actual CodeChef username you want to scrape.
3.Example:
- python python.py johndoe
  
This will output details like ratings, solved problems, and contest history for the user "johndoe".
3. Customize the Script: You can customize the script to extract additional data or save the output in different formats (e.g., CSV, JSON).
# Project Structure:
- python.py: The main script for scraping and parsing CodeChef profiles.
- README.md: Project documentation.
