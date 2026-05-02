# Sport Schedule To Calendar

## Introduction
A "Scraping &amp; Automation" project. It sits at the intersection of data engineering (getting the data) and system automation (doing something with it).

While "scraping" usually means extracting data from a webpage's HTML, for a project like this, you actually have two main paths: the Scraping Route (extracting from a website) or the API Route (getting structured data directly). 

## Implementation Design
Since I am looking at this from a backend perspective, using a dedicated library is much more robust. FastF1 is the gold standard for Python. It handles the data fetching for you and gives you clean, structured objects. Thus, I have chosen the API Route.

The easiest way to "add to calendar" without dealing with complex OAuth2 credentials for the Google API is to generate an .ics file. You can then import this file into Google, Apple, or Outlook.

## Adding To Calendar
Find the File: You will see a new file named F1_2026_Schedule.ics in your folder.

Add to Calendar:
- Google Calendar: Go to Settings -> Import & Export -> Import. Select the .ics file.

- Apple/Outlook: Just double-click the file, and it should prompt you to add the events to your calendar.
