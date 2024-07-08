#!/bin/bash

celery -A config.celery_app.app worker -l ${CELERY_LOG_LEVEL} -S django