-- Import SQL DUmp.
-- script ranks country origin of bands
-- import a table dump
-- column names must be origin and nb_fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
