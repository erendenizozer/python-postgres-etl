SELECT
    post_id,
    title,
    body
FROM {{ ref('stg_posts') }}