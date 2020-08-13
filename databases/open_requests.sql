-- get open request and the apt associated with it (just the apt, do NOT dedupe)
-- get the building associated with each apt
-- do a group by in which we group by building and count number of apts

select
    buildingname, num_reqs
from
    buildings inner join (
select
	buildingid,
	count(requestid) as num_reqs
from
	Apartments
	left join (
		select
			AptID, requestid
		from
			Requests
		where
			Status='Open'
	) as request_apt
	using (aptid)
group by
    buildingid
) B using (buildingid)
;
