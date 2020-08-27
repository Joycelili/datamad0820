--CHALLENGE 1

SELECT authors.au_id as `Author ID`, authors.au_lname `LAST NAME`, authors.au_fname `FIRST NAME`,titles.title `TITLE`, publishers.pub_name `PUBLISHERS`
FROM titles
LEFT JOIN titleauthor
ON titles.title_id = titleauthor.title_id
LEFT JOIN authors
ON authors.au_id = titleauthor.au_id
LEFT JOIN publishers
ON publishers.pub_id = titles.pub_id;

--CHALLENGE 2

SELECT authors.au_id as `Author ID`, authors.au_lname `LAST NAME`, authors.au_fname `FIRST NAME`, publishers.pub_name `PUBLISHERS`, count(titles.title) as `COUNT TITLES`
FROM titles
INNER JOIN titleauthor
ON titles.title_id = titleauthor.title_id
LEFT JOIN authors
ON authors.au_id = titleauthor.au_id
LEFT JOIN publishers
ON publishers.pub_id = titles.pub_id
GROUP BY authors.au_id , authors.au_lname , authors.au_fname , publishers.pub_name;

--CHALLENGE 3

SELECT authors.au_id as `Author ID`, authors.au_lname `LAST NAME`, authors.au_fname `FIRST NAME`, SUM(sales.qty) as `TOTAL`
FROM authors
LEFT JOIN titleauthor
ON  titleauthor.au_id = authors.au_id 
LEFT JOIN sales
ON sales.title_id = titleauthor.title_id
GROUP BY authors.au_id, authors.au_lname , authors.au_fname
ORDER BY `TOTAL` DESC LIMIT 3;

--CHALLENGE 4

SELECT authors.au_id as `Author ID`, authors.au_lname `LAST NAME`, authors.au_fname `FIRST NAME`, SUM(sales.qty) as `TOTAL`
FROM authors
LEFT JOIN titleauthor
ON  titleauthor.au_id = authors.au_id 
LEFT JOIN sales
ON sales.title_id = titleauthor.title_id
WHERE sales.qty IS NOT NULL
GROUP BY authors.au_id, authors.au_lname , authors.au_fname
ORDER BY `TOTAL` DESC LIMIT 23;


