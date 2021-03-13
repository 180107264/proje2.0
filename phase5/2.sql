--which sites have the .com extension?
SELECT COUNT(*)
FROM Phish_Info
WHERE description LIKE '%.com';