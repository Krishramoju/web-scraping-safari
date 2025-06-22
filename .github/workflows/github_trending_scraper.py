import requests
from bs4 import BeautifulSoup
import csv
import os

def scrape_github_trending():
    url = "https://github.com/trending"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        # Send HTTP request
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all repository articles
        repos = soup.find_all('article', class_='Box-row', limit=5)
        
        # Prepare data for CSV
        trending_repos = []
        for repo in repos:
            # Extract repository name
            name_element = repo.find('h2', class_='h3')
            name = name_element.get_text(strip=True).replace('/', '').strip() if name_element else "N/A"
            
            # Extract repository URL
            relative_url = name_element.find('a')['href'] if name_element and name_element.find('a') else "N/A"
            url = f"https://github.com{relative_url}" if relative_url != "N/A" else "N/A"
            
            trending_repos.append({'repository name': name, 'link': url})
        
        # Save to CSV (overwrite existing file)
        with open('github_trending.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['repository name', 'link']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(trending_repos)
            
        print("Successfully scraped top 5 trending repositories and saved to github_trending.csv")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create empty CSV file if it doesn't exist
    if not os.path.exists('github_trending.csv'):
        with open('github_trending.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['repository name', 'link']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        print("Created empty github_trending.csv file")
    
    # Run the scraper
    scrape_github_trending()
