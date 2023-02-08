# AirBnB Clone - The Console

This project is to create a Console to access and manipulate data for the AirBnB Clone website.

This console is a single-used function, a Command Line Interface (CLI) from which devs can Create, Read, Update, and Delete (CRUD) objects in file storage.

It is a testing tool, a sandbox where devs can play around with ideas, to see what does and doesn't work in the file storage, before building out the rest of the web application.

To start the Console, just type-in the following command and press `ENTER`:

```bash
./console.py
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
