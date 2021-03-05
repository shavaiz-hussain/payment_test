FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
ADD ./requirements.txt /app/requirements.txt

# Install the pip requirements file depending on
# the $ENV build arg passed in when starting build.
RUN pip install -Ur requirements.txt

# Copy the rest of our application.
COPY . /app/
