FROM hitokizzy/geezram:slim-buster

RUN git clone -b main https://github.com/geezrampy/ram-Pyro /home/rams/
WORKDIR /home/rams

RUN wget https://raw.githubusercontent.com/GeezRamPy/Ram-Pyro/main/requirements.txt \
    && pip3 install --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt \
    && rm requirements.txt

CMD bash start
