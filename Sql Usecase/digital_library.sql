--Database creation
CREATE DATABASE college_library;
USE college_library;

--students table
CREATE TABLE Students (
student_id INT PRIMARY KEY,
 student_name VARCHAR(100),
last_active_date DATE
);

-- books table
CREATE TABLE Books (
 book_id INT PRIMARY KEY,
book_title VARCHAR(150),
category VARCHAR(50)
);

--issued books table
CREATE TABLE IssuedBooks (
issue_id INT PRIMARY KEY,
 student_id INT,
 book_id INT,
issue_date DATE,
return_date DATE,
FOREIGN KEY (student_id) REFERENCES Students(student_id),
 FOREIGN KEY (book_id) REFERENCES Books(book_id)
);


-- Input data

INSERT INTO Students VALUES
(1, 'Vishnu', '2025-01-24'),
(2, 'Tharun', '2021-11-01'),
(3, 'Sankho', '2024-06-26'),
(4, 'Akash', '2020-02-15'),
(5, 'Rishi', '2023-12-10');

INSERT INTO Books VALUES
(101, 'Steal like an artist', 'Self help'),
(102, '$100M Offers', 'Business'),
(103, 'Show your work', 'Self help'),
(104, 'The lean startup', 'Business'),
(105, 'Keep going', 'Self help');

INSERT INTO IssuedBooks VALUES
(1, 1, 101, '2026-04-08', NULL),
(2, 2, 102, '2026-03-01', '2026-03-10'),
(3, 3, 103, '2026-03-20', NULL),
(4, 4, 104, '2026-02-01', '2026-02-20'),
(5, 1, 105, '2026-01-15', '2026-01-30');


-- overdue books (more than 14 days and not returned)

SELECT 
 s.student_name,
 b.book_title,
i.issue_date
FROM IssuedBooks i
JOIN Students s ON i.student_id = s.student_id
JOIN Books b ON i.book_id = b.book_id
WHERE i.return_date IS NULL
AND DATEDIFF(CURDATE(), i.issue_date) > 14;


-- popular categories

SELECT 
 b.category,
  COUNT(*) AS total_count
FROM IssuedBooks i
JOIN Books b ON i.book_id = b.book_id
GROUP BY b.category
ORDER BY total_count DESC;


-- remove inactive students who are greater than 3 years)

DELETE FROM Students 
WHERE 
last_active_date < DATE_SUB(CURDATE(), INTERVAL 3 YEAR);