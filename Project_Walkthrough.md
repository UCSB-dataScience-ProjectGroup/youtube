## Guided Walkthrough:

1. Set up a Google Account, Create a project in the Developers Consol, etc. to request an API key and authorization credentials  <br />
	[Google Account](https://accounts.google.com/SignUp?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount)  <br />
	[Google Developers Consol](https://console.developers.google.com/) <br />
	[More Detailed Guide](https://developers.google.com/youtube/v3/getting-started) <br />
	
	
2. Put your secret client code in a file  <br />
	[Secret File](https://github.com/UCSB-dataScience-ProjectGroup/youtube/.gitignore)
	
	
3. Install requirements  <br />
	[Requirements](https://github.com/UCSB-dataScience-ProjectGroup/youtube/requirements.txt) <br />
	
	
3. Run the CommentThread.py file to extract comments from the API  <br />
	[Comment Thread File](https://github.com/UCSB-dataScience-ProjectGroup/youtube/CommentThread.py) <br />
	- Your output will be in JSON format, which is embedded dictionaries  <br />
	
	
4. Download PostgreSQL (for the GUI, can also just use through terminal) and make a database  <br />
	[PostreSQL Application](https://www.postgresql.org) <br />
	[Basic Tutorial](http://postgresqltutorial.com) <br />
	
	
5. Insert comments into a SQL relational database for easier access <br />
	[Requirements](https://github.com/UCSB-dataScience-ProjectGroup/PostgresPipe.py) <br />
	
	
6. NLP!!! <br />
- We will probably use Pthyon's NLTK package to perform the proessing <br />
- Here are some sources to learn more about it & how to use it: <br />
[Source 1](https://pypi.python.org/pypi/nltk) <br />
[Source 2](https://pythonprogramming.net/tokenizing-words-sentences-nltk-tutorial/)<br />
[Source 3](http://www.nltk.org)<br />
