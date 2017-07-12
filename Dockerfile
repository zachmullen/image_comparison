FROM python:3.4.6
RUN pip install nibabel scikit-image
COPY compare_images.py /compare_images.py 
ENTRYPOINT ["python", "/compare_images.py"]
