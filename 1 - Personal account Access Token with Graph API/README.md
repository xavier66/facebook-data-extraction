# Personal account Access Token + Graph API

Use your own Token with **almost full permission** for fetching data. This is the **MOST EFFECTIVE** method.

> The knowledge and the way to get **Access Token** below is translated from these 2 Vietnamese blogs:
>
> -   https://ahachat.com/help/blog/cach-lay-token-facebook
> -   https://alotoi.com/get-token-full-quyen

## Knowledge

### I. What is Facebook Token?

The Facebook token is a randomly generated code that contains the data associated with the Facebook account. Facebook Token, also known as **Access Token** will contain the permissions to perform an action on the library (API) provided by Facebook. Each Facebook account will have different **Access Tokens**. There may be 1 or more Tokens on the same Facebook account.

There are many ways to reach a destination, but for some reason we will have to choose only one, usually the shortest, fastest path. The **Access Token**is a shortcut to that destination. Understand simply Facebook Token is like that.

### II. What are Facebook tokens used for?

Facebook Token is now quite popular in the field of Facebook Marketing, depending on the limit of the permissions of each token. Some popular applications of Facebook Token:

-   Increase Facebook likes and subs.
-   Automatically post on Facebook.
-   Automatically comment, share articles.
-   Automatically interact in groups, pages.
-   ...

It is used for many different purposes, but the main goal is still to automate all manual operations. With Facebook Token, you can use some features that Facebook has not yet supported or supported in some countries. For example, you won't be able to do the feature of enabling the Facebook Avatar protection shield without using tokens (or Extensions) if in some other countries (India, Germany, ...), then you will find the option to enable shields right on the Facebook account itself.

### III. Facebook Token types

There are 2 types of Facebook Tokens: **Token by App** and **Token by Personal Account**. The Facebook Token by App is the safest one, as it will have a limited lifetime and only has some basic permissions to manipulate on pages and groups. So our main focus will on the Facebook **Token by Personal Account**.

### IV. Facebook Token by Personal Account

This is a **full permissions** token represented by a string of characters starting with `EAA...`, the purpose of this token is to represent your Facebook account to perform actions you can do on Facebook, such as sending messages, like pages, and posts to groups through `API`. Compared to **Token by App**, this token has a longer lifetime and more authority. To make it easier to understand what **Token by App** can do, **Token by Personal Account** can also, but not vice versa.

An example of using this token is that you want to post simultaneously to many groups and many pages; to do this, you cannot log in to each page or group to post because it will be very time-consuming. Just fill in a list of group and page ids, then call an `API` to post them all. Or as you often see on the market, there are tools to increase fake likes, and fake comments are also using this trick.

Note that using Facebook token can save you time, but you should not disclose this token to others because they can abuse it for bad purposes, by:

-   Do not download extensions to get tokens or login your phone number and password to websites that support getting tokens because your information will be exposed.
-   And if you suspect your token has been exposed, immediately change your Facebook password and delete the extensions installed in the browser. Or if you are more careful you can turn on **two-factor authentication** (2FA).

👉 To ensure the safety of using Facebook tokens for personal purposes and save time, as mentioned above, you should use the method of getting tokens directly on Facebook by following the steps below.

## Get full permissions Access Token

In the past, getting Facebook tokens were very simple. Now many Facebook services are developing. Getting Facebook tokens is becoming more and more difficult. Facebook also restricts Full rights tokens to avoid Spam and excessive abuse of user behaviors. Or you can get Token, but it will be limited by basic permissions that we do not use, that is nothing compared to sometimes having an account locked (identity verification).

Currently, this is the way to use the most. However, it may require you to authenticate with 2FA (via app or SMS Code). With these simple steps, you can get **almost full permission** token.

-   Go to https://business.facebook.com/content_management.
-   Press `Ctrl + U`, then `Ctrl + F` to find the code that contains `EAAG`. Copy the highlighted text, that's the Token you need to get.

    ![](https://alotoi.com/wp-content/uploads/2020/08/token-business.png)

-   You can go to this [facebook link](https://developers.facebook.com/tools/debug/accesstoken) to check the permissions of the above token.
    ![](https://lh4.googleusercontent.com/0S64t2sjFXjkX8HUjo2GeEW8hyKL88G4lMXkpNF7RgtFCRm0oVPRT--vnoM1rkMyhrRvvHufW9J0ZeP8tPxfo4j5vYityQFM0m06NTI2hq4zk1JMp59W9voHXHYtOjE7zqDGMlhh)

**Note**: I only share how to get **Access Token** from Facebook itself. Revealing tokens can seriously affect your Facebook account. Please refrain from getting tokens from unknown sources!

## Data extraction with Graph API

I wrote a [simple script](./crawler.py) to get data of posts from any page using [Facebook Graph API](https://developers.facebook.com/docs/graph-api)

### I. Usage

    python crawler.py

This [script](./crawler.py) needs 2 important parameters:

-   **ACCESS_TOKEN**: you can get this value with the [way](#get-full-permissions-access-token) mentioned above
-   **COOKIE**: when you have the **ACCESS_TOKEN**, follow these steps to get the **COOKIE**:
    -   Go to https://graph.facebook.com/me?access_token=YOUR_ACCESS_TOKEN_HERE
    -   Press F12 and reload.
    -   Go to the `Network` Panel and copy value of the `cookie` param in **Request Headers**.

### II. Recommendation

I have learned too much from this [repo](https://github.com/HoangTran0410/FBMediaDownloader). It's a NodeJs tool for auto download media from Facebook with lots of cool stuff:

-   View album information (name, number of photos, link, ...)
-   Download **timeline album** of a FB page: this kind of album is hidden, containing all the photos so far in that FB page, like [this album](https://www.facebook.com/groups/j2team.community/posts/1377217242610392/).
-   Download any kind of album: `user`'s, `group`'s, or `page`'s.
-   Download all photos/videos on the wall of an object (`user`/`group`/`page`).
-   To be able to download the above items, it also provided [scripts](https://github.com/HoangTran0410/FBMediaDownloader/blob/master/scripts/bookmarks.js) to extract `album_id` / `user_id` / `group_id` / `page_id`.

The only disadvantage is that the description and instructions of this [repo](https://github.com/HoangTran0410/FBMediaDownloader) are in Vietnamese, _my language_. But I think it's not too hard to understand, you can watch its [instruction video](https://www.youtube.com/watch?v=g4zh9p-QfAQ) for more information. Hopefully, in the future, the author will update the description as well as the instructions in English.
