FROM debian:latest

#  $ docker build . -t continuumio/miniconda3:latest -t continuumio/miniconda3:4.5.11
#  $ docker run --rm -it continuumio/miniconda3:latest /bin/bash
#  $ docker push continuumio/miniconda3:latest
#  $ docker push continuumio/miniconda3:4.5.11

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.11-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

ENV TINI_VERSION v0.16.1
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

# install most packages via conda
RUN /opt/conda/bin/conda install numpy pandas rpy2 networkx tqdm pip matplotlib r-base jupyter -y --quiet && \
    /opt/conda/bin/conda install -c conda-forge antlr-python-runtime -y && \
# use pip for z3
    pip install z3-solver && \
# clean up caches to reduce image size
    conda clean --all -y
	
# set up R environment via R (this takes forever to build...)
RUN Rscript -e "install.packages(c('Rcpp','RcppEigen','BH','digest','rlang','volesti', 'codetools'), repos='https://cloud.r-project.org/' , dependencies=TRUE)" && \
# clean up caches to reduce image size (Not sure if this does something for packages installed via R)
    conda clean --all -y
	
# set up jupyter notebook files
RUN mkdir /opt/notebooks && \
# make shapex the root directory of the jupyter notebook
    jupyter notebook --generate-config &&\  
    echo "c.NotebookApp.notebook_dir = '/home/shapex/'" > /root/.jupyter/jupyter_notebook_config.py

# TODO this is problematic because it is hardcoded... need shapes_generator in current directory. Automatically pull from repository?
COPY shapes_generator /home/shapex

ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]


