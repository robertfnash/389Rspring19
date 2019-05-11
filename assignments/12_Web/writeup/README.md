# Web Writeup

Name: Robert Nash
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Robert Nash
## Assignment Writeup

### Part 1 (40 Pts)

After exploring the website we notice that the site does SQL queries to a table called item. We try to exploit this by adding `' OR 'a'='a` to end.

When we did this we got an ERROR stating that SQL injection was attempted. The website is checking for the use of the word `OR`. Instead of `OR` we change it to `||` s.t. the command is now `' || 'a'='a`

This works and we get our flag.

`CMSC389R-{y0u_ar3_th3_SQ1_ninj@}`

### Part 2 (60 Pts)

**Level 1**

To run an alert in javascript you type `<script>alert('CMSC389R');</script>`. I simply put this is the search input to test it and it worked.

**Level 2**

This page allows you to post content in a forum.

Again I entered in the script `<script>alert('CMSC389R');</script>` to see what would happen. An empty post was made. The first pot made suggests that the page allows users to insert HTML. So I made a post with the onclick command in HTML.

`<button onclick="alert('CMSC389R')">Click me</button>`

Now the post a button that says "Click me" and when clicked, an alert is executed.

**Level 3**

This level doesn't have any direct input. Playing around and clicking the button shows that url `frame#` mimicks the Image #. If we change the url to `frame#2` it goes to Image 2. Change it to `frame#9` it tries to go to Image 9 (even though there isn't one). When this is done, the website does reveal some source code. It shows `?.jpg'/>`. This suggests the site is running some line `"blahblahblah .jpg'/>`. So we will tryo to escape the code by inserting `'/><script>alert('CMSC389R');</script>` so that the code that runs looks like this `"blahblahblah'/><script>alert('CMSC389R');</script> .jpg'/>`.

We tried it and it works.

**Level 4**

Right away we see that we can input a number and a timer will start for that amount of seconds.

Looking at the source code we can see that the way the timer is called looks like this:

`onload="startTimer('{{ timer }}');`

Where "timer" is the value that we input. To get the function to run our code we will make our input escape the function and complete our function by using the leftover `')`.

Our input becomes `');alert('CMSC389R` such that the entire command that is run becomes `onload="startTimer('');alert('CMSC389R');`

**Level 5**

This site asks you to sign up for something. Clicking signup asks for an email as input. Typing in an arbitrary email, the site goes to a confirm page, waits a bit and sends you back to the front.
Playing around with site we see that at the signup page, the URL shows that if we select the "Next" button, it should send us to the confirm page. If we change the url to execute javascript instead, we could get an alert.

We replace `confirm` with `javascript:alert('CMSC389R');` and click `Next`.  Our alert is executed.

**Level 6**

This website calls and loads a `.js` form somewhere else. In this case it is calling `gadget.js`. So for this site, you can change the url so that it loads a `.js` from a remote site or pastebin but I went ahead and used the hint and used `https://google.com/jsapi?callback=foo`, replacing `foo` with `alert`.

After updating the url, the website says it won't load `http` and uses a regex to validate input. It specifically checks for lower case `http` so I changed it to `Http`. This bypasses the validation and the alert is run.




