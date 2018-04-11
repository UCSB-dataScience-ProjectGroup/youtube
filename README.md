# YouTube Data Prediction
## Abstract:
Using natural language processing (nlp) and machine learning (ml) algorithms to classify YouTube comments as positive, negative or neutral

## Goals: 
* Understand how word usage can be indicative of overall user sentiment towards or approval of videos on social media platforms
* Learn about NLP and how computers can be used to comprehend, analyze, and classify human language and emotions through text

## Workflow:
1. Obtain API key from [Google Developers Console](https://console.developers.google.com/)
2. Extract comments for a video by pulling from the Youtube API using [apiCall3](https://github.com/UCSB-dataScience-ProjectGroup/youtube/blob/Andies-Branch/apiCall3.py)
3. Output comments into an Excel file by typing `Python 3 <tags for video paramters...> apiCall3.py >> example_output_file.xls` into your terminal when running the code
4. Change the path and file name in the [Youtube_Analysis.ipynb](https://github.com/UCSB-dataScience-ProjectGroup/youtube/blob/Andies-Branch/Youtube_Analysis.ipynb) file to your personal path and file name:
`os.chdir('~/<path_to_your_directory_here>/')` <br>
`df = pd.read_csv('<your_file_here>.csv', delimiter=";", skiprows=2, encoding='latin-1', engine='python')`
5. Run Youtube_Analysis jupyter notebook file for model predictions on the video selected (in progress)
6. Dashboard (to come!)

### Current Progress: [Jupyer Notebook](https://github.com/UCSB-dataScience-ProjectGroup/youtube/blob/Andies-Branch/Youtube_Analysis.ipynb)

### Next Steps:
* cross validation
* grid search
* neural networks
* dashboard

## Links:
1. [Requirements](https://github.com/UCSB-dataScience-ProjectGroup/youtube/requirements.txt)
2. [API](https://developers.google.com/youtube/v3/)

## Dashboard (In Progress): 
![dashboard screenshot](https://github.com/UCSB-dataScience-ProjectGroup/youtube/blob/Andies-Branch/images/Dashboard_Screenshot.png)

### Table of Contents: 
1. Youtube API Call: [apiCall3.py](https://github.com/UCSB-dataScience-ProjectGroup/youtube/blob/Andies-Branch/apiCall3.py)
2. Machine Learning Notebook: [Youtube_Analysis.ipynb](https://github.com/UCSB-dataScience-ProjectGroup/youtube/blob/Andies-Branch/Youtube_Analysis.ipynb)
3. Dashboard Script: [PP.py](https://github.com/UCSB-dataScience-ProjectGroup/youtube/blob/Andies-Branch/PP.py)
