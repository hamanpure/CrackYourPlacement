# Write your MySQL query statement below
select m2.machine_id, round(sum(m2.timestamp  - m1.timestamp)/count(m1.machine_id), 3) as processing_time from 
Activity as m1 
join Activity as m2
on
m1.machine_id = m2.machine_id and
m1.process_id  = m2. process_id and 
m1.activity_type = "start" and 
m2.activity_type = "end"

GROUP BY 
m1.machine_id;
