FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nodejs \
    npm \
    git \
    curl \
    wget \
    openssh-client \
    nmap \
    dnsutils \
    whois \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /matus

# Copy repository
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir \
    requests \
    beautifulsoup4 \
    paramiko \
    pycryptodome \
    scapy \
    netaddr \
    dnspython \
    flask

# Install Node dependencies
RUN npm install

# Expose port
EXPOSE 3000

# Set entry point
ENTRYPOINT ["npm", "start"]

# Labels
LABEL maintainer="sanjaynain754"
LABEL description="MATUS ULTIMATE - Penetration Testing and Bug Bounty Framework"
LABEL version="1.0.0"
