# The "buster" flavor of the official docker Python image is based on Debian and includes common packages.
FROM python:3.8-buster

# Create the working directory
RUN set -ex && mkdir /repo
WORKDIR /repo

# Copy only the relevant directories to the working diretory
RUN pwd
RUN ls
COPY ./code/text_recognizer ./text_recognizer/
COPY ./bot ./bot/

# Install Python dependencies
RUN set -ex && pip3 install -r bot/requirements.txt

# Run the web server
EXPOSE 8000
ENV PYTHONPATH /repo
CMD python3 /repo/bot/bot.py
