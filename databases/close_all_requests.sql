UPDATE Requests
SET Status='Closed'
WHERE AptID in (
		SELECT AptID
		FROM Apartments
		WHERE BuildingID = 11 
	)
)
