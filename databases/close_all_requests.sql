UPDATE Requests
SET Status='Closed'
WHERE RequestID IN (
	SELECT DISTINCT RequestID
	FROM Requests INNER JOIN (
		SELECT AptID
		FROM Apartments
		WHERE BuildingID = 11 
	) as apts ON Requests.AptID = apts.AptID
)
