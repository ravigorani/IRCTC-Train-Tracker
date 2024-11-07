# IRCTC Train Tracker

## Overview
IRCTC Train Tracker is a Python-based command-line application that allows users to access Indian Railways train information. Users can check the trains arriving at their station, PNR status, and station details of a particular train. The application interacts with the Indian Railways API to provide real-time data to users.

## Features
- **Check Trains from Your Station**: Get a list of trains arriving and departing from a specified station.
- **Check PNR Status**: Enter your PNR number to retrieve the status of your ticket.
- **Check Train Schedule**: View the full schedule of a train, including station names, arrival and departure times, and distance traveled.

## How It Works
1. Users will be prompted to choose one of the following options:
   - Check trains arriving and departing from a specific station.
   - Check the status of their PNR.
   - View the schedule of a specific train.
2. Depending on the selection, users will input either a station code, PNR number, or train number.
3. The program then makes API calls to Indian Railways API endpoints to fetch the required data and displays the information in a user-friendly format.

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/ravigorani/irctc-train-tracker.git
    cd irctc-train-tracker
    ```

2. **Install dependencies**:
    Ensure you have Python installed. Install the `requests` library using:
    ```bash
    pip install requests
    ```

3. **API Key Setup**:
    Replace `<apikey>` in the code with your actual API key from [Indian Railways API](https://indianrailapi.com/). Make sure to keep your API key secure.

## Usage
Run the script using Python:
```bash
python irctc_train_tracker.py
