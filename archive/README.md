# intervals
running intervals

I want a running app eventually on my Android phone which will do the following:
* let user set length of intervals
* let user set number of intervals
* let user set length of walking breaks
* set these loose in a while loop that runs down the number of intervals
* tells user when to run & when to walk with Text-To-Speech
  - every platform is different.  right now in python this just uses my linux system,
    so this won't work anywhere but on a similar OS, much less an android phone.  Hard
* runs in the background (hard [might just be telling user to add to battery saver exceptions?])
* extremely EXTREMELY light UI (extremely hard, 4 me).
  - Unstyled HTML page with integer-only fields as captured values is probably sufficient for me
