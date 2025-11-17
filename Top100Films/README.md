# Top Movies Web Scraper

A Python script that scrapes archived data of Empire Online’s “Top 100 Movies” using `BeautifulSoup` and exports the list into a clean, formatted text file.
This project demonstrates web scraping, HTML parsing, working with archived pages, text processing, and file handling.

## Project Structure

TopMoviesScraper  
├── main.py # Main web scraping script  
├── movies.txt # Output file containing the ordered movie list  
└── README.md # This file  

## How It Works?

1. Sends a GET request to a **Wayback Machine snapshot** of the Empire Online website.
2. Parses the HTML using BeautifulSoup.
3. Extracts all movie titles from `<h3 class="title">` tags.
4. Reverses the list to produce the correct ranking (1 → 100).
5. Cleans text (removing incorrect characters from encoding issues).
6. Writes the final list into `movies.txt`, one title per line.

## Technologies Used

- **Python 3.12**
- **requests** → sending HTTP requests  
- **BeautifulSoup (bs4)** → parsing HTML  
- Basic file handling (`with open(...)`)

## Requirements
Install dependencies:
`pip install requests beautifulsoup4`

## How to Run?
`main.py`
A new file `movies.txt` will be generated containing the full ordered list of movie titles.

Example output is uploaded in *movies.txt*.
*(Note: actual titles depend on the scraped page)*

## Key Features

- Works with archived websites  
- Clean extraction using HTML tags & class names  
- Unicode cleanup for incorrect characters  
- Writes data in a well-formatted text file  
- Minimal, readable Python code  
- Great example of beginner-friendly web scraping 

## Future Improvements

- Save results as JSON or CSV    
- Detect encoding issues and auto-fix all invalid characters  
- Convert script into a reusable module  
- Add unit tests for parsing logic

## Notes

⚠️ **Always check website policies before scraping.**  
This project uses an archived site from Wayback Machine, which is safe for educational purposes.

