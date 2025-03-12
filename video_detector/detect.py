"""
This module detects new videos on the canal.parlamento.pt plenário page.
It uses Selenium to scrape video links, checks a JSON file to see which videos
have already been processed, and triggers further processing if new videos are found.
"""

import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up Selenium with headless Chrome
chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# Define the target URL
URL = "https://www.canal.parlamento.pt"
driver.get(URL)

# Allow the page to load (adjust as necessary)
driver.implicitly_wait(10)

button = driver.find_element(by=By.ID, value="videos")

if button:
    button.click()

# Allow the page to load (adjust as necessary)
driver.implicitly_wait(10)

# Find video elements (update the selector based on actual page structure)
video_elements = driver.find_elements(by=By.CLASS_NAME, value="each_video")
new_videos = []

# TODO: getting the videos, but the url of the videos is hidden, found another
# way using a request to the frontend, but would like to keep this as backup if
# one day the frontend request changes.

# Load the list of processed videos (if available)
PROCESSED_FILE = "processed_videos.json"
if os.path.exists(PROCESSED_FILE):
    with open(PROCESSED_FILE, "r", encoding="utf-8") as f:
        processed_videos = json.load(f)
else:
    processed_videos = []

# Check each video and identify new ones
for video in video_elements:
    print(video)
    video_url = video.get_attribute("href")
    if video_url not in processed_videos:
        new_videos.append(video_url)
        processed_videos.append(video_url)
        # Optionally trigger downstream processing here

# Trim the processed videos list to the 30 most recent entries
if len(processed_videos) > 30:
    processed_videos = processed_videos[-30:]

# Save the updated list
with open(PROCESSED_FILE, "w", encoding="utf-8") as f:
    json.dump(processed_videos, f)

driver.quit()

# Log the detected new videos
if new_videos:
    print("New videos detected:")
    for url in new_videos:
        print(url)
else:
    print("No new videos found.")
