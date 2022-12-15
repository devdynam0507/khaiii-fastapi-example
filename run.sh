#/bin/bash

docker run -v $(pwd):/workspace/code \
           -p 80:8080 \
           -t dynam0507/khaiii-fastapi \
           main:app --host 0.0.0.0 --port 8080 --workers 2