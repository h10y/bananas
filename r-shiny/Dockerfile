FROM rocker/r2u:24.04
RUN install.r remotes renv pak rconfig jsonlite yaml deps
RUN cp /usr/lib/R/site-library/deps/examples/03-cli/deps-cli.R /usr/local/bin/deps-cli
RUN chmod +x /usr/local/bin/deps-cli

RUN groupadd app && useradd -g app app
WORKDIR /home/app

COPY app/dependencies.json .
RUN deps-cli install
# RUN R -q -e "install.packages('shiny')"

COPY app .

RUN chown app:app -R /home/app
USER app
EXPOSE 3838
CMD ["R", "-e", "shiny::runApp(host='0.0.0.0', port=3838)"]
