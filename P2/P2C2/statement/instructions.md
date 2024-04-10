# Instructions  
In your development environment, write a class definition for each of those classes (using subclasses where relevant).

Assume that, for now, you’re just printing a post’s content to the terminal. We’ll deal with displaying threads later, so just use  `pass`  for that method for now.

When you don’t know how to implement a method, you can use  `pass`  as that method’s body. Use your judgment when implementing these methods. Remember to include constructors for each class!

### Reminder 

Last chapter classes descriptions : 

| File                   | Image     |
| ---------------------- | --------- |
| **State**<br>name<br>size  | **State** <br>image_size<br><br>    |
| **Behaviour**<br>display() | **Behaviour**<br><br> |

| User                   | Moderator     |
| ---------------------- | --------- |
| **State**<br>username<br>password  | **State** <br><br><br>    |
| **Behaviour**<br>login()<br>post(thread, content)<br>make_thread(title, content) | **Behaviour**<br>edit(post, content)<br><br><br> |

| Post                   | FilePost     |
| ---------------------- | --------- |
| **State**<br>user<br>time_posted<br>content | **State** <br>file<br><br><br>    |
| **Behaviour**<br>display() | **Behaviour**<br><br> |


| Thread                   |
| ---------------------- | 
| **State**<br>title<br>time_posted<br>posts |
| **Behaviour**<br>display()<br>add_post(post) |