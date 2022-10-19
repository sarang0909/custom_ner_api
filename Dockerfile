# Start from official miniconda image
FROM continuumio/miniconda3

# This will be our base folder in image where we'll put src and environment.yml
WORKDIR /code

# Copy environment.yml
COPY ./environment.yml /code/environment.yml

# Install all dependencies
RUN conda env create -f environment.yml


# Activate conda environment/Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "custom_ner_api", "/bin/bash", "-c"]

# Copy source code and config
COPY ./src /code/src
COPY ./config /code/config
COPY ./main.py /code/

# Entrypoint for main script
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "custom_ner_api", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]