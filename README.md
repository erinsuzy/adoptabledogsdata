🐶 Adoptable Dog Listing Scraper

This project is a web scraper that extracts available dog listings from a local adoption site for data analysis. It gathers each dog's name, breed, and gender, saving the information in a structured format for further analysis.

🚀 Features

  Scrapes dog listing fron the Needy Paws adoption page
  Removes unnecessary prefixes (e.g., "Dog - " from breed names)
  Saves data as a CSV file for easy analysis


🛠️ Technologies Used

  Helium (built on Selenium) for browser automation
  BeautifulSoup for HTML parsing
  Pandas for data structuring and storage

📌 Setup Instructions

  Install dependencies (if not already installed):

  pip install helium beautifulsoup4 pandas

Run the script:

  python scraper.py

  The scraped data will be saved as dog_listings_cleaned.csv.

📊 Example Output
Name	Breed	Gender
Esther	Boxer / American Pit Bull Terrier	Female
Max	Labrador Retriever Mix	Male
Bella	Golden Retriever	Female

📜 License

This project is open-source under the MIT License.


![dog_adoption_gsd](https://github.com/user-attachments/assets/f3565c5e-3a37-486e-a951-80f8ed5d7b0c)
![dog_adoption_gender](https://github.com/user-attachments/assets/6a1d0585-f24d-41ae-a33c-d6d8ec89f285)
![dog_adoption_boxer](https://github.com/user-attachments/assets/fc2c2722-0f03-486d-94aa-c5575cd0d325)
