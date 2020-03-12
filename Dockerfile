FROM python:3-alpine

# Create directory for app install. Consider changes when we use NGINX or APACHE
RUN mkdir -p /root/citysync/
ADD citysync /root/citysync/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install the requirements. Need a base version of python 3.6 at the least. 
WORKDIR /root/citysync/
RUN pip install -r requirements.txt

# Exposes the default test development server on post 5000. 
# Consumer needs to map to this port using either randon (-P) or single specific (-p) to docker run
EXPOSE 5000

# Start the development server
ENTRYPOINT [ "python3" ]
CMD ["-u", "manage.py" ]
