				0x00. AirBnB clone - The console


		Concepts

	For this project, students are expected to look at these concepts:

	.Python packages

	.AirBnB clone

			Welcome to the AirBnB clone project!

	This is the first step towards building the first full web application: the AirBnB clone. 
	This first step is very important because it will used during the  building of the 
	project with all other following projects: 

	HTML/CSS templating, database storage, API, front-end integration…


	.put in place a parent class (called BaseModel) to take care of the initialization, 
	serialization and deserialization of your future instances

	.create a simple flow of serialization/deserialization: 
	Instance <-> Dictionary <-> JSON string <-> file

	.create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel

	.create the first abstracted storage engine of the project: File storage.

	.create all unittests to validate all our classes and storage engine

			The Console

	This software is a command interpreter similar to a Linux shell but limited to a 
	specific use-case; management of objects in the AirBnB Clone:

	.Create a new object (ex: a new User or a new Place)

	.Retrieve an object from a file, a database etc…

	.Do operations on objects (count, compute stats, etc…)

	.Update attributes of an object

	.Destroy an object


		It can work in two different modes:

		Interactive and Non-interactive.

	.In Interactive mode, the console will display a prompt (hbnb) indicating that the user 
	can write and execute a command. 
	.After the command is run, the prompt will appear again a wait for a new command. 
	.This can go indefinitely as long as the user does not exit the program.


	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb) 
	(hbnb) 
	(hbnb) quit
	$


		In Non-interactive mode, 

	the shell will need to be run with a command input piped into its execution so that the 
	command is run as soon as the Shell starts. 
	In this mode no prompt will appear, and no further input will be expected from the user.

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


	Format of Command Input

	In order to give commands to the console, these will need to be piped through an 
	echo in case of Non-interactive mode.

	In Interactive Mode the commands will need to be written with a keyboard when the prompt 
	appears and will be recognized when an enter key is pressed (new line). 
	As soon as this happens, the console will attempt to execute the command through 
	several means or will show an error message if the command didn't run successfully. 
	In this mode, the console can be exited using the CTRL + D combination, CTRL + C, 
	or the command quit or EOF.

	Arguments

	Most commands have several options or arguments that can be used when executing the program. 	In order for the Shell to recognize those parameters, 
	the user must separate everything with spaces


	CMD Commands
	Command	 			   Description				Sample Usage
	Help		Show all available commands			help
	Quit	        Exit to the prompt				quit
	Create	        Create a new object				create class
	Show	        Retrieve an object from a file			show class name id
	All	        Display all objects in class			all class
	Update   	Update objects and attributes			update class id name key
	Destroy	        Destroy specified object			destroy class
	Count		Retrieve the number of instances of a class	class.count


		Getting Started

	.These instructions will get you a copy of the project up and running on your 
	local machine (Linux distro) for development and testing purposes.

		Installing

	.You will need to clone the repository of the project from Github. 
	This will contain the simple shell program and all of its dependencies.

	git clone https://github.com/manodhiambo/AirBnB_clone.git
	After cloning the repository you will have a folder called AirBnB_clone. 
	In here there will be several files that allow the program to work.

	/console.py : The main executable of the project, the command interpreter.

	models/engine/file_storage.py: Class that serializes instances to a JSON file and 
	deserializes JSON file to instances

	models/__ init __.py: A unique FileStorage instance for the application

	models/base_model.py: Class that defines all common attributes/methods for other classes.

	models/user.py: User class that inherits from BaseModel

	models/state.py: State class that inherits from BaseModel

	models/city.py: City class that inherits from BaseModel

	models/amenity.py: Amenity class that inherits from BaseModel

	models/place.py: Place class that inherits from BaseModel

	models/review.py: Review class that inherits from BaseModel

	In the tests folders, several test files can be found which serve as unit-tests 
	for the console.

		Testing

	The program runs on Python3 which is an interpreted language, 
	so it needs no compilation of any kind.

		Usage of command interpreter
	Interactive Mode:

	Run program and show prompt with help command.
	PROMPT~> ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb)
	(hbnb) help quit
	Quit command to exit the program

	(hbnb)
	(hbnb)
	(hbnb) quit
	PROMPT~>

	non-interactive mode:
	Run the program passing argumments with pipes

	PROMPT~> echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	PROMPT~>
	PROMPT~> cat test_help
	help
	PROMPT~>
	PROMPT~> cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	PROMPT~>
