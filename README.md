# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import blackfox 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import blackfox
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import blackfox
from blackfox.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = blackfox.DataSetApi()
id = 'id_example' # str | Dataset Id

try:
    # Download dataset file (*.csv)
    api_instance.get(id)
except ApiException as e:
    print("Exception when calling DataSetApi->get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DataSetApi* | [**get**](docs/DataSetApi.md#get) | **GET** /api/DataSet/{id} | Download dataset file (*.csv)
*DataSetApi* | [**head**](docs/DataSetApi.md#head) | **HEAD** /api/DataSet/{id} | Check if csv file exist
*DataSetApi* | [**post**](docs/DataSetApi.md#post) | **POST** /api/DataSet | Upload csv file
*NetworkApi* | [**get**](docs/NetworkApi.md#get) | **GET** /api/Network/{id} | Download nework file (*.onnx)
*NetworkApi* | [**head**](docs/NetworkApi.md#head) | **HEAD** /api/Network/{id} | Check if onnx file exist
*NetworkApi* | [**post**](docs/NetworkApi.md#post) | **POST** /api/Network | Upload onnx file
*PredictionApi* | [**post_array**](docs/PredictionApi.md#post_array) | **POST** /api/Prediction/keras/array | 
*PredictionApi* | [**post_file**](docs/PredictionApi.md#post_file) | **POST** /api/Prediction/keras/file | 
*TrainingApi* | [**post**](docs/TrainingApi.md#post) | **POST** /api/Training/keras | 


## Documentation For Models

 - [HiddenLayerConfigKerasActivationFunction](docs/HiddenLayerConfigKerasActivationFunction.md)
 - [KerasTrainingConfig](docs/KerasTrainingConfig.md)
 - [LayerConfigKerasActivationFunction](docs/LayerConfigKerasActivationFunction.md)
 - [PredictionArrayConfig](docs/PredictionArrayConfig.md)
 - [PredictionFileConfig](docs/PredictionFileConfig.md)
 - [Range](docs/Range.md)
 - [TrainedNetwork](docs/TrainedNetwork.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author


