#!/bin/bash

cd /Users/denizerenozer/python-postgres-etl

/Users/denizerenozer/python-postgres-etl/venv/bin/python schedular.py >> /Users/denizerenozer/python-postgres-etl/logs/pipeline.log 2>&1

# ./run_pipeline.sh
# tail -30 logs/pipeline.log