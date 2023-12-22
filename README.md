#Hello
# Web Scraper with Flask API
This project is a simple web scraper implemented using Flask, BeautifulSoup, and Requests. It exposes a Flask API that accepts a URL as a query parameter and returns information about the title and category of the specified URL.

## Prerequisites

- Docker and Docker Compose installed on your machine.

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-web-scraper.git
    cd your-web-scraper
    ```

2. **Run the script to build and start the Docker containers:**

    ```bash
    ./run.sh
    ```

    This will build the Docker image and start the Flask server on `http://127.0.0.1:9999`.

## API Usage

Send a GET request to the `/scraper` endpoint with the `url` query parameter:

```bash
curl -X GET "http://127.0.0.1:9999/scraper?url=https://www.example.com"
jbkjbjln 
