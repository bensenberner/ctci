drop TABLE IF EXISTS Students;
drop TABLE IF EXISTS Courses;
drop TABLE IF EXISTS StudentCourses;

create table if not exists Students(
    StudentID   int primary key,
    StudentName varchar(60)
);
create table if not exists Courses(
    CourseID int primary key,
    CourseTitle varchar(60)
);
create table if not exists StudentCourses(
    StudentID   int,
    CourseID    int,
    Grade       decimal,
    primary key (StudentID, CourseID)
);

INSERT INTO Students VALUES
(1, 'Ben'),
(2, 'Jules'),
(3, 'Sash'),
(4, 'John'),
(5, 'Wern')
;

INSERT INTO Courses VALUES
(1, 'Herbology'),
(2, 'Physics')
;

INSERT INTO StudentCourses (studentid, courseid, grade) values
(1, 1, 4.0),
(1, 2, 3.9),
(2, 1, 4.5),
(3, 1, 3.2),
(3, 2, 3.5),
(4, 2, 3.4)
;

(select
    studentname,
    coalesce(avg(grade), 0) as gpa
FROM (students left join studentcourses using (studentid))
GROUP BY (studentid)
ORDER BY gpa desc
) AS grades
;
