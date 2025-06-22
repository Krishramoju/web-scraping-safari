# GitHub Trending Repositories Scraper

This Python script scrapes the top 5 trending repositories from GitHub's trending page (https://github.com/trending) and updates a CSV file with the results.

## Project Structure

- `github_trending_scraper.py`: The main Python script
- `github_trending.csv`: Initially empty CSV that gets populated when the script runs
- `README.md`: This documentation file

## Features

- Starts with an empty CSV file containing just headers
- Updates the CSV with current top 5 trending repositories when run
- Includes proper error handling
- Creates the CSV file if it doesn't exist

## Requirements

- Python 3.x
- requests library (`pip install requests`)
- BeautifulSoup4 library (`pip install beautifulsoup4`)

## Usage

1. Clone this repository
2. Install the required dependencies
3. Run the script:
