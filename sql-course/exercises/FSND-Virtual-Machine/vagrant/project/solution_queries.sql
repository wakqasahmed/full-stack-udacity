## Query # 1

### Brainstorming
select a.slug, a.title, count(l.*) as views
from articles a, log l where l.path
like '%' || a.slug group by a.slug, a.title
order by views desc limit 3;

### Final
CREATE OR REPLACE VIEW most_popular_articles AS (
	SELECT a.title, COUNT(l.*) AS views
	FROM articles a, log l
	WHERE l.path LIKE '%' || a.slug
	GROUP BY a.title
	ORDER BY views DESC LIMIT 3
);

## Query # 2

### Brainstorming
select ar.title, au.name, count(l.path) as views
from articles ar
join authors au on au.id = ar.author
left join log l on l.path like '%' || ar.slug
group by ar.title, au.name;

### Final
CREATE OR REPLACE VIEW most_popular_article_authors AS (
	SELECT most_views.author_name, SUM(most_views.article_views) AS views FROM
	(SELECT au.name AS author_name, COUNT(l.path) AS article_views
	FROM articles ar
	JOIN authors au ON au.id = ar.author
	LEFT JOIN log l ON l.path LIKE '%' || ar.slug
	GROUP BY au.name) AS most_views
	GROUP BY most_views.author_name
	ORDER BY views DESC
);


## Query # 3

### Brainstorming
select status, time::date, count(*) as no_of_errors
from log
where status != '200 OK'
group by time::date, status
order by time::date desc limit 50;

#### all requests day wise
select time::date as day, count(status) as no_of_requests
from log
group by day
order by day desc;

#### erroneous requests day wise
select time::date as day, count(status) as no_of_errors
from log
where status != '200 OK'
group by day
order by day desc;

### Final
#### combining the above two queries and creating a view
CREATE OR REPLACE VIEW erroneous_requests_per_day_more_than_a_percent AS (
	SELECT critical_error_log.day, ROUND(critical_error_log.request_to_error_ratio,1) as request_to_error_ratio
	FROM
	(
		SELECT error_log.day,
		SUM(error_log.no_of_errors)/SUM(error_log.no_of_requests)*100 AS request_to_error_ratio,
		SUM(error_log.no_of_requests) AS total_requests,
		SUM(error_log.no_of_errors) AS total_errors
		FROM
		(
			SELECT time::date AS day, COUNT(status) AS no_of_requests, '0' AS no_of_errors 
			FROM log
			GROUP BY day

			UNION

			SELECT time::date AS day, '0' AS no_of_requests, COUNT(status) AS no_of_errors
			FROM log
			WHERE status != '200 OK'
			GROUP BY day
			) AS error_log
		GROUP BY error_log.day
	)
	AS critical_error_log
	WHERE critical_error_log.request_to_error_ratio > 1
);