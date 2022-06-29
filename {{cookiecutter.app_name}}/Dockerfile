################################################################################
### Builder Image
################################################################################

FROM 778129680386.dkr.ecr.us-east-1.amazonaws.com/gumgum/ops/python-builder:3.7 AS builder
LABEL maintainer="{{ cookiecutter.author_fullname }} <{{ cookiecutter.author_email }}>"

ARG PIP_EXTRA_DEV_DEPS
ENV PIP_EXTRA_DEV_DEPS $PIP_EXTRA_DEV_DEPS

ENV PYTHON_VERSION 3.7
ENV PYTHONUSERBASE /venv
ENV PYTHONPATH /venv/lib/python${PYTHON_VERSION}}/site-packages
ENV PATH $PATH:/venv-dev/bin:/venv/bin

# RUN apt-get update \
#   && apt-get install -y \
#   ${PACKAGE} \
#   && apt-get clean \
#   && rm -rf /var/lib/apt/lists/*

# Copy files needed to install app requirements
COPY ./*requirements.txt /src/
COPY ./docker/pip.config /etc/pip.conf

# Install app requirements in virtualenv
RUN mkdir /venv \
  && pip3 install -I -U  pip \
  && pip3 install -I -U pyopenssl cryptography certifi idna ndg-httpsclient pyasn1 singledispatch ${PIP_EXTRA_DEV_DEPS}\
  && pip3 install --user -r /src/requirements.txt

# Copy the source code into the container
COPY . /src

################################################################################
### Production Image
################################################################################

FROM 778129680386.dkr.ecr.us-east-1.amazonaws.com/gumgum/ops/python:3.7
LABEL maintainer="{{ cookiecutter.author_fullname }} <{{ cookiecutter.author_email }}>"

ENV TZ=America/Los_Angeles
ENV PYTHON_VERSION 3.7
ENV PYTHONPATH /:/venv/lib/python${PYTHON_VERSION}/site-packages
ENV PYTHONUNBUFFERED=1
ENV PATH $PATH:/venv/bin

ENV AWS_DEFAULT_REGION=us-east-1

# RUN apt-get update \
#   && apt-get install -y \
#   <PACKAGE>
#   && apt-get clean \
#   && rm -rf /var/lib/apt/lists/*

# Make application folders
RUN mkdir /var/log/gumgum \
  && chown ggapp:ggapp /var/log/gumgum

WORKDIR /app
USER ggapp

# Copy the app and its dependencies
COPY --from=builder /src/app /app
COPY --from=builder /venv /venv

CMD ["/usr/bin/dumb-init", "python3",  "__main__.py"]
