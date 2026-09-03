SELECT
    id AS post_id,
    title,
    body
FROM {{ source('raw', 'raw_data') }}