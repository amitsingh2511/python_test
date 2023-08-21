import requests
from bs4 import BeautifulSoup
import re


def test(url, target_words, snapsort_text):
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()

        # total_word_count = count_words(text)
        words = re.findall(r'\b\w+\b', text)
        total_word_count = len(words)

        matched_words = {word: text.lower().count(word.lower()) for word in target_words}

        snapsort_text_exists = snapsort_text.lower() in text.lower()

        if snapsort_text_exists:
            with open("snapsort.txt", 'w',encoding='utf-8') as file:
                file.write(snapsort_text)

        return total_word_count, matched_words, snapsort_text_exists
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None, None

# Input URL
url = "https://www.indiatoday.in/india/story/new-expressway-kashmir-kanyakumari-cag-report-nitin-gadkari-2423440-2023-08-19"

#Input snapsort word
snapsort_text = "From"

# List of target words to match
target_words = ["lunch", "From"]

total_word_count, matched_words, snapsort_text_exists = test(url, target_words, snapsort_text)

if total_word_count is not None:
    print(f"Total word count: {total_word_count}")
    print(f"Matched words count with key: {matched_words}")
    if snapsort_text_exists:
        print("'snapsort_text' found in the page and saved to 'snapsort.txt'")
    else:
        print("'snapsort_text' not found in the page")
