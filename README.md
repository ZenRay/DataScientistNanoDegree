**Contents**

[TOC]



# $\rm II.$  Project 2

## Project Overview

In this course, you've learned and built on your data engineering skills to expand your opportunities and potential as a data scientist. In this project, you'll apply these skills to analyze disaster data from [Figure Eight](https://www.figure-eight.com/) to build a model for an API that classifies disaster messages.

In the Project Workspace, you'll find a data set containing real messages that were sent during disaster events. You will be creating a machine learning pipeline to categorize these events so that you can send the messages to an appropriate disaster relief agency.

Your project will include a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data. This project will show off your software skills, including your ability to create basic data pipelines and write clean, organized code!

Below are a few screenshots of the web app.





![img](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/September/5b967bef_disaster-response-project1/disaster-response-project1.png)





![img](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/September/5b967cda_disaster-response-project2/disaster-response-project2.png)





**Project Components**

There are three components you'll need to complete for this project.

**1. ETL Pipeline**

In a Python script, `process_data.py`, write a data cleaning pipeline that:

- Loads the `messages` and `categories` datasets
- Merges the two datasets
- Cleans the data
- Stores it in a SQLite database

**2. ML Pipeline**

In a Python script, `train_classifier.py`, write a machine learning pipeline that:

- Loads data from the SQLite database
- Splits the dataset into training and test sets
- Builds a text processing and machine learning pipeline
- Trains and tunes a model using GridSearchCV
- Outputs results on the test set
- Exports the final model as a pickle file

**3. Flask Web App**

We are providing much of the flask web app for you, but feel free to add extra features depending on your knowledge of flask, html, css and javascript. For this part, you'll need to:

- Modify file paths for database and model as needed
- Add data visualizations using Plotly in the web app. One example is provided for you

**Github & Code Quality**

Your project will also be graded based on the following:

- Use of Git and Github
- Strong documentation
- Clean and modular code

Follow the [RUBRIC](https://review.udacity.com/#!/rubrics/1565/view) when you work on your project to assure you meet all of the necessary criteria for developing the pipeline and web app.

## Project Details

Below are additional details about each component and tips to get you started.

**Data Pipelines: Jupyter Notebooks**

We've provided Jupyter notebooks in Project Workspaces with instructions to get you started with both data pipelines. The Jupyter notebook is not required for submission, but highly recommended to complete before getting started on the Python script.

**Project Workspace - ETL**

The first part of your data pipeline is the Extract, Transform, and Load process. Here, you will read the dataset, clean the data, and then store it in a SQLite database. We expect you to do the data cleaning with pandas. To load the data into an SQLite database, you can use the pandas dataframe `.to_sql()` method, which you can use with an SQLAlchemy engine.

Feel free to do some exploratory data analysis in order to figure out how you want to clean the data set. Though you do not need to submit this exploratory data analysis as part of your project, you'll need to include your cleaning code in the final ETL script, `process_data.py`.

**Project Workspace - Machine Learning Pipeline**

For the machine learning portion, you will split the data into a training set and a test set. Then, you will create a machine learning pipeline that uses NLTK, as well as scikit-learn's Pipeline and GridSearchCV to output a final model. Finally, you will export your model to a pickle file. After completing the notebook, you'll need to include your final machine learning code in `train_classifier.py`.

**Data Pipelines: Python Scripts**

After you complete the notebooks for the ETL and machine learning pipeline, you'll need to transfer your work into Python scripts, `process_data.py` and `train_classifier.py`. If someone in the future comes with a revised or new dataset of messages, they should be able to easily create a new model just by running your code. These Python scripts should be able to run with additional arguments specifying the files used for the data and model.

**Example:**

```txt
python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db

python train_classifier.py ../data/DisasterResponse.db classifier.pkl
```

Templates for these scripts are provided in the Resources section, as well as the **Project Workspace IDE**. The code for handling these arguments on the command line is given to you in the templates.

**Flask App**

In the last step, you'll display your results in a Flask web app. We have provided a workspace for you with starter files. You will need to upload your database file and pkl file with your model.

This is the part of the project that allows for the most creativity. So if you are comfortable with html, css, and javascript, feel free to make the web app as elaborate as you would like.

In the starter files, you will see that the web app already works and displays a visualization. You'll just have to modify the file paths to your database and pickled model file as needed.

There is one other change that you are required to make. We've provided code for a simple data visualization. Your job will be to create two additional data visualizations in your web app based on data you extract from the SQLite database. You can modify and copy the code we provided in the starter files to make the visualizations.

**Github & Code Quality**

Throughout the process, make sure to push your code and comments to Github so that you will not repeat your work and you can keep track of the changes you've made. This will also help you keep your code modular and well documented. Make sure to include effective comments and docstrings. These software engineering practices will improve your communication and collaboration in the future when you work within a team.

**Starter Code**

The coding for this project can be completed using the Project Workspace IDE provided. Here's the file structure of the project:

```txt
- app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py
|- InsertDatabaseName.db   # database to save clean data to

- models
|- train_classifier.py
|- classifier.pkl  # saved model 

- README.md
```

**Running the Web App from the Project Workspace IDE**

When working in the Project Workspace IDE, here is how to see your Flask app.

Open a new terminal window. You should already be in the workspace folder, but if not, then use terminal commands to navigate inside the folder with the run.py file.

Type in the command line:

```python
python run.py
```

Your web app should now be running if there were no errors.

Now, open another Terminal Window.

Type

```python
env|grep WORK
```

You'll see output that looks something like this:

![img](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/February/5a8e41a1_screen-shot-2018-02-21-at-8.05.18-pm/screen-shot-2018-02-21-at-8.05.18-pm.png)

In a new web browser window, type in the following:

```
https://SPACEID-3001.SPACEDOMAIN
```

In this example, that would be: "[https://viewa7a4999b-3001.udacity-student-workspaces.com/"](https://viewa7a4999b-3001.udacity-student-workspaces.com/%22) (Don't follow this link now, this is just an example.)

Your SPACEID might be different.

You should be able to see the web app. The number 3001 represents the port where your web app will show up. Make sure that the 3001 is part of the web address you 