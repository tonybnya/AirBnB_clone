# AirBnB Clone - The Console

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230213%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230213T082737Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=380d929e09cded1c4b69c498fee2b0aacde926fc7dd3af1d464627d1f06dd242)



This project is to create a Console to access and manipulate data for the AirBnB Clone website.

This console is a single-used function, a Command Line Interface (CLI) from which devs can Create, Read, Update, and Delete (CRUD) objects in a file storage.

It is a testing tool, a sandbox where devs can play around with ideas, to see what does and doesn't work in the file storage, before building out the rest of the web application.

To start the Console, just type in your shell terminal the following command and press `ENTER`:

```bash
./console.py
```

A prompt will appear in which you can enter some defined commands.

```bash
(hbnb) 
```

Here are some uses cases:

1.Interactive Mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

2.Non-Interactive Mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
