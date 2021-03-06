SELECT
	TenantName
FROM
	Tenants
INNER JOIN (
	SELECT
		TenantID
	FROM
		AptTenants
	GROUP BY
		TenantID
	HAVING
		COUNT(AptID) > 1
	) C
ON Tenants.TenantID = C.TenantID;
