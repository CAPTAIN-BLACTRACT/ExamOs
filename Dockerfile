# Use a minimal Debian base image, as our OS is based on it.
FROM debian:bookworm-slim

# Set non-interactive frontend to avoid prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install the necessary tools for building the live OS.
# - live-build is the core tool.
# - sudo is required by the live-build process.
RUN apt-get update && apt-get install -y \
    live-build \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container.
# Our project files will be mounted here.
WORKDIR /app

# The command that will be executed when the container starts.
# It runs the live-build process to generate the ISO.
CMD ["sudo", "lb", "build"]
