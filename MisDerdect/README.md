# MisDerdect

These topics are publicized through the official website of the Weibo Community Management Center. The center displays topics that have been officially identified as rumors by Weibo. We collected information on 2067 original topics. There were 1,000 rumor topics and 1,067 non-rumor topics. Meanwhile, we perform manual identification of derived topics based on official facts. Strong-related derivative topics were collected nearly 270,000 posts, and nearly 300,000 unrelated posts were randomly added. The set of Web-wide topics is composed of them together.

## Rumor set introduce

The first data set contains 1000 rumors in 2022.Each rumor data is collected from three aspects: comment collection, topic information, and multimedia information collection.

## non-Rumor set introduce

The data set contains 1067 non-rumors in 2022.Each non-rumor data is collected from three aspects: comment collection, topic information, and multimedia information collection.

## derive set introduce

Strong-related derivative topics were collected nearly 270,000 posts, and nearly 300,000 unrelated posts were randomly added.Each data is collected by topic information.

### comment collection

* **created_at**: Comment creation time.
* **id**: Comment ID.
* **text**: Comment content.
* **source**: Source of comments.
* **user**: Detailed comment user information.
* **mid**: Comment MID.
* **idstr**: Comment MID (string).
* **status**: Detailed comment microblog information.
* **reply_comment**: Comment source comment Return when this comment is a reply to other.


### topic information

* **mid**: Topic MID.
* **uid**: User ID.
* **name**: User nickname.
* **time**: Topic creation time.
* **iphone**: Client used for topic publishing.
* **retweet**: Number of retweets.
* **comment_num**: Number of comments.
* **like_num**: Number of likes.
* **author**: Official level of user account
* **focus**: Number of users following.
* **fans**: Number of user fans
* **tweet**: Number of topics sent by users

### multimedia information collection

This folder contains multimedia information in the published topic. For example, video and image.
