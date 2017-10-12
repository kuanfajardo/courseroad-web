from engine import run
from fancy_print import *
from copy import deepcopy
import json

allowed_courses = {"6-3", "2", "16", "10", "5"}

print_header("+--------------------------------+\n"
             "|        COURSEROAD MINI         |\n"
             "+--------------------------------+\n")

course = None
classes = set()

try:
    with open("course_road.json", "r") as file:
        obj = json.load(file)

        print_message(bold("Successfully loaded data from previous sessions."))

        course = obj["course"]
        classes = set(obj["classes"])

        load_success = True

except FileNotFoundError:
    load_success = False


if not load_success:
    while True:
        inp = input("Enter your course. Enter \"options\" to see supported courses: ")
        inp = inp.upper().strip()

        if inp.lower() == "options":
            for course in allowed_courses:
                print(course)

            print("")
            continue

        if inp not in allowed_courses:
            print_failure("Sorry, that course is not yet supported." + "\n")

        else:
            course = inp
            print_success("Registered as Course " + course)
            break


print_message("\n"
              "Welcome to CourseRoad Mini. Type \"help\" for more information.")

# MAIN RUN #
while True:
    inp = input(message(bold("\n>> ")))

    inp = inp.lower().strip()
    inp_arr = inp.split(" ")

    if inp_arr[0] == "help":
        if len(inp_arr) != 1:
            print_failure("Invalid usage of " + bold(message("help")))
            continue

        print_message("\n" + "list of available commands")

        help_menu = {
            "add [<classes>]": "Add class(es) to your list of classes",
            "remove [<classes> | --all]": "Remove class(es) from your list of classes",
            "classes": "See current list of classes",
            "road [--pre-reqs]": "See course road and satisfied/missing requirements",
            "course": "Edit course",
            "exit": "Exit application"
        }

        for key, value in help_menu.items():
            print("{0:2} {1:30} {2}".format("", key, value))

        continue

    if inp_arr[0] == "road":
        if len(inp_arr) >= 2:
            if len(inp_arr) == 2 and inp_arr[1] == "--pre-reqs":
                show_pre_reqs = True
            else:
                print_failure("Invalid usage of " + bold(message("road")))
                continue
        else:
            show_pre_reqs = False

        run(classes, course + ".req", show_pre_reqs=show_pre_reqs)
        continue

    if inp_arr[0] == "course":
        if len(inp_arr) != 1:
            print_failure("Invalid usage of " + bold(message("course")))
            continue

        print_message("** You currently are registered as Course " + course + " **" + "\n")
        inp = input("Enter a new course number, \"options\", or press enter to return to menu: ")

        while True:
            if inp == "":
                break

            if inp.lower() == "options":
                for course in allowed_courses:
                    print(course)

                print("")

            elif inp not in allowed_courses:
                print_failure("Sorry, that course is not yet supported.\n")

            else:
                course = inp
                print_success("Registered as Course " + course)
                break

            inp = input("Enter a new course number, \"options\", or press enter to return to menu: ")
        continue

    if inp_arr[0] == "classes":
        if len(inp_arr) != 1:
            print_failure("Invalid usage of " + bold(message("classes")))
            continue

        if len(classes) == 0:
            print("You have not added any classes yet.")
            continue

        for cls in classes:
            print(cls)
        continue

    if inp_arr[0] == "exit":
        if len(inp_arr) != 1:
            print_failure("Invalid usage of " + bold(message("exit")))
            continue

        break

    if inp_arr[0] == "add":
        for cls in set(inp_arr[1:]):
            arr = cls.split(".")

            if len(arr) != 2:
                print_failure(cls.upper() + " is not a valid class.")
                continue

            if cls.upper() not in classes:
                classes.add(cls.upper())
                print_success(cls.upper() + " added")
            else:
                print_failure(cls.upper() + " already added.")

        continue

    if inp_arr[0] == "remove":
        classes_to_remove = inp_arr[1:]

        if len(inp_arr) >= 2 and inp_arr[1] == "--all":
            if len(inp_arr) != 2:
                print_failure("Invalid usage of " + bold(message("remove")))
                continue

            classes_to_remove = deepcopy(classes)

        for cls in classes_to_remove:
            arr = cls.split(".")

            if len(arr) != 2:
                print_failure(cls.upper() + " is not a valid class.")
                continue

            if cls.upper() not in classes:
                print_failure(cls.upper() + " is not in your current classes.")
            else:
                classes.remove(cls.upper())
                print_success(cls.upper() + " removed")

        continue

    print_failure("\"" + inp + "\" is not a valid command. Please see help menu.")


content = {
    "course": str(course),
    "classes": list(classes)
}

with open("course_road.json", "w+") as file:
    json.dump(content, file)
    print_message(bold("Data successfully saved."))
