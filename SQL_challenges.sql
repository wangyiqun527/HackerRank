-- Select cities that begins with or ends with vowels.
select distinct city from station where city regexp "^(a|e|i|o|u)" and city regexp "(a|e|i|o|u)$";

-- right(string, n) Extract n characters from a string (starting from right)
select name from students where marks > 75 order by right(name,3), ID ;

select round(sqrt(power((max(LAT_N)-min(LAT_N)),2)+power((max(LONG_W)-min(LONG_W)),2)),4) from station;

-- Median
SELECT round(AVG(dd.lat_n),4) 
FROM (
SELECT d.lat_n, @rownum:=@rownum+1 as `row_number`, @total_rows:=@rownum
  FROM station d, (SELECT @rownum:=0) r
  WHERE d.lat_n is NOT NULL
  ORDER BY d.lat_n
) as dd
WHERE dd.row_number IN ( FLOOR((@total_rows+1)/2), FLOOR((@total_rows+2)/2) );

--Or: 
SET @rowIndex := -1;
SELECT ROUND(AVG(t.LAT_N), 4) FROM
(SELECT @rowIndex := @rowIndex+1 AS rowIndex, s.LAT_N 
 FROM STATION AS s ORDER BY s.LAT_N) as t
WHERE t.rowIndex IN (FLOOR(@rowIndex / 2), CEIL(@rowIndex / 2));

-- symmetric pairs:
select x, y from functions f1 
    where exists(select * from functions f2 where f2.y=f1.x 
                 and f2.x=f1.y and f2.x>f1.x) and (x!=y) 
union 
select x, y from functions f1 where x=y and 
    ((select count(*) from functions where x=f1.x and y=f1.x)>1)    
order by x;

-- OCCUPATION
SET @r1=0, @r2=0, @r3 =0, @r4=0;
SELECT MIN(Doctor), MIN(Professor), MIN(Singer), MIN(Actor) FROM
(SELECT CASE Occupation WHEN 'Doctor' THEN @r1:=@r1+1
                       WHEN 'Professor' THEN @r2:=@r2+1
                       WHEN 'Singer' THEN @r3:=@r3+1
                       WHEN 'Actor' THEN @r4:=@r4+1 END
       AS RowLine,
  CASE WHEN Occupation = 'Doctor' THEN Name END AS Doctor,
  CASE WHEN Occupation = 'Professor' THEN Name END AS Professor,
  CASE WHEN Occupation = 'Singer' THEN Name END AS Singer,
  CASE WHEN Occupation = 'Actor' THEN Name END AS Actor
 FROM OCCUPATIONS ORDER BY Name) AS t
GROUP BY RowLine;


--The PADS:
select concat('There are a total of ', count(distinct name), ' ', lower(OCCUPATION),'s.')
from OCCUPATIONS  group by OCCUPATION order by 1, OCCUPATION ;

--BINARY TREE NODES:
select N, 
if(P is null, 'Root', if(N in (select P from BST), 'Inner','Leaf')) from BST order by N;

--DRAW THE TRIANGLE 1:
SET @number = 21;
SELECT REPEAT('* ', @number := @number-1) FROM information_schema.tables LIMIT 20;

-- Interviews: 
-- Samantha interviews many candidates from different colleges using coding challenges and contests. 
-- Write a query to print the contest_id, hacker_id, name, and the sums of total_submissions, 
--total_accepted_submissions, total_views, and total_unique_views for each contest sorted by contest_id. 
-- Exclude the contest from the result if all four sums are 0.
-- Note: A specific contest can be used to screen candidates at more than one college, 
-- but each college only holds  screening contest.
SELECT con.contest_id, con.hacker_id, con.name, 
SUM(sg.total_submissions) as s1, 
SUM(sg.total_accepted_submissions)  as s2, 
SUM(vg.total_views) as s3, 
SUM(vg.total_unique_views) as s4
FROM Contests AS con
JOIN Colleges AS col ON con.contest_id = col.contest_id
JOIN Challenges AS cha ON cha.college_id = col.college_id
LEFT JOIN
(SELECT ss.challenge_id, 
 SUM(ss.total_submissions) AS total_submissions, 
 SUM(ss.total_accepted_submissions) total_accepted_submissions 
FROM Submission_Stats AS ss GROUP BY ss.challenge_id) AS sg
ON cha.challenge_id = sg.challenge_id
LEFT JOIN
(SELECT vs.challenge_id, 
 SUM(vs.total_views) AS total_views, 
 SUM(vs.total_unique_views) AS total_unique_views
FROM View_Stats AS vs GROUP BY vs.challenge_id) AS vg
ON cha.challenge_id = vg.challenge_id
GROUP BY con.contest_id, con.hacker_id, con.name
HAVING s1+s2+s3+s4 > 0
ORDER BY con.contest_id;
                         
-- Advanced join
--15 Days of Learning SQL
-- Write a query to print total number of unique hackers who made at least 1 submission each day (starting on the 1st day of the contest), and find the hacker_id and name of the hacker who made maximum number of submissions each day. If more than one such hacker has a maximum number of submissions, print the lowest hacker_id. The query should print this information for each day of the contest, sorted by the date.
select 
submission_date, 
(select count(distinct hacker_id) from submissions s2 -- table with hackers who consecutively submit
  where s2.submission_date = s1.submission_date and
   (select count(distinct s3.submission_date) from submissions s3 
    where s3.hacker_id = s2.hacker_id and s3.submission_date < s1. submission_date)
    = datediff(s1.submission_date, '2016-03-01')), 
(select hacker_id from submissions s2 
  where s2.submission_date = s1. submission_date
   group by hacker_id
   order by count(submission_id) desc, hacker_id limit 1) tmp, (select name from hackers where hacker_id = tmp)
from (select distinct submission_date from submissions) s1
group by 1;


