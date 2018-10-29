**Table Of Contents**

1. [Installation](#installation)
2. [Project Overview](#project)

3. [File Descripton](#file)
4. [Results](#results)

5. [Acknowledge](#ackowledge)
6. [Licensing](#licensing)

## Installation<a id="installation"></a>

The project is supported by Python 3.x (Hint: directly install the Anaconda distribution), libraries and packages:

* Numpy 1.15.2
* Pandas 0.23.4
* IPython 6.5.0
* Matplotlib 3.0.0
* scikit-learn 0.20.0
* sqlalchemy 1.2.12
* nltk 3.3.0

**Note:** There is different in different scikit-learn version, when using `classification_report` method.

## Project Overview<a id="project"></a>

We apply data enginering method  to analyze disaster data, besides we build a model for API, in order to classify disaster messages.

In the project, we finish the ETL pipeline. And, we store the data into the database. At the second step, we use the cleaning data to build a model, so that we can classify the messages, which is a Machine Learning pipeline.

Our target is that we deploy the model at the web application. We can classify the messages that are queried from the web.

## File Description<a id="file"></a>

- [workspace](./workspace)

  Directory contains [ETL pipeline](./workspace/data), [ML pipeline](./workspace/models), and [Web application](./workspace/app).

  -  [ETL pipeline](./workspace/data)

    A Python script [process_data.py](./workspace/data/process_data.py) can load and merge the [disaster_messages.csv](workspace/data/disaster_messages.csv) and [disaster_categories.csv](workspace/data/disaster_categories.csv) datasets, then stores the data in a SQLite database [DisasterResponse.db](workspace/data/DisasterResponse.db), after cleaning. 

    ```bash
    # change workspace as the current directory
    cd workspace
    
    # run below code to finish the ETL pipeline
    python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
    ```

  - [ML pipeline](./workspace/models)

    A Python script [train_classifier.py](workspace/models/train_classifier.py) can load data from SQLite database. And it stores the final model [classifier.pkl](workspace/models/), after training model.

    ```bash
    # change workspace as the current directory
    cd workspace
    
    # run below code to finish the ML pipeline, which can build model
    python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
    ```

  - [Web application](./workspace/app)

    A Python scrip [run.py](./workspace/app/run.py)  and [HTML templates](./workspace/app/templates) provide the flask web app. We can check the dataset visualization and query the messages classification result.

    ```bash
    # change add as the current directory
    cd app
    
    # run below code to run web app
    python run.py
    
    # link the underline into a web browser
    http://0.0.0.0:3001/
    ```

- [ML Pipeline Preparation.ipynb](./ML Pipeline Preparation.ipynb)

  This is Jupyter notebook about ETL pipeline. It is the Extract, Transform, and Load process that the process is reading the dataset, cleaning the data, and then storing it in a SQLite database. 

- [ETL Pipeline Preparation.ipynb](ETL Pipeline Preparation.ipynb)

  This is Jupyter notebook about machine learning pipeline. The process is splitting the data into a training set and a test set, creating a machine learning pipeline that uses NLTK, as well as scikit-learn's Pipeline and GridSearchCV to output a final model. Finally export the model into a pickle file.

The main file structure is like:

```
├── ETL Pipeline Preparation.ipynb # Project Workspace - ETL
├── ML Pipeline Preparation.ipynb # Project Workspace - Machine Learning Pipeline
├── README.md	# README file
├── data	# Project workspace original data directory
│   ├── DisasterResponse.db		# Project Workspace - ETL result
│   ├── categories.csv		# Project workspace original data
│   └── messages.csv		# Project workspace original data
├── model.pickle		# Project Workspace - Machine Learning Pipeline result
└── workspace		# full pipeline contain ETL pipeline script and ml pipeline script
    ├── README.md
    ├── app			# web app
    │   ├── run.py
    │   └── templates
    │       ├── go.html
    │       └── master.html
    ├── data		# ETL pipeline
    │   ├── DisasterResponse.db		# ETL pipeline result
    │   ├── disaster_categories.csv
    │   ├── disaster_messages.csv
    │   └── process_data.py
    └── models		# ml pipeline
        ├── classifier.pkl		# ML pipeline result
        └── train_classifier.py
```

## Results <a id="results"></a>

The result is a data visualization and messages classification. We need run the web application by using `python run.py` in the app directory, and link the url `http://0.0.0.0:3001/` in the web browser.

## Acknowledge <a id="acknowlege"></a>

Must give credit to [Figure Eight](https://www.figure-eight.com/) and Udacity to the data and web application templates. The project focus on full pipelines about the ETL and the machine learning.

## Licensing<a id="licensing"></a>

Feel free to use the code, and let me know the project can be improved. If you  would like to do further more, it is available below under GNU license.