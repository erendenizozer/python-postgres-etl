def transform_posts(posts):
    transformed_posts = []

    for post in posts:
        if not post["id"]:
            continue
        if not post["title"]:
            continue
        if not post["body"]:
            continue

        transformed_post = {
            "id": post["id"],
            "title": post["title"].strip(),
            "body": post["body"].strip()
        }

        transformed_posts.append(transformed_post)

    return transformed_posts