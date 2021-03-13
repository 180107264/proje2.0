--What is Phish_Info_id where domain2 is www.qooqle.com?
SELECT phish_info_id
FROM Phish_Info a JOIN Phish2 b
ON a.phish2_id = b. phish2_id;