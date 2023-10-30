# Используем официальный образ Python 3 в качестве базового образа
FROM python:3

# Установка Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    /bin/bash miniconda.sh -b -p /usr/local/miniconda && \
    rm miniconda.sh

# Копирование environment.yml в контейнер
COPY environment_bioinform_platform.yml /app/

# Создание Conda-окружение и установка зависимости из environment.yml
# Активация Conda и создание Conda-окружения
SHELL ["/bin/bash", "-c"]
RUN source /usr/local/miniconda/etc/profile.d/conda.sh && \
    conda env create -f /app/environment_bioinform_platform.yml

# Активация Conda-окружения
RUN echo "source activate environment_bioinform_platform.yml" > ~/.bashrc
ENV PATH /opt/conda/envs/environment_bioinform_platform.yml/bin:$PATH

# Копирование Django проекта
COPY dna_liv /app