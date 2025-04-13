#Uses Python 3.7 as the base image
FROM python:3.7-slim-buster

#update the package list and install awscli for interacting with aws services
RUN apt update -y && apt install awscli -y

#Sets the working directory inside the container to /app.
#All subsequent commands run inside this directory.
WORKDIR /app

#Copies everything from the project directory on the host machine to /app in the container.
COPY . /app
RUN pip install -r requirements.txt

#Defines the default command that runs when the container starts.
CMD ["python3", "app.py"]