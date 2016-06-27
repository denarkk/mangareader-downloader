## Web-Scraper for mangareader.net

The main objective of this project is to type in the name of a manga series, the episode number and then a script that we're going to create is gonna download each page of the episode in our machine. Web scraping is a technique that's used to parse the HTML inside a website and collect the data that is needed, store it somewhere and or use it. It can be automated with loops and complex algorithms to perform tasks that would regularly take us a lot of time to complete. Imagine you want to read episodes of manga on your Kindle and thus you need to download them, but what if you can't find them outside the regular manga-reading websites like mangapanda or mangafox? You use them! But instead of dowloading the pages one by one, you automate this task with the beauty that is web scraping.

**DISCLAIMER**: If you enjoy a manga series, always pay respect and money to the Mangakas (creators) to compensate 'em for their hard work and dedication. I am not encouraging you to download scanned manga (it's sort of illegal) in any way, shap or form, this is just for educational purposes only!

#### Requirements
1. **Python 2.7 or 3.x**: [https://www.python.org](https://www.python.org)
2. **PIP**: Find out more about it [here](https://www.google.com.mx#q=how+to+install+pip&gws_rd=cr)
3. **BeautifulSoup 4**: [https://www.crummy.com/software/BeautifulSoup/#Download](https://www.crummy.com/software/BeautifulSoup/#Download)
4. **Requests**: [http://docs.python-requests.org/en/master/](http://docs.python-requests.org/en/master/)

## The main plan

Which site to download from? http://www.mangareader.net/ of course. It provides a well defined URL structure that we can assemble to send the HTTP requests and also returns the appropriate server responses. The HTML inside doesn't take much science to parse and read through, the image is under an *id* and a *name* of "img".

#### Steps to follow

First we need to set a file with global constants that can be changed in one place and affect the whole project, for example, if we want to change the directory where the images should be stored we can just change the constant's value. Other constants we may need are the messages to be displayed at certain points, the provider's base URL (mangareader.net/) and other stuff we can find out later on.

Since this is going to be a console utility, the console API provides python with something called **"system arguments"**, which are parameters that you can pass to the utility and use them. The name of the series and the episode number will be those parameters, we need to use the `sys.argv` array to access and use them. For that we can write our main logic/algorithm inside a function (if you want to export it as a module) and accept two arguments: the name of the manga series to be downloaded and the episode, both are strings.

Set the current page to the initial page global constant and **assemble the download path** with the series name and the episode number, just to keep things organized for the end-user. Then, send a request to the first page of the episode, mangareader provides us with a clear message that says "This episode is not released yet..." when the episode is yet to be released or the series ended and that episode outright won't ever be released. So we can fetch the raw HTML code from that page and search for the keywords **"not released"**, if it's not released yet we can go ahead and terminate the main function.

Now is the time to think about autimating the process with a loop, we could determine the exact amount of pages the manga episode has but that'd require extra effort and thinking (more data scraping and an extra http request)! We can save us some of that effort and just create an **infinite While Loop** that only breaks when the html is empty, which means the user got the manga name wrong or it doesn't exist, it also means the current page doesn't exist so we are 100% sure we have reached **the end of the episode** and there's nothing more to download. The aforementioned event happens when the server sends back a 404 error, we could specifically check for that error but we may need to check when the **server response code** is not 200 (success), just to account for extra error codes like 500 for example.

Inside the loop we **assemble the URL of the page** to be downloaded using the "current page" variable and send the request to get back the raw html and the response code (for breaking the loop), we use **BeautifulSoup** to search for JUST ONE image tag with the id of "img", it'd be ridiculous if there were more than one id's with that name and we only want one image anyway, there's a method called "findAll" but we only want **ONE image tag**. After we parsed and scraped the image tag, we want to get the **source attribute** as a string (the link to the episode's jpg image).

Here's an example of a portion of the parsed HTML code of the page's URL:

``` html
<img id="img" width="800" height="1167" src="http://i5.mangareader.net/naruto/3/naruto-1564848.jpg" alt="Naruto 3 - Page 1" name="img" /></a>
```

Now that we have our image url, we can go ahead and send a request but this time we want the contents of the image to be **copied to a file** which will be opened in **Binary Writing** mode, this file will contain the decoded binary data of the image in .jpg format (it can be any other extension dependin on the provider) and it won't stop until it finishes if we use `stream = True` inside the request next to the url parameter. The copying of the decoded binary data of the image into a new file is performed by the *Shutil* library which is already integrated in Python. Bofore any of that happens, we should **create the directory** if it doesn't exist, the way it's done, is with the help of the *OS* library.

And lastly, inside the loop, we **increment the counter** variable (current page) for the loop to keep iterating through the episode pages and eventually stop, otherwise, we'd be stuck in an infinite While Loop!

## Strategies and considerations

The **modular** approach will be better in a long term, if we convolute our manga.py file we may end up spending more time finding what we want or need to change than actually doing a useful change to our code. That's why we'll be separating the code into 4 files (one main and three modules):

1. **manga.py**: This is the file where the main logic will happen.
2. **request.py**: In here we send our requests and perform file operations.
3. **stringhelpers.py**: Little algorithms to assemble URLs or help with string manipulation.
4. **settings.py**: The global constants that will make easy to change little things.

We also need to take Connection **Exceptions** in consideration while working with the *Requests* library, if something goes wrong like no internet connection or if we mistyped the provider URL, the DNS can be resolved or any other network error, the program will exit with a big error message provided by the Python interpreter. So what's the deal? We like errors, don't we? Yes but it'd be nice to show the user a simplified error message and then exit the program! We can do this with the **try/catch** approach that we use in many programming languages.

Lastly, have you ever seen how some **sorting** algorithms like to treat number-named files oddly? Say you have the following array of files in a folder somewhere in your hard drive: `1.zip, 2.zip, 3.zip, 4.zip, 5.zip, 6.zip, 7.zip, 8.zip, 9.zip, 10.zip`, what do you think will happen if we sort them by name? The "10.zip" file will be right after the "1.zip" because both start with the number 1! We can avoid that by adding a **trailing zero(s)** to the files lower than 10, like this: `01.zip, 02.zip, 03.zip, 04.zip, 05.zip, 06.zip, 07.zip, 08.zip, 09.zip, 10.zip`. The same goes if we had a "100.zip" file, we should add two zeros to files below 10 and one zero to files below 100 but above 9 (notice we're speaking about integers here). When saving the pages in the hard drive, we could make sure we add those trailing zeros, just for sorting purposes.
