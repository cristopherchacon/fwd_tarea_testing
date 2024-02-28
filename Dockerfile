FROM python:3.12-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the Gemfile and Gemfile.lock to the container
COPY . .

# Install the gems
RUN pip install pytest

# Copy the application code to the container
COPY . ./app

# Set the default command to run RSpec
CMD ["pytest", "game_test.py"]
