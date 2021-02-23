FROM python:3
ADD FinalOptimised_Paranthesis_Code.py /
RUN apt-get install python
COPY FinalOptimised_Paranthesis_Code.py ./

RUN  pip3 install --upgrade pip && \
     pip3 install memory_profiler 
 
CMD ["python","./FinalOptimised_Paranthesis_Code.py"]

