-- get open request and the apt associated with it (just the apt, do NOT dedupe)
-- get the building associated with each apt
-- do a group by in which we group by building and count number of apts

SELECT buildingid, buildingname, count(requestid) as numreqs
FROM
    buildings left join
    (SELECT buildingid, requestid
    from apartments inner join requests using (aptid)
    WHERE status='Open') as building_reqs using (buildingid)
GROUP BY (buildingid, buildingname)
;

