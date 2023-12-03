# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Debugging information
RUN echo "Checking installed packages:" && \
    pip freeze && \
    echo "End of installed packages check."

# Make port 9999 available to the world outside this container
EXPOSE 9999

# Run app.py when the container launches
CMD ["python", "./server/scraper.py"]
