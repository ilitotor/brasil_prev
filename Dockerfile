# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /brasil_store
# Set the working directory to /brasil_store
WORKDIR /brasil_store
ADD requirements.txt /brasil_store/
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
# Copy the current directory contents into the container at /brasil_store
ADD /brasil_store /brasil_store

