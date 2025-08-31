--  Sample employee database 
--  See changelog table for details
--  Copyright (C) 2007,2008, MySQL AB
--  
--  Original data created by Fusheng Wang and Carlo Zaniolo
--  http://www.cs.aau.dk/TimeCenter/software.htm
--  http://www.cs.aau.dk/TimeCenter/Data/employeeTemporalDataSet.zip
-- 
--  Current schema by Giuseppe Maxia 
--  Data conversion from XML to relational by Patrick Crews
-- 
-- This work is licensed under the 
-- Creative Commons Attribution-Share Alike 3.0 Unported License. 
-- To view a copy of this license, visit 
-- http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to 
-- Creative Commons, 171 Second Street, Suite 300, San Francisco, 
-- California, 94105, USA.
-- 
--  DISCLAIMER
--  To the best of our knowledge, this data is fabricated, and
--  it does not correspond to real people. 
--  Any similarity to existing people is purely coincidental.
-- 

DROP DATABASE IF EXISTS perpustakaan;
CREATE DATABASE IF NOT EXISTS perpustakaan;
USE perpustakaan;

-- SELECT 'CREATING DATABASE STRUCTURE' as 'INFO';
-- SELECT perpustakaan;

DROP TABLE IF EXISTS ID,
                     judul_buku,
                     pengarang,
                     kategori_buku, 
                     penerbit, 
                     tahun_terbit,
                     kota_penerbit,
                     pages;

/*!50503 set default_storage_engine = InnoDB */;
/*!50503 select CONCAT('storage engine: ', @@default_storage_engine) as INFO */;

CREATE TABLE perpustakaan1 (
    ID      VARCHAR(10)             NOT NULL,
    judul_buku  VARCHAR(75)		NOT NULL,
    pengarang  VARCHAR(55)		NOT NULL,
    kategori_buku   VARCHAR(100)     NOT NULL,
    penerbit      VARCHAR(255)	  NOT NULL,    
    tahun_terbit  INT		NOT NULL,
    jumlah_buku		INT				NOT NULL,
    kota			VARCHAR(100)		NOT NULL,
    pages			INT			NOT NULL,
    PRIMARY KEY (ID)
);

INSERT INTO perpustakaan1 (ID, judul_buku, pengarang, kategori_buku, penerbit, tahun_terbit, jumlah_buku, kota, pages) 
		VALUES('A1', "A Child's History of the world", 'v.m hillyer', 'Sejarah', 'Appleton century croft', 1952, 56, 'New york', '502'),
                ('A2', 'Petroleum Geology of South east asia', 'geological society Special publication', 'Science', 'The Geological Society', 1997, 103, 'London', '436'),
                ('A3', 'The story book of science', 'Jean Henri Fabre', 'Story Science', 'the century co', '1917', '155', 'New York', '400'),
                ('A4', 'Cat sTories', 'James Herriot', 'Sastra', 'Gramedia', '2012', '321', 'Jakarta', '216'),
                ('A5', 'the intelligent Investor', 'Benjamin Graham', 'economic', 'Serambi ilmu semesta', '2008', '217', 'Jakarta', '747'),
                ('A6', 'Sistem operasi UNIX', 'Abdul Kadir dan Fetra Syahbana', 'komputer', 'Elex Media Komputindo', '1995', '567', 'Jakarta', '668'),
                ('A7', 'Sejarah Tuhan', 'Karen Armstrong', 'Filsafat', 'Mizan', '2001', '445', 'Bandung', '581'),
                ('A8', 'Python Programming', 'John Smith', 'Programming', 'O\'Reilly Media', 2022, 332, 'San Francisco', 450),
				('A9', 'Data Science Handbook', 'Jane Doe', 'Data Science', 'Wiley', 2021, 113, 'New York', 380),
				('A10', 'Machine Learning Basics', 'Robert Johnson', 'AI', 'Springer', 2020, 201, 'Berlin', 520);
                
-- CREATE TABLE departments (
--     dept_no     CHAR(4)         NOT NULL,
--     dept_name   VARCHAR(40)     NOT NULL,
--     PRIMARY KEY (dept_no),
--     UNIQUE  KEY (dept_name)
-- );

-- CREATE TABLE dept_manager (
--    emp_no       INT             NOT NULL,
--    dept_no      CHAR(4)         NOT NULL,
--    from_date    DATE            NOT NULL,
--    to_date      DATE            NOT NULL,
--    FOREIGN KEY (emp_no)  REFERENCES employees (emp_no)    ON DELETE CASCADE,
--    FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE,
--    PRIMARY KEY (emp_no,dept_no)
-- ); 

-- CREATE TABLE dept_emp (
--     emp_no      INT             NOT NULL,
--     dept_no     CHAR(4)         NOT NULL,
--     from_date   DATE            NOT NULL,
--     to_date     DATE            NOT NULL,
--     FOREIGN KEY (emp_no)  REFERENCES employees   (emp_no)  ON DELETE CASCADE,
--     FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE,
--     PRIMARY KEY (emp_no,dept_no)
-- );

-- CREATE TABLE titles (
--     emp_no      INT             NOT NULL,
--     title       VARCHAR(50)     NOT NULL,
--     from_date   DATE            NOT NULL,
--     to_date     DATE,
--     FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE,
--     PRIMARY KEY (emp_no,title, from_date)
-- ) 
-- ; 

-- CREATE TABLE salaries (
--     emp_no      INT             NOT NULL,
--     salary      INT             NOT NULL,
--     from_date   DATE            NOT NULL,
--     to_date     DATE            NOT NULL,
--     FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE,
--     PRIMARY KEY (emp_no, from_date)
-- ) 
-- ; 

-- CREATE OR REPLACE VIEW dept_emp_latest_date AS
--     SELECT emp_no, MAX(from_date) AS from_date, MAX(to_date) AS to_date
--     FROM dept_emp
--     GROUP BY emp_no;

-- # shows only the current department for each employee
-- CREATE OR REPLACE VIEW current_dept_emp AS
--     SELECT l.emp_no, dept_no, l.from_date, l.to_date
--     FROM dept_emp d
--         INNER JOIN dept_emp_latest_date l
--         ON d.emp_no=l.emp_no AND d.from_date=l.from_date AND l.to_date = d.to_date;

-- flush /*!50503 binary */ logs;

-- SELECT 'LOADING departments' as 'INFO';
-- source load_departments.dump ;
-- SELECT 'LOADING employees' as 'INFO';
-- source load_employees.dump ;
-- SELECT 'LOADING dept_emp' as 'INFO';
-- source load_dept_emp.dump ;
-- SELECT 'LOADING dept_manager' as 'INFO';
-- source load_dept_manager.dump ;
-- SELECT 'LOADING titles' as 'INFO';
-- source load_titles.dump ;
-- SELECT 'LOADING salaries' as 'INFO';
-- source load_salaries1.dump ;
-- source load_salaries2.dump ;
-- source load_salaries3.dump ;

-- source show_elapsed.sql ;
show tables;
describe perpustakaan1;
show create table perpustakaan1;
select * from perpustakaan1;
show databases;