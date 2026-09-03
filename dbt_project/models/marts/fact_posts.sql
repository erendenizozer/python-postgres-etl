SELECT
    post_id,
    LENGTH(title) AS title_length,
    LENGTH(body) AS body_length,
    LENGTH(title) + LENGTH(body) AS total_length
FROM {{ ref('dim_posts') }}