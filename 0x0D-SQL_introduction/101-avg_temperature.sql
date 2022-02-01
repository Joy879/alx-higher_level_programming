-- Computes the average of a group of records in a table in the database
SELECT city, AVG(value) AS avg_temp FROM temperatures
    GROUP BY city
    ORDER BY avg_temp DESC;
