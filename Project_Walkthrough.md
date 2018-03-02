## Guided Walkthrough:

1. Set up a Google Account, Create a project in the Developers Consol, etc. to request an API key and authorization credentials  
	* [Google Account](https://accounts.google.com/SignUp?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount)
	* [Google Developers Consol](https://console.developers.google.com/)
	* [More Detailed Guide](https://developers.google.com/youtube/v3/getting-started) 
	
	
2. Put your secret client code in a file  
	* [Secret File](https://github.com/UCSB-dataScience-ProjectGroup/youtube/.gitignore)
	
	
3. Install requirements  
	* [Requirements](https://github.com/UCSB-dataScience-ProjectGroup/youtube/requirements.txt) 
	* activate your virtual environment: source venv/bin/activate
	* run: $ pip install -r requirements.txt $
	
3. Run  `ApiCall2.py >> comments.xlsx` to extract comments from specified video and write them into an excel file 
	* [ApiCall2.py](https://github.com/UCSB-dataScience-ProjectGroup/youtube/blob/master/apiCall2.py) <br />
	*  Your output from the api call will be in JSON format (embedded dictionaries) and then that is parsed into comma separated format suitable for an excel file.
	
	
4. Head over to Youtube_Classifers.ipynb, it's time to do some Natural Language Processing! 
* We used sci-kit learn's natural language processing packages for their flexibility and great documentation 
	* Here are some sources to learn more about it & how to use it: 
		* [Source 1](https://pypi.python.org/pypi/nltk) 
		* [Source 2](https://pythonprogramming.net/tokenizing-words-sentences-nltk-tutorial/)
		* [Source 3](http://www.nltk.org)

5. Dash Board + Visualizations!
	* We will be using plotly because of its similarities to ggplot (which we all know and love) as well as its aesthetic visualizations, dashboard capabilities, and clean integration
