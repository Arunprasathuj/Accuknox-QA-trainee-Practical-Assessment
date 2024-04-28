# Use a base image with Ubuntu
FROM ubuntu:latest

# Install required packages
RUN apt-get update && \
    apt-get install -y dos2unix bash cowsay fortune netcat-openbsd

# Create symbolic links for cowsay and fortune
RUN ln -s /usr/games/cowsay /usr/local/bin/cowsay && \
    ln -s /usr/games/fortune /usr/local/bin/fortune

# Copy the script into the container
COPY wisecow.sh /usr/local/bin/wisecow.sh

# Convert line endings in the script file to Unix-style
RUN dos2unix /usr/local/bin/wisecow.sh

# Make the script executable
RUN chmod +x /usr/local/bin/wisecow.sh

# Expose the port used by the server
EXPOSE 4499

# Command to run the application
CMD ["wisecow.sh"]
