# Instructions for extracting comments from video using API: 

1. Set up API key. It should be about 40 characters and have numbers and letters

2. cd to your youtube directory

3. Download the secret_key.py template file and put in your API key
* The file should only have one line and look like this:
	SECRET_KEY = 'Nifuviabdva34bFYKCrdbvaBg1FJabvqeiurb'

4. Download apiCall3.py

5. Download the requirements.txt file in a clean virtual environment using: 
$ pip install -r requirements.txt $

6. Run the code using:

$ python3 apiCall3.py --c --videourl=https://www.youtube.com/watch?v=TPb6eoOu33g $
* you can change out the link for a different video
* this should create a file called apiCall2_output.txt with a corpus of the comments. If it doesn't, try creating a blank file with that name by typing:
	
	$ touch apiCall2_output.txt $

## Troubleshooting

* if urllib isn't working, check the spacing and indenting around those commands & make sure all of your packages are updates. 

* if you get an error like "object has no attribute 'key'", check that your API key is correct and the file is properly named and called on. 

* if you get an error like "IndentationError: unexpected indent", sometime when downloading from github the indenting on the files gets messed up. In a text editor, try changing the tab size/ spacing and either convert to tabs or spaces completely

* If you get an error with "Invalid Arguments....", check to make sure you are entering the video URL into the command line correctly


# Next Steps:
* One of the files we have should format and parse the JSON properly and write it to a csv file (i'm not sure which one...)
* For building the model right now, we are using the cleanly formatted and labeled data from OK Go video stored in the labeledCom.csv file
* Currently using NLP_Youtube.ipynb file to practice fitting a MNB Classifier