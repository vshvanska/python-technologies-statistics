# Job Vacancy Analysis Project
Overview
The Job Vacancy Analysis Project is a Python-based project that aims to gather and analyze job postings for Python developers from the Djinni.co website. The project utilizes the Scrapy framework for web scraping and provides insights into various aspects of the job market, including vacancies, views, and reviews.

Features
- Web Scraping: Utilizes Scrapy to crawl and extract relevant information from job postings.

- Data Analysis: Provides statistical analysis on the collected data, including information on vacancies, views, and reviews.

- Experience Requirement: Analyzes and presents insights into the experience required for Python developer positions.

- Location Insights: Offers statistics and trends related to the geographical locations of job vacancies.

- Technology Trends: Identifies and presents the most commonly mentioned technologies in job postings.

- Relationships: Explores correlations between reviews, required experience, and specific technologies.

# Installation
1. Fork the repo (GitHub repository)
2. Clone the forked repo
    ```
    git clone the-link-from-your-forked-repo
    ```
    - You can get the link by clicking the `Clone or download` button in your repo
3. Open the project folder in your IDE
4. Open a terminal in the project folder

5. If you are using PyCharm - it may propose you to automatically create venv for your project 
    and install requirements in it, but if not:
    ```
    python -m venv venv
    venv\Scripts\activate (on Windows)
    source venv/bin/activate (on macOS)
    pip install -r requirements.txt
    ```

To run the project locally, follow these steps:
- Run scrapy:
    ```
    scrapy crawl vacancies -o data.csv
    ```
After running the project, you will find the extracted data in the data.csv file.

Run main.ipynb to analyse data.

In the archive folder you can find previous results for comparing statistics.
Data is automatically saved to this folder
