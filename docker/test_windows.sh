#!/bin/bash
# this should be called in same directory as docker image (or dockerfile?), only need docker and completely automate the setup process (for usage via jupyter)

# TODO maybe check whether image is already known, otherwise see if there is a dockerfile in working dir and build

# stop other shapex containers
# https://stackoverflow.com/questions/32073971/stopping-docker-containers-by-image-name-ubuntu FROM HERE
docker rm $(docker stop $(docker ps -a -q --filter ancestor=shapex:latest --format="{{.ID}}")) 

# run docker image
#docker run -p 8888:8888 -d -t shapex:latest /bin/bash -c "/opt/conda/bin/jupyter notebook /home/shapex/demo.ipynb --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='0291029398729374728jdaojalklyo'" >/dev/null
docker run -p 8888:8888 -d -t shapex:latest /bin/bash -c "/opt/conda/bin/jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='0291029398729374728jdaojalklyo'"

echo "Started docker container and jupyter server"

timeout --kill-after=1 1 ls /mnt/ftp/ # give container some time to start jupyter

# open jupyter in browser (possibly inside python session)
# http://127.0.0.1:8888?token=0291029398729374728jdaojalklyo OPENS JUPYTER NOTEBOOK
# https://stackoverflow.com/questions/3124556/clean-way-to-launch-the-web-browser-from-shell-script FROM HERE
URL="http://127.0.0.1:8888/notebooks/demo.ipynb?token=0291029398729374728jdaojalklyo"

start "$URL"
# start "" "http://127.0.0.1:8888/notebooks/demo.ipynb?token=0291029398729374728jdaojalklyo"