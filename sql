-- Select cities that ends with either a,e,i,o u or ends with those vowels.
select distinct city from station where city regexp "^(a|e|i|o|u)" and city regexp "(a|e|i|o|u)$";

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

--
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

