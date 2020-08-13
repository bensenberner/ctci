-- get open request and the apt associated with it (just the apt, do NOT dedupe)
-- get the building associated with each apt
-- do a group by in which we group by building and count number of apts

SELECT
	BuildingID,
	COUNT(BuildingID)
FROM 
	Apartments
	INNER JOIN (
		SELECT
			AptID
		FROM
			Requests
		WHERE
			Status='Open'
	) as request_apt
	ON Apartments.AptID = request_apt.AptID
GROUP BY
	BuildingID
;
