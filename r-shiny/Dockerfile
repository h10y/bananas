FROM rocker/r2u:24.04

RUN groupadd app && useradd -g app app
WORKDIR /home/app

RUN install2.r --error --skipinstalled shiny plotly e1071

COPY app .

RUN chown app:app -R /home/app
USER app
EXPOSE 3838
CMD ["R", "-e", "shiny::runApp(host='0.0.0.0', port=3838)"]
