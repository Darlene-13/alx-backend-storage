#Docker file for REDIS basic project

FROM ubuntu:18.04
#Preventive interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

#Update package list and install dependencies
RUN apt-get update && apt-get install -y \
    python3.7 \
    python3-pip \
    redis-server \
    vim \
    nano \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create symbolic link for python3
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1


# Install python packages and dependencies
RUN pip3 install --upgrade pip && \
    pip3 install redis pycodestyle

#Configure Redis to bind localhost 
RUN sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf && \
    sed -i "s/protected-mode yes/protected-mode no/g" /etc/redis/redis.conf

#Create a workiing directory
WORKDIR /app

# SET default command
CMD ["/bin/bash"]