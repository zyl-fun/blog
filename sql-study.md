### 多表连接

```
select Firstname, LastName, City, State from Person p left join Address a on p.PersonID = a.PersonID
```

### 查找N高数据

distinct 针对查询结果去除重复记录

```
SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
```

```
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    set n = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      select (select distinct Salary from Employee order by Salary desc limit 1 offset n ) as SecondHighestSalary
      
  );
END
```

### 排名

```
select a.Score as Score,
(select count(distinct b.Score) from Scores b where b.Score >= a.Score) as Rank
from Scores a
order by a.Score DESC
```

### 查找连续出现的数据

出现几次，就整几张一样的表，之后进行连续性判断和值判断

```
SELECT DISTINCT
    l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num

```

### 表的自身连接

```
select e1.Name as Employee from Employee e1, Employee e2 where e1.ManagerId = e2.Id and e1.Salary > e2.Salary
```

### 查找重复值

```
select distinct(p1.Email) as Email from Person p1, Person p2 where p1.Email = p2.Email and p1.Id != p2.Id
```

### 删除重复值

表的自身连接

```
delete a from Person a, Person b where a.Email = b.Email and a.Id > b.Id
```



### 查找从未出现的数据

```
select c.Name as Customers from Customers c where c.Id not in (select CustomerId from Orders)
```

### 查找各部门工资最高的数据

```
select d.Name as Department, e.Name as Employee, e.Salary as Salary from Employee e left join Department d on e.DepartmentId = d.Id where (e.DepartmentId, e.Salary) in (select DepartmentId, max(Salary) from Employee group by DepartmentId)
```

### 查找各个部门前N高的数据

```mysql
select d.Name as Department, e.Name as Employee, e.Salary as Salary from Employee e left join Department d on e.DepartmentId = d.Id where 3 > (select count(distinct(e2.Salary)) from Employee e2 where e2.Salary > e.Salary and e2.DepartmentId = e.DepartmentId)
```

### 日期数据的比较

```
select w1.Id from Weather w1, Weather w2 where DATEDIFF(w1.RecordDate, w2.RecordDate) = 1 and w1.Temperature > w2.Temperature
```

### 订单取消率的计算

```
select t.Request_at as Day ,ROUND(sum(CASE WHEN t.Status != 'completed' THEN 1 ELSE 0 END) / COUNT(t.Id),2) as 'Cancellation Rate'
from Trips t, Users u1, Users u2 where (t.Client_Id = u1.Users_Id and u1.Banned = 'No' and t.Driver_Id = u2.Users_Id and u2.Banned = 'No' ) and t.Request_at BETWEEN '2013-10-01' and '2013-10-03' GROUP BY t.Request_at
```

### 超过某个数值的数据

```
select c1.class from courses c1  group by c1.class having count(c1.student) >= 5
```

### 高峰期

```
select distinct s1.* from stadium s1, stadium s2, stadium s3 where ((s1.id = s2.id - 1 and s3.id = s2.id + 1) or (s1.id - 1 = s2.id and s1.id - 2 = s3.id) or (s1.id - 1 = s2.id and s1.id + 1 = s3.id )) and (s1.people >= 100 and s2.people >= 100 and s3.people >= 100 )order by s1.id
```

### 数学函数 

abs 绝对值

ceil 向上取整

floor 向下取整

round（x,d） 四舍五入,d为保留的小数点位数

pow(x,y) x的y次幂

rand 0,1 之间随机小数

mod 求模

### 交换相邻数据

使用 CASE 函数

```
select (CASE when mod(id ,2) !=0 and id != counts then id + 1 when mod(id,2)!= 0 and id = counts then id else id - 1 end) as id , student from seat,(select count(*) as counts from seat) as stu_counts order by id asc
```

### update 更新数据

```
update salary set sex = case  sex when 'm' then 'f' else 'm' end 
```

### 考察分类

```
select id,
       sum(case
               when month = 'Jan'
                   then revenue
           end) as Jan_Revenue,
       sum(case
               when month = 'Feb'
                   then revenue
           end) as Feb_Revenue,
       sum(case
               when month = 'Mar'
                   then revenue
           end) as Mar_Revenue,
       sum(case
               when month = 'Apr'
                   then revenue
           end) as Apr_Revenue,
       sum(case
               when month = 'May'
                   then revenue
           end) as May_Revenue,
       sum(case
               when month = 'Jun'
                   then revenue
           end) as Jun_Revenue,
       sum(case
               when month = 'Jul'
                   then revenue
           end) as Jul_Revenue,
       sum(case
               when month = 'Aug'
                   then revenue
           end) as Aug_Revenue,
       sum(case
               when month = 'Sep'
                   then revenue
           end) as Sep_Revenue,
       sum(case
               when month = 'Oct'
                   then revenue
           end) as Oct_Revenue,
       sum(case
               when month = 'Nov'
                   then revenue
           end) as Nov_Revenue,
       sum(case
               when month = 'Dec'
                   then revenue
           end) as Dec_Revenue
from department
group by id;
```

