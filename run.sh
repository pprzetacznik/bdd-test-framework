#!/bin/bash

set -x

export FLASK_DEBUG=${FLASK_DEBUG:-1}
export FLASK_APP=my_app/autoapp.py
export FLASK_ENV=${FLASK_ENV:-dev}

ACTION=${1:-run}

case $ACTION in
  run)
    flask run --port=8002
    ;;
  shell)
    flask shell
    ;;
  *)
    exec "$@"
    ;;
esac
