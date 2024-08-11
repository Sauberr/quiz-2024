#!/bin/bash

celery -A config.celery_app.app worker -l ${CELERY_LOG_LEVEL} -c ${CELERY_NUM_WORKERS}
