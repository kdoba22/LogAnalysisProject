# LogAnalysisProject
  Udacity FSND log analysis project

## Project overview
  You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

  The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

  The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

## You will need
  1.  Python 2.7
  2.  Vagrant 1.9.5
  3.  VirtualBox

## Setup
  1.  Install setup Vagrant and VirtualBox
  2.  [load the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## To Run project
  Launch Vagrant by running 'vagrant up'.  Once running you can log on with 'vagrant ssh'.

  To get to the data, use the command 'psql -d news -f newsdata.sql'.

  The DB includes 3 tables:
    * Articles
    * Authors
    * Log

To execute the program, run 'python newsdata.py' from the command line
