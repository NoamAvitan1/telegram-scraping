Telegram Data Scraping

This project allows you to scrape messages from your Telegram channels based on specified filters.

Setup Instructions
1. Get Your Telegram API Credentials

    Visit Telegram API - https://my.telegram.org/auth.
    Enter your phone number and complete the validation process. A password 
    will be sent to your Telegram app.

    After authentication, select "API development tools".

    Create a new application with the following details:
        App title: testing
        Short name: testing
        URL: my.telegram.org
        Platform: Android
        Description: testing
        Click "Create application".

    On the next screen, press "Save". You will see your api_id and hash_id.

2. Set Up Your Environment Variables
    Create a .env file in your project directory with the following content:
        api_id = "your api id"
        hash_id = "your hash id"

3. Install and Activate Virtual Environment
    Open your terminal and navigate to your project directory:
        cd telegram-data-scraping
    Activate the virtual environment:
        ./venv/Scripts/activate

4. Run the Script
    Execute the main script:
        python main.py
    When prompted, enter the following details in the terminal:
        Channel name: The name of the Telegram channel you want to scrape.
        Number of messages: The number of messages you want to retrieve.
        Message filter: The specific message content you want to filter.

5. View the Output
    Once the script completes, open output.xlsx with Excel to view the 
    scraped data.
