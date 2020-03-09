FROM python:3-alpine

# Exposes the default test development server on post 5000. 
# Consumer needs to map to this port using either randon (-P) or single specific (-p) to docker run
EXPOSE 5000

# Create directory for app install. Consider changes when we use NGINX or APACHE
RUN mkdir -p /root/citysync/
ADD citysync /root/citysync/

# Copy readymade data seeded TEST sqlite3 database. Consider changes when we use PostgreSQL 
COPY database-devel.sqlite3 /root/citysync/

# Install the requirements. Need a base version of python 3.6 at the least. 
WORKDIR /root/citysync/
RUN pip install -r requirements.txt

# Start the development server
ENTRYPOINT [ "python3" ]
CMD ["-u", "manage.py" ]
