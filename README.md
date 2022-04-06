# compounds-data

Deployed API: https://g2nabpqw52.execute-api.eu-west-2.amazonaws.com/v1/

The API is built with the Chalice Python framework. Documentation can be found [here](https://aws.github.io/chalice/main.html).
Chalice is a wrapper around the Flask Python web framework and deploys and configures the python application onto AWS Services:

- AWS Lambdas
  - Serverless functions, info here: https://aws.amazon.com/lambda/
   
- AWS API Gateway
  - An API service handling traffic management and routing requests to AWS Lambdas, info here: https://aws.amazon.com/api-gateway/

- AWS CloudWatch
  - Logs from all AWS services, info here: https://aws.amazon.com/cloudwatch/

## Development

### Quick reference

- Local development environment
    - `cd api`
    - `chalice local --stage local`
        - http://localhost:8000/
- Linting
  - `black -l 120 .`
  - `flake8 --max-line-length 120`
- Testing
  - `pytest --mypy api/tests/` 
- Upgrading
  - `pip install -U -r api/requirements.txt`
  - `pip check`: checks for conflicts
  - `pip freeze > api/requirements.txt`
- Deployment
  - `cd api && chalice deploy --stage v1`
  - https://g2nabpqw52.execute-api.eu-west-2.amazonaws.com/v1/

### Initial setup

1. Clone this repository

    ```sh
    git clone git@github.com:tom-clements/compounds-data.git
    ```

3. Change into the api directory

    ```sh
    cd compounds-data/api
    ```

4. Create python environment

    Python version has to be supported by AWS lambdas: https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html.  
    
    Latest supported version as of 2022-04-05: `Python 3.9`
    
    Please use a python environment manager of choice. Instructions here are shown using anaconda.  
    Installing anaconda from https://www.anaconda.com/products/individual will enable conda CLI.  
    ```sh
    conda create -n <venv_name> python=3.9
    conda activate <venv_name>
    conda install pip
    ```
    
4. Install python dependencies

    ```sh
    pip install pytest black flake8 pytest-mypy
    pip install -r requirements.txt
    ```

6. Start a local development environment

    ```sh
    chalice local --stage local
    ```

    The environment should be accessible from http://localhost:8000/ by default.


### Module overview

#### chalicelib/
This folder has a **protected name**, which is picked up by chalice and deployed onto AWS lambda.  
Inside here should contain all application code.

#### tests/
This folder contains all the tests for the application. Please run using:
```sh
pytest --mypy tests/
```

### .chalice/config.json
The configuration file for the chalice deployment.


## Deployment

### Configure AWS credentials

Follow this official guide https://aws.github.io/chalice/quickstart.html.  
Refer to the **Credentials** section.

Ensure the access and secret keys are setup for your local profile.

### Chalice deploy

Deploy using: 
```sh
chalice deploy --stage v1
```

### Endpoint

Endpoint is configured to: https://g2nabpqw52.execute-api.eu-west-2.amazonaws.com/v1/

## Data ETL

The data was loaded into an Amazon DynamoDB table.
Run the ETL process using:

```sh
cd etl
python run_pipeline --table-name "compounds"
```