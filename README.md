# priscillafy

priscillafy makes creating, setting up, and working on projects of any programming language or framework really easy. It's a useful command line utility for Mac OS written in Python that initializes project structure, generates code files, and runs tasks. Different project templates can be installed allowing priscillafy to adapt to and automate to any type of project.

The idea came in preparation for a hackathon on how to be more efficient. I originally wrote the tool and shared it with my awesome friend, Priscilla (Github: @priscillalam) so she could easily deploy static websites. 

### Prerequisites

Install brew, git, and npm if not already. You can install brew by going to http://brew.sh and following the instructions there. 

Install Git and Node by opening up Terminal (Applicatons -> Utilities) and run `brew install git npm`. It should install the ncessary depenencies.

### Installing

1. Download the zip from Github and extract it. 
2. Open Terminal
3. Drag and drop "install.sh" into the window
4. Press enter.

### Getting Project Templates

Project templates can either be installed manually by downloading the project template folder (which ends in a .project) and placing it in the priscillafy folder in your home directory or through the priscillafy tool.

You can install templates with priscillafy itself by running `priscillafy install <github url of template>`.

When installing project templates, it is important to read the documentation for the template and what it offers.

##### Example

Inside Terminal type `priscillafy install https://github.com/priscillafy/website.project.git` and press enter. This will install the `website` project template for priscillafy.

### Creating Projects

You can create a priscillafy project in the current folder by running `priscillafy project <project template name> <options (optional)>` in Terminal.

##### Example (continued)
In Terminal, run `cd ~/Documents`.

Make a new folder for the project by running `mkdir sample-project`. Navigate into the folder with `cd sample-project`. We will create a new website project in that folder by typing `priscillafy project website` and pressing enter.

### Creating files in projects

You can generate files with types that are provided by the project template by running `priscillafy create <file type> <file name> <options (optional)>`.

You can also delete code files/undo changes by typing `priscillafy delete <file type> <file name> <options (optional)>` inside the project folder. 

Some types of files will contain boilerplate code from the template. This makes coding much easier and saves repetitive typing of code that is common in each type of follow.

##### Example (continued)

Each project template offers different types of files. The `website` template includes three file types: `page`, `style`, and `script`. Let's create a `page` file by running `priscillafy create page index`. Here we just created a new page called `index`. For the `website` template, the page files get created in `public/html`. If you open `index.html` you will see that there is some common HTML already there which saves time and effort.

### Running Project Tasks

Each project template offers certain tasks you can run for your project. You can run those tasks provided by typing `priscillafy run <task name> <options (optional)>`.

##### Example (continued)
 The `website` template, for example, has a `start` task that lets you start up the web server to view your new website. Type `priscillafy run start` and press enter. Go to `localhost:3000` in your browser to view your website!

### Updating and Removing Project Templates ###

To update your project template run `priscillafy update <project type>`. 

To uninstall a project template run `priscillafy uninstall <project type>`.

### Creating Project Templates (Advanced)

Project templates are written in Python. priscillafy offers the following API/functions that are available globaly:

`delete_file(file_path)` - deletes a file relative to the project directory.

`copy_asset(asset_name, destination)` - copies a file located in the asset directory of the template to a destination which is relative to the project directory.

`read_asset(asset_name)` - reads the contents of a file located in the asset directory and returns the string of its contents.

`run_shell(command)` - runs a shell command

`create_file(contents, file_name)` - creates a file with contents at the file name relative to the project directory.

`create_directory(directory_name)` - creates a directory inside the project directory

`load_template(template_name, args)` - reads a file template from the templates folder with the arguments provide as a dictionary.

There is a global array called `arguments` which are the arguments passed to a priscillafy command.

**Instructions**

1. Create a new folder with the ending `.project`, place it under git version control by typing `git init`, and `cd` into it.
2. Create a new file called init.py, do project structure setup there. This is run durning `priscillafy project <project name>`. The project name will be in `arguments[0]` and any other options would follow after that.
3. Create folders named `assets`, `creators`, `templates`, and `tasks`
4. For each static asset you will need to reference in your project template put them in `assets`.
5. For each file type, make a new file called <file type>.py inside creators. Create two functions in the file, `default` and `undo`. `default` is run during `priscillafy create`, `undo` is run for `priscillafy delete`.
6. Create the file with its contents inside `default()`, and delete the file in `undo()`. The filename passed in by the user is in `arguments[0]`, subsequent elements in `arguments` are options passed in by the user.
7. You can create file templates that can be populated with dynamic data and place them inside `templates`.  `load_template` takes in a template name and a dictionary. The dictionary's key and value should be both of type string. In each template you can use `%(key)s` anywhere to replace it with the `value` specified in the dictionary. You will need to escape `%` signs with `\%` if you do not wish to have it interpolated.
9. You can create tasks in the `task` folder. Name your file `<taskname>.py` and the file will be run when `priscillafy run <taskname>` is called. `arguments` contain the options and parameters passed in by the user.
10. To share your template, push it up to a public git repository. That way your template can be installed with `priscillafy install`.

A sample project template can be found in `github.com/priscillafy/website.project`.
