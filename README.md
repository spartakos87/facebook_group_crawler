# Facebook group crawler
This is a program which can extract from any existing group in Facebook these informations:

* posts
* reactions of each post
* likes
* shares
* comments,not just the number of commnet but the comments , whith any info which maybe include , like who make the comment ,how many likes it has etc

## What you need to run it
First of all you need to have install the [Python3](https://www.python.org/download/releases/3.0/) and [facepy](https://github.com/jgorset/facepy). The last thing you must have is a [Facebook app](https://developers.facebook.com/docs/apps/register#create-app), because at the begin you need to input facebook app id and app secret.

## How to run it
```bash
$python3 fun_page.py
```
The you have to give group id ,app id ,secret id and the name of file which want to save the extracted json

