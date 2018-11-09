**Table Of Contents**

1. [Installation](#installation)
2. [Project Overview](#project)

3. [File Descripton](#file)
4. [Results](#results)

5. [Licensing](#licensing)

## Installation<a id="installation"></a>

The project is supported by Python 3.x (Hint: directly install the Anaconda distribution), libraries and packages:

* Numpy
* Pandas
* IPython
* Matplotlib
* Pickle

## Project Overview<a id="project"></a>

We make the recommendations about the interactions that users have with articles on the IBM Watson Studio platform. We use the different method to build the recommendations system.

## File Description<a id="file"></a>

- [Recommendations_with_IBM.ipynb](Recommendations_with_IBM.ipynb)

  The notebook is used to build the recommendation system. We can run the file by using Jupyter Notebook

- [data](./data)

  Directory contains the original data files, like [articles_community.csv](data/articles_community.csv) and [user-item-interactions.csv](data/user-item-interactions.csv) 

The main file structure is like:

```
├── README.md
├── Recommendations_with_IBM.ipynb	# notebook to build the recommendation system
├── data	# original data
│   ├── articles_community.csv
│   └── user-item-interactions.csv
├── project_tests.py
├── top_10.p
├── top_20.p
├── top_5.p
└── user_item_matrix.p
```

## Results <a id="results"></a>

There are different recommendation systems, which can be built. Otherwise, we must to choose a proper method to build the system, which there are the factors taken into account, like user type, user habit and so on.

## Licensing<a id="licensing"></a>

Feel free to use the code, and let me know the project can be improved. If you  would like to do further more, it is available below under GNU license.