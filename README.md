# Words

Installation steps:

1-Download and install Python 3.6.4 from https://www.python.org/downloads/ (check "Add Python to environment variables" while in the setup)

2-Download and Install Visual Studio 2015 Build Tools from http://landinghub.visualstudio.com/visual-cpp-build-tools

3-Unzip the contents of rc.zip (its in the /setup folder of the repo) and copy rc.exe and rc.dll to the /bin folder of the Visual Studio Build Tools installation (typically C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin)

4-Open a windows command line as admin and execute the following sentences

	4.1-pip install -U spacy
  
	4.2-python -m spacy download en
	
App execution steps:

1-Open a windows command line

2-"cd" to the folder containing the words.py file

3-Execute python words.py
