# Using the latest LTS version of Ubuntu as our base image
FROM ubuntu:latest

# Labels for metadata
LABEL maintainer="your_email@domain.com" \
      version="1.0" \
      description="Jellyfin Media Server Docker image"

# Update OS packages and install prerequisites
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y apt-transport-https

# Add Jellyfin apt repository
RUN echo "deb [arch=$(dpkg --print-architecture)] https://repo.jellyfin.org/ubuntu focal main" | tee /etc/apt/sources.list.d/jellyfin.list \
    && apt-get update \
    && apt-get install -y jellyfin

# Expose ports
EXPOSE 8096 8920

# Set volume for Jellyfin data
VOLUME /config /media

# Define healthcheck
HEALTHCHECK --interval=60s --timeout=3s \
  CMD curl --fail http://localhost:8096/ || exit 1

# Start Jellyfin server
CMD ["jellyfin", "--datadir", "/config", "--cachedir", "/cache"]
