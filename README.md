**Contents**

[TOC]

# $\rm I.$ Project 1

## Project Overview

**1. Introduction**

For this project, you will be creating a blog post and Github repository to begin building a data science portfolio of your own. You can gain some inspiration from Robert's posts [here](https://medium.com/@rchang).

- Come up with three questions you are interested in answering.
- Extract the necessary data to answer these questions.
- Perform necessary cleaning, analysis, and modeling.
- Evaluate your results.
- Share your insights with stakeholders.

**2. Where to Start**

There are two components that are required for project completion.

- A **Github repository** for your code.
- A **blog post** of your findings.

Your **Github repository** must have the following characteristics:

- A README.md.
- Your code either in a notebook or script, with appropriate comments and documentation.

You may also provide any other necessary documentation you find necessary. Your **blog must** provide the following:

- A clear and engaging title and image.
- Your questions of interest.
- Your findings for those questions with a supporting statistic(s), table, or visual.

The purpose of this project is for you to show off your technical skills, but more importantly for you to begin putting together a portfolio that shows your ability to effectively communicate technical results. Your technical skills will be built up as the program progresses, but for this project the main focus should be on communicating effectively the results of your analysis.

In this project follow the [RUBRIC](https://review.udacity.com/#!/rubrics/1507/view) to assure you meet all of the necessary criteria for communicating your findings both as a developer and as a business professional.

## Project Details

**1. Data Details**

For this project, you will pick a dataset. Inspired by Robert, there are a few public datasets from AirBnB available below, but you may also choose a dataset similar to what was used in the lessons, or an entirely different dataset. Using your dataset, you will choose 3 questions you aspire to answer from the data.

[**Stack Overflow Data - 2017 Survey**](https://www.kaggle.com/stackoverflow/so-survey-2017)

You might have different questions about the 2017 StackOverflow survey data than I looked at earlier in the course. If you choose this dataset, you can not use the same questions that were analyzed earlier in the classroom.

Alternatively, if you felt pretty confident with the techniques in this lesson, you might be looking to push the envelope. In this case, you may choose to retrieve all of the [Stack Overflow Survey - Multiple Years](https://insights.stackoverflow.com/survey) results. From this data, you could analyze trends over time. What languages were most popular in each year? What other changes can you observe over time?

[**Seattle AirBNB Data**](https://www.kaggle.com/airbnb/seattle/data)

The Seattle AirBnB homes data can be used at the above link. You might pair this with the Boston AirBnB data, which can be found at the link below.

[**Boston AirBNB Data**](https://www.kaggle.com/airbnb/boston)

If you are looking to really challenge yourself, data from Seattle and Boston AirBNB homes can be used to understand how much AirBNB homes are earning in certain time frames and areas. You can compare rates between the two cities, or try to understand if there is anything about the properties that helps you predict price. Can you find negative and positive reviews based on text? This dataset requires a number of skills beyond those shown thus far in the course, but if you would like a challenge, this will certainly test your ability to work with messy, real world data.

You can find additional AirBnB data at the link [here](http://insideairbnb.com/get-the-data.html).

**2. Choose A Dataset of Your Own**

You are welcome to use Kaggle or another platform (or your own data) to create a blog and Github post instead of using the datasets discussed above.

**Key Steps for Project**

Feel free to be creative with your solutions, but do follow the CRISP-DM process in finding your solutions.

1) Pick a dataset.

2) Pose at least three questions related to business or real-world applications of how the data could be used.

3) Create a Jupyter Notebook or Python script, and any associated packages you'd like, to:

- Prepare data:
  - Gather necessary data to answer your questions
  - Handle categorical and missing data
  - Provide insight into the methods you chose and why you chose them
- Analyze, Model, and Visualize
  - Provide a clear connection between your business questions and how the data answers them.

4) Communicate your business insights:

- Create a Github repository to share your code and data wrangling/modeling techniques, with a technical audience in mind
- Create a blog post to share your questions and insights with a non-technical audience

Your **deliverables** will be a **Github repo** and a **blog post**. Use the rubric [here](https://review.udacity.com/#!/rubrics/1507/view) to assist in successfully completing this project!



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

# $\rm III.$ Project 3

## Project Details

**1. Recommendations with IBM**

**Introduction**

For this project you will be looking at the interactions that users have with articles on the IBM Watson Studio platform. Below you can see an example of what the dashboard could look like displaying articles on the IBM Platform.

![img](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/September/5ba02d6d_screen-shot-2018-09-17-at-3.40.30-pm/screen-shot-2018-09-17-at-3.40.30-pm.png)

Though the above dashboard is just showing the newest articles, you could imagine having a recommendation board available here that shows the articles that are most pertinent to a specific user.

In order to determine which articles to show to each user, you will be performing a study of the data available on the IBM Watson Studio platform. You can create your own account to become a part of their community, and get a better understanding of their data [by creating an account on the platform here](https://dataplatform.cloud.ibm.com/).

**2. Your Tasks**

Your project will be divided into the following tasks

I. **Exploratory Data Analysis**

Before making recommendations of any kind, you will need to explore the data you are working with for the project. Dive in to see what you can find. There are some basic, required questions to be answered about the data you are working with throughout the rest of the notebook. Use this space to explore, before you dive into the details of your recommendation system in the later sections.

II. **Rank Based Recommendations**

To get started in building recommendations, you will first find the most popular articles simply based on the most interactions. Since there are no ratings for any of the articles, it is easy to assume the articles with the most interactions are the most popular. These are then the articles we might recommend to new users (or anyone depending on what we know about them).

III. **User-User Based Collaborative Filtering**

In order to build better recommendations for the users of IBM's platform, we could look at users that are similar in terms of the items they have interacted with. These items could then be recommended to the similar users. This would be a step in the right direction towards more personal recommendations for the users. You will implement this next.

IV. **Content Based Recommendations (EXTRA - NOT REQUIRED)**

Given the amount of content available for each article, there are a number of different ways in which someone might choose to implement a content based recommendations system. Using your NLP skills, you might come up with some extremely creative ways to develop a content based recommendation system. You are encouraged to complete a content based recommendation system, but not required to do so to complete this project.

V. **Matrix Factorization**

Finally, you will complete a machine learning approach to building recommendations. Using the user-item interactions, you will build out a matrix decomposition. Using your decomposition, you will get an idea of how well you can predict new articles an individual might interact with (spoiler alert - it isn't great). You will finally discuss which methods you might use moving forward, and how you might test how well your recommendations are working for engaging users.

VI. **Extras & Concluding (EXTRA - NOT REQUIRED)**

As other (non-required) work to show off your skills, you can configure your code into a class and deploy your code to a flask app (like in the lessons). Adam will walk you through how he did this on IBM. Alternatively, you could deploy using Heroku. Again, these steps are not required to complete the project, but can help you push your skills and show off your work to the world.

Before you submit your work, check the [RUBRIC](https://review.udacity.com/#!/rubrics/2322/view) to make sure you meet all of the rubric items.

# $\rm IV.$ CapstoneProject

## 4. 1 Build Your Data Science Project

In this capstone project, you will leverage what you’ve learned throughout the program to build a data science project of your choosing. Your project deliverables are:

1. A Github repository of your work.
2. A blog post written for a technical audience, or a deployed web application powered by data.

In this capstone project, you will leverage what you’ve learned throughout the Nanodegree program to solve a problem of your choice.

1. You will first **define** the problem you want to solve and investigate potential solutions.
2. Next, you will **analyze** the problem through visualizations and data exploration to have a better understanding of what algorithms and features are appropriate for solving it.
3. You will then **implement** your algorithms and metrics of choice, documenting the preprocessing, refinement, and post-processing steps along the way.
4. Afterwards, you will collect **results** about your findings, visualize significant quantities, validate/justify your results, and make any concluding remarks about whether your implementation adequately solves the problem.
5. Finally, you will **construct** a blog post to document all of the steps from start to finish of your project, or deploy your results into a web application.

## 4.2 Setting Yourself Apart

An important part of landing a job or advancing your career as a data scientist is setting yourself apart through impressive data science projects. By now, you've completed several guided projects, and now's your chance to show off your skills and creativity. You'll receive a review and feedback from a Udacity mentor, and they will focus on how your project demonstrates your skills as a well-rounded data scientist.

This project is designed to prepare you for delivering a polished, end-to-end solution report of a real-world problem in a field of interest. When developing new technology, or deriving adaptations of previous technology, properly documenting your process is critical for both validating and replicating your results.

Things you will learn by completing this project:

- How to research and investigate a real-world problem of interest.
- How to accurately apply specific data science algorithms and techniques.
- How to properly analyze and visualize your data and results for validity.
- How to document and write a report of your work.

## 4.3 Software Requirements

**Your project must be written in Python 3.x**. Given the free-form nature of the data scientist capstone, the software and libraries you will need to successfully complete your work will vary depending on the chosen application area and problem definition. Because of this, it is imperative that all necessary software and libraries used in your capstone project are accessible to the reviewer and clearly documented. Information regarding the software and libraries your project makes use of should be included in the `README` along with your submission. Please note that proprietary software, software that requires private licenses, or software behind a paywall or login account should be avoided.

## 4.5 Data Requirements

Every data scientist capstone project will most certainly require some form of dataset or input data structure (input text files, images, etc.). Similar to the software requirements above, the data you use must either be publicly accessible or provided by you during the submission process, and private or proprietary data should not be used without expressed permission. Please take into consideration the file size of your data — while there is no strict upper limit, input files that are excessively large may require reviewers longer than an acceptable amount of time to acquire all of your project files and/or execute the provided development code. This can take away from the reviewer's time that could be put towards evaluating your submission. If the data you are working with fits the criteria of being too large, consider whether you can work with a subset of the data instead, or provide a representative sample of the data which the reviewer may use to verify the solution explored in the project.

## 4.6 Ethics

Udacity's A/B Testing course has a segment that discusses [the sensitivity of data](https://classroom.udacity.com/courses/ud257/lessons/3998098714/concepts/39997087540923#)(free course link) and the expectation of privacy from those whose information has been collected. While most data you find available to the public will not have any ethical complications, it is extremely important that you are considering where the data you are using came from, and whether that data contains any sensitive information. For example, if you worked for a bank and wanted to use customers' bank statements as part of your project, this would most likely be an unethical choice of data and should be avoided.

## 4.7 Selecting a Project

Think about a technical field or domain that you are passionate about, such as robotics, virtual reality, finance, natural language processing, or even artificial intelligence (the possibilities are endless!). Then, choose an existing problem within that domain that you are interested in which you could solve by applying data science techniques. Be sure that you have collected all of the resources needed (such as data sets) to complete this project, and make the appropriate citations wherever necessary in Github (and your blog if that is the path you decide to pursue). Below are a few suggested problem areas you could explore if you are unsure what your passion is:

- [Robot Motion Planning](https://docs.google.com/document/d/1ZFCH6jS3A5At7_v5IUM5OpAXJYiutFuSIjTzV_E-vdE/pub)
- [Healthcare](https://docs.google.com/document/d/1WzurKKa9AX2DnOH7KiB38mvozdOSemfkGpex8hdTy8c/pub)
- [Computer Vision](https://docs.google.com/document/d/1y-XfjkPFgUQxFIQ9bBncUSjs4HOf5E-45FrLYNBsZb4/pub)
- [Education](https://docs.google.com/document/d/1vjerjRQnWs1kLbZagDYT6rNqiwAG23Yj45oUY88IAxI/pub)
- [Investment and Trading](https://docs.google.com/document/d/1ycGeb1QYKATG6jvz74SAMqxrlek9Ed4RYrzWNhWS-0Q/pub)

In addition, you may find a technical domain (along with the problem and dataset) as *competitions* on platforms such as [Kaggle](http://kaggle.com/), or [Devpost](http://devpost.com/). This can be helpful for discovering a particular problem you may be interested in solving as an alternative to the suggested problem areas above. In many cases, some of the requirements for the capstone project are already defined for you when choosing from these platforms.

## 4.8 [Bertelsmann/Arvato Project](./P4_CapstoneProject)

### 4.8.1 Steps to Complete This Project

The project has three major steps: the customer segmentation report, the supervised learning model, and the Kaggle Competition.

**1. Customer Segmentation Report**

This section will be familiar to the corresponding project in Term 1 of the program, but the datasets now include more features that you can potentially use. You'll begin the project by using unsupervised learning methods to analyze attributes of established customers and the general population in order to create customer segments.

**2. Supervised Learning Model**

You'll have access to a third dataset with attributes from targets of a mail order campaign. You'll use the previous analysis to build a machine learning model that predicts whether or not each individual will respond to the campaign.

**3. Kaggle Competition**

Once you've chosen a model, you'll use it to make predictions on the campaign data as part of a Kaggle Competition. You'll rank the individuals by how likely they will be to convert to becoming a customer and see how your modeling skills measure up against your fellow students.

### 4.8.2 Terms & Conditions

In addition to Udacity's Terms of Use and other policies, your downloading and use of the **AZ Direct GmbH** data solely for use in the **Unsupervised Learning** and **Bertelsmann Capstone** projects are governed by the following additional terms and conditions. The big takeaways:

1. You agree to **AZ Direct GmbH's** General Terms provided below and that you only have the right to download and use the **AZ Direct GmbH** data solely to complete the data mining task which is part of the **Unsupervised Learning** and **Bertelsmann Capstone** projects for the Udacity Data Science Nanodegree program.
2. You are prohibited from using the **AZ Direct GmbH** data in any other context.
3. You are also required and hereby represent and warrant that you will delete any and all data you downloaded within 2 weeks after your completion of the **Unsupervised Learning** and **Bertelsmann Capstone** projects and the program.
4. If you do not agree to these additional terms, you will not be allowed to access the data for this project.

The full terms are provided in the workspace below. You will then be asked in the next workspace to agree to these terms before gaining access to the project, which you may also choose to download if you would like to read in full the terms.

These same exact terms are provided in the next workspace, where you will be asked to accept the terms prior to gaining access to the data.