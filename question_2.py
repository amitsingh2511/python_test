# SELECT customer_name, 
#     CASE
#         WHEN COUNT(*) = SUM(CASE WHEN status = 'DELIVERED' THEN 1 ELSE 0 END) THEN 'COMPLETED'
#         WHEN SUM(CASE WHEN status = 'DELIVERED' THEN 1 ELSE 0 END) > 0
#              AND (SUM(CASE WHEN status = 'CREATED' THEN 1 ELSE 0 END) > 0 OR SUM(CASE WHEN status = 'SUBMITTED' THEN 1 ELSE 0 END) > 0) THEN 'IN PROGRESS'
#         WHEN SUM(CASE WHEN status = 'SUBMITTED' THEN 1 ELSE 0 END) > 0 AND SUM(CASE WHEN status = 'DELIVERED' THEN 1 ELSE 0 END) = 0 THEN 'AWAITING PROGRESS'
#         ELSE 'AWAITING SUBMISSION'
#     END AS Final_Status
# FROM newtable
# GROUP BY customer_name
# ORDER BY customer_name;

