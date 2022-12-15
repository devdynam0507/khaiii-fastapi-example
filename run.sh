#/bin/bash

docker run -v $(pwd):/workspace/code \
           -t dynam0507/khaiii-fastapi \
           -p 80:8080 \
           main:app --host 0.0.0.0 --port 8080 --workers 2