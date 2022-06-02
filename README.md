# Brane Visualization package
[![DOI](https://zenodo.org/badge/498253114.svg)](https://zenodo.org/badge/latestdoi/498253114)
## Requirements
pandas==1.2.4

numpy==1.20.3

matplotlib==3.4.2

seaborn==0.11.1

pyecharts==1.9.1
## Installation
```
brane import 97Simei/braneVisualPackage
```
## Functions

| NAME | INPUT EXAMPLES | OUTPUT EXAMPLES |
| :----: | :----: | :----: |
|  plot   |  INPUT_PATH: '/data/train.csv'<br>FUNCTION_TYPE='missing_value'<br>OUTPUT_PATH: '/data/' | /data/missing_value.html |
| plot  |  INPUT_PATH: '/data/train.csv'<br>FUNCTION_TYPE='correlation'<br>OUTPUT_PATH: '/data/' | /data/correlation.png |
| plot  |  INPUT_PATH: '/data/train.csv'<br>FUNCTION_TYPE='distribution'<br>OUTPUT_PATH: '/data/' | /data/distributiin.png |
## Tests
Run unit tests with pytest: `pytest`
