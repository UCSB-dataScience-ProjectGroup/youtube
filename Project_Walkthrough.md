Steps for Utilizing Project:

1. Set up a Google Account, Create a project in the Developers Consol, etc. to request an API key/ authorization credentials, 
	[Google Account](https://accounts.google.com/SignUp?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount)
	[Google Developers Consol](https://console.developers.google.com/)
	[More Detailed Guide](https://developers.google.com/youtube/v3/getting-started)
2. Put your secret client code in a file
	[Secret File](https://github.com/UCSB-dataScience-ProjectGroup/youtube/.gitignore)
3. Install requirements
	[Requirements](https://github.com/UCSB-dataScience-ProjectGroup/youtube/requirements.txt)
3. Run the CommentThread.py file to extract comments from the API 
	[Comment Thread File](https://github.com/UCSB-dataScience-ProjectGroup/youtube/CommentThread.py)
	-Your output will be in JSON format, which is embedded dictionaries
4. Download PostgreSQL (for the GUI, can also just use through terminal) and make a database
	[PostreSQL Application](https://www.postgresql.org)
	[Basic Tutorial](http://postgresqltutorial.com)
5. Insert comments into a SQL relational database for easier access
	[Requirements](https://github.com/UCSB-dataScience-ProjectGroup/PostgresPipe.py)
6. NLP!!!
