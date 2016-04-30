#!/usr/bin/python
import sys, os, os.path, argparse
from os.path import expanduser
from shutil import copyfile

### Project Template Methods ###

def delete_file(file_name):
    os.remove(file_name)

def copy_asset(asset_name, destination):
    project_name = get_project_name()
    if not project_name:
        return
    asset_path = get_asset_path(asset_name)
    copyfile(asset_path, get_current_directory() + destination + asset_name)

def read_asset(asset_name):
    asset_path = get_asset_path(asset_name)
    asset_file = open(asset_path, "r")
    asset = asset_file.read()
    asset_file.close()
    return asset

def run_shell(command):
    os.system(command)

def create_file(contents, file_name):
    new_file = open(file_name, "w")
    new_file.write(contents)
    new_file.close()

def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

def load_template(template_name, args):
    template_path = get_project_templates_directory() + get_project_name() + ".project/templates/" + template_name
    template = open(template_path, "r")
    template_contents = eval('"""' + template.read() + '"""') % args
    template.close()
    return template_contents

### Private Helper Methods ###

def get_asset_path(asset_name):
    return  get_project_templates_directory() + get_project_name() + ".project/assets/" + asset_name

def get_current_directory():
    return os.getcwd() + "/"

def get_project_name():
    config_path = get_current_directory() + ".priscillafy"
    if not os.path.isfile(config_path):
        print("Error: No project in this directory")
        return None
    config = open(config_path, "r")
    project_name = config.read()
    config.close()
    return project_name

def get_project_templates_directory():
    return expanduser("~") + "/priscillafy/"

### Commands ###

def create(args):
    if len(args) == 0:
        print("priscillafy create <file type>")
    else:
        creator_name = args[0]
        project_name = get_project_name()
        if not project_name:
            return
        creator_path = get_project_templates_directory() + project_name + ".project/creators/" + creator_name + ".py"
        global arguments
        arguments = args[1:]
        if os.path.isfile(creator_path):
            execfile(creator_path, globals())
            default()
        else:
            print("Error: File type does not exist.")

def delete(args):
    if len(args) == 0:
        print("priscillafy delete <file type>")
    else:
        creator_name = args[0]
        project_name = get_project_name()
        if not project_name:
            return
        creator_path = get_project_templates_directory() + project_name + ".project/creators/" + creator_name + ".py"
        global arguments
        arguments = args[1:]
        if os.path.isfile(creator_path):
            execfile(creator_path, globals())
            undo()
        else:
            print("Error: File type does not exist.")

def project(args):
    if len(args) == 0:
        print("priscillafy project <project type>")
    else:
        name = args[0]
        config = open(get_current_directory() + ".priscillafy", "w")
        config.write(name)
        config.close()
        project_path = get_project_templates_directory() + name + ".project/"
        global arguments
        arguments = args[1:]
        if os.path.exists(project_path):
            execfile(project_path + "init.py")
        else:
            print("Error: Project type does not exist.")

def run(args):
    if len(args) == 0:
        print("priscillafy run <task name>")
    else:
        task_name = args[0]
        project_name = get_project_name()
        if not project_name:
            return
        task_path = get_project_templates_directory() + project_name + ".project/tasks/" + task_name + ".py"
        global arguments
        arguments = args[1:]
        if os.path.isfile(task_path):
            execfile(task_path)
        else:
            print("Error: Task does not exist.")

def install(args):
    if len(args) == 0:
        print("priscillafy install <project template git url>")
    else:
        repo_url = args[0]
        run_shell("cd " + get_project_templates_directory() + " && git clone " + repo_url)

def update(args):
    if len(args) == 0:
        print("priscillafy update <project type>")
    else:
        project_name = args[0]
        run_shell("cd " + get_project_templates_directory() + project_name + ".project && git pull")

def uninstall(args):
    if len(args) == 0:
        print("priscillafy uninstall <project type>")
    else:
        project_name = args[0]
        run_shell("rm -rf " + get_project_templates_directory() + project_name + ".project")

### Command Line Logic ###

def usage():
    print("priscillafy <project|create|delete|run|install|update|delete>")

def main(argv):
    if len(argv) < 1:
        usage()
        sys.exit(2)
    command = argv[0]
    if command == "project":
        project(argv[1:])
    elif command == "create":
        create(argv[1:])
    elif command == "delete":
        delete(argv[1:])
    elif command == "run":
        run(argv[1:])
    elif command == "install":
        install(argv[1:])
    elif command == "uninstall":
        uninstall(argv[1:])
    elif command == "update":
        update(argv[1:])

if __name__ == "__main__":
    main(sys.argv[1:])
