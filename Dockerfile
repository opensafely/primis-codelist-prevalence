FROM ebmdatalab/datalab-jupyter:python3.8.1-2328e31e7391a127fe7184dcce38d581a17b1fa5

RUN apt-get update && apt-get install -y unixodbc-dev dos2unix

# Install Microsoft stuff needed to install Pyodbc and access a SQL Server
# database
COPY install_mssql.sh /tmp/
# Because git on Windows will rewrite the line-endings, and because bash can't
# tolerate DOS line-endings we need to fix them first
RUN dos2unix /tmp/install_mssql.sh && bash /tmp/install_mssql.sh

# Set up jupyter environment
ENV MAIN_PATH=/home/app/notebook

# Install pip requirements
COPY requirements.txt /tmp/
# Hack until this is fixed https://github.com/jazzband/pip-tools/issues/823
RUN chmod 644 /tmp/requirements.txt
RUN pip install --requirement /tmp/requirements.txt

EXPOSE 8888

# This is a custom ipython kernel that allows us to manipulate
# `sys.path` in a consistent way between normal and pytest-with-nbval
# invocations
COPY config/kernel.json /tmp/kernel_with_custom_path/kernel.json
RUN jupyter kernelspec install /tmp/kernel_with_custom_path/ --user --name="python3"

COPY . /home/app/notebook

CMD cd ${MAIN_PATH} && PYTHONPATH=${MAIN_PATH} jupyter lab --config=config/jupyter_notebook_config.py
