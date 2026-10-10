-- Newly authored portfolio example, not original coursework SQL.
-- BigQuery Standard SQL. Replace the synthetic CTE with an authorised source table.
-- This query is read-only and does not create or modify tables.

WITH synthetic_source AS (
  SELECT 'sample_a' AS business_id, '2024-01-05 18:30:00,2024-01-06 12:00:00' AS date UNION ALL
  SELECT 'sample_b', 'bad-date,2024-01-07 09:00:00'
),
expanded AS (
  SELECT business_id, TRIM(token) AS raw_timestamp
  FROM synthetic_source, UNNEST(SPLIT(date, ',')) AS token
  WHERE TRIM(token) != ''
),
validated AS (
  SELECT business_id, SAFE.PARSE_TIMESTAMP('%Y-%m-%d %H:%M:%S', raw_timestamp) AS event_timestamp
  FROM expanded
)
SELECT
  COUNT(*) AS timestamp_tokens,
  COUNTIF(event_timestamp IS NOT NULL) AS valid_timestamps,
  COUNTIF(event_timestamp IS NULL) AS invalid_timestamps,
  COUNT(DISTINCT business_id) AS businesses
FROM validated;
