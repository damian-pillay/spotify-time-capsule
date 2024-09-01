1. Introduction
    - This cool project generates a Spotify playlist of the top 100 songs from any user-inputted date
    - The purpose of this project was to gain some experience with webscraping and API Integration
    - I also saw this as an excuse to merge my love for music with my love for coding.

2. Features
    - Web scraping Billboard Hot 100 to retrieve top 100 songs from any date
    - Spotify API integration to create and populate playlists
    - User-friendly interface for inputting dates
    - Error-Handling and Robust Coding Practices

3. Technologies Used
    - Python
    - BeautifulSoup
    - Spotify API
    - Spotipy (Spotify Library for Python)

4. Setup and Installation
    - Make sure to create a .env file and to replace the global variables with your own credentials, within that .env file (You can get these credentials by making an app on the spotify website via spotify developer tools)
    - On the first run of the program, a chrome tab will pop up asking for permission. Click accept and you will be redirected. Copy the redirected link into the Python terminal. Thereafter you may use the program as prompted.

5. Usage
    - Inputting dates 
        - You will be prompted for Year, Month and Day respectively. Put only positive numerical values
        - You are free to put any date you desire, if a date doesn't have a top 100 list, it will count as an invalid date, and you will be reprompted. (billboard only has list from the year 1958 onwards)
    
    - Generating playlists
        - the playlist will be made and populated automatically

6. Challenges and Limitations
    - Difficulty mainly stemmed from reading the Spotify API documentation, as it is sometimes unclear.
    - Due to the nature of Python and the processes required by the spotify API, the code takes about 30-50 seconds to generate the playlist

7. Future Development
    - I would like to develop more features within the SpotifyManager() class like, playlist deletion, top 10 albums etc
    - maybe also a better interface like a GUI
    - time will tell...

8. License
    - No License is attached to this. You are free to alter and use this code as you wish!

9. Contact
    - If you have any questions, please feel free to contact me at any time
    - email: damianleep@gmail.com