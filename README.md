# **CoREtex-Manager-Assistant**

This application can be used by the CoREtex Manager to keep track of all the books in the CoREtex and if anyone has borrowed them.

The Python code can be viewed [here](https://github.com/Ajahni1016/CoREtex-Manager-Assistant/blob/main/CoREtexManager.py).

When the program is launched, the user is met with the following screen with options to choose from:
![image](https://user-images.githubusercontent.com/42648282/169916726-6b31ac64-24d4-480c-a411-7a1340a7d9e8.png)

All the books are saved in a [JSON file](https://github.com/Ajahni1016/CoREtex-Manager-Assistant/blob/main/coretexBooks.json) 
![image](https://user-images.githubusercontent.com/42648282/169919350-573a7a74-4599-472e-8d9b-9bbca2ae12ee.png)


## Searching for a book
The user can search books by title, author, or ISBN number. The search is not case sensitive and allows partial text matching, so the title does not need to be inputted in entirety. The ISBN can be typed in with or without hyphens.

![search](https://user-images.githubusercontent.com/42648282/169918965-ebc97472-62ea-425e-9b9d-97532a0d380e.gif)

## Searching by genre
Books can also be searched by genre. A list of genres is displayed and the user can either search using the name of a genre or using its respective number in the list.

https://user-images.githubusercontent.com/42648282/169919887-30374797-b21b-4fab-b41f-9bc3e8d2a45d.mp4

## Borrowed books
This tool can be used to keep track of how many books are being borrowed by CoRE members. If the user selects option 3, it displays a list of all the books that are currently checked out.

![borrow](https://user-images.githubusercontent.com/42648282/169920531-cc6af693-b178-4616-8837-e2560dabdc0e.gif)

##  View all books
Selecting option 5 will display a list of all the books that CoRE owns.

![all](https://user-images.githubusercontent.com/42648282/169920682-f4394cb0-6984-45f6-b59c-47ed83fe7c17.gif)

## GUI Version
I have also been playing around with Android Studio to create a mobile version of this assistant. Currently, it isn't fully functional and only the frontend is complete. The code for this can be viewed [here]() and [here]().

![image](https://user-images.githubusercontent.com/42648282/169921132-ad5b16a4-b322-4a99-bd59-2c5b8438577d.png)

