# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory to server
WORKDIR /content

# Copy the file into the directory
COPY . /content

# Install any needed packages as in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to world outside
EXPOSE 5000

# Run app.py when container launches
CMD ["python", "app.py"]
