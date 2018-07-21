## Q: I modified my database. Can I undo it?

If you'd like to revert the 

news database to its original form, you can do that by dropping each of the tables, then re-importing the data from the 

newsdata.sql file.

In 

psql:

drop table log;
drop table articles;
drop table authors;

Then in the shell, re-import the data:

psql -d news -f newsdata.sql

## Q: These queries are complicated. Where do I start?

One of the best ways to build complex queries is by starting with smaller pieces, and testing each of them in small steps. Here's a worked example —

Suppose we wanted to print out each article's _title and author name._

Looking at the schema for 

articles (with 

\d articles) we can see there's an author and title column. But the author column doesn't have names in it — just numbers. To see this in your database, run:

select author from articles;

But the 

authors table has a 

name column, and a numeric 

id column. To see this, run:

select * from authors;

Those numeric id values match up with the 

articles.author column. And that means we can connect the two tables with a join:

select title, name
from articles join authors
on articles.author = authors.id;

or:

select title, name
from articles, authors
where articles.author = authors.id;

Try these queries on your 

news database! Look for other relationships that can work with 

join.