FROM python:3-alpine

# Make the directory we will be installing app. Consider if using NGINX or APACHE
RUN mkdir -p /root/citysync/
WORKDIR /root/citysync/

COPY citysync /root/

# Already in folder so this is extraneous most likely
#COPY requirements.txt /root/citysync/

# Copy readymade data seeded TEST sqlite3 database. Consider when using PostgreSQL 
COPY database-devel.sqlite3 /root/citysync/

# Install the requirements. We need a base version of python 3.6 at the least. 
RUN pip install -r requirements.txt

# Start the developmental server
CMD [ "python", "-u", "manage.py" ]
