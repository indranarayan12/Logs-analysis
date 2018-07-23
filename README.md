# Logs-analysis

### Brief analysis 
Uses SQL queries to analyze data by connecting to a newspaper articles database. This project works with data that could have come from real-world web application, with fields representing information that a web server would record, such as HTTP status codes URI paths. The web server and the reporting tool bith connect to the same database. allowing information to flow from the web server into the report.

### Download

#### Softwares required:
[Python3](https://www.python.org/)
[Vagrant](https://www.vagrantup.com/)
[VirtualBox](https://www.virtualbox.org/)

#### Environment setup:
1. Install Vagrant and VirtualBox
2. Download or clone [fsnd-virtual-machine](https://github.com/udacity/fullstack-nanodegree-vm) repository.
3. Download [newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here and unzip the it.
3.Move the newsdata.sql  and newsdata.py files to the vagrant directory.

#### Launching the virtual machine and running the project
1. '''cd''' inside the vagrant directory of FSND-Virtual-Machine directory run :
'''$ vagrant up'''
2. Log in using:
'''$vagrant ssh'''
3. '''cd''' inside vagrant directory
'''$cd vagrant'''
4.run:
'''psql -d news -f newsdata.sql'''
5.'''python3 newsdata.py''' to run the reporting tool
6.From the vagrant directory inside the virtual machine, run logs_analysis.py using:
'''$python3 logs_analysis.py'''

