FROM rocker/r-ver:3.5.3

RUN apt-get update && apt-get install -y \
    sudo \
    gdebi-core \
    pandoc \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev \
    libxt-dev \
    xtail \
    wget


# Download and install shiny server
RUN wget --no-verbose https://download3.rstudio.org/ubuntu-14.04/x86_64/VERSION -O "version.txt" && \
    VERSION=$(cat version.txt)  && \
    wget --no-verbose "https://download3.rstudio.org/ubuntu-14.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb && \
    gdebi -n ss-latest.deb && \
    rm -f version.txt ss-latest.deb && \
    . /etc/environment && \
    R -e "install.packages(c('shiny', 'rmarkdown'), repos='$MRAN')" && \
    cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/ && \
    chown shiny:shiny /var/lib/shiny-server

EXPOSE 3838

# TODO - create user
RUN mkdir -p /home/shinymap/app
COPY . /home/shinymap/app

WORKDIR /home/shinymap/app
RUN R -e 'install.packages("udunits2_0.13.tar.gz",configure.args=" --with-udunits2-include=/usr/include/udunits2")'
RUN R -e 'install.packages("packrat" , repos="http://cran.us.r-project.org"); packrat::restore()'

CMD ["Rscript app.R"]
