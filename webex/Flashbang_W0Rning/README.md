# Flashbang_W0Rning
Here's your daily dose of brainrot....

hints:
1. no robots allowed.
2. Our roots are our foundation.

Solution:
In this challenge, we are directed to a webpage with some random brainrot, for your own sanity don't read it. 

1. checking the robots.txt file, we find there's a disallowed page called secret.
2. accessing secret says that "I am Bond, James Bond", which is clue to changing User-Agent to James Bond.
3. accessing the page again tells us "Lets go back to our roots." With a link of mist linkedin which tells that there's a query parameter for "our roots" which is for year in which mist was founded (2016).


Final URL: domain/secret?year=2016


Flag: wtfCTF{all_this_gen_alpha_stuff_is_crazy}
