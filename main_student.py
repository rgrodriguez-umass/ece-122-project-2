from course_management_student import CourseItem, Course, CourseManager, DEFAULT_WEIGHTS


def display_menu():
    print("\nCourse Management System")
    print("1.  Add a new course")
    print("2.  View all courses")
    print("3.  Add an item to a course")
    print("4.  View all items in a course")
    print("5.  Mark an item as completed")
    print("6.  Update an item's score")
    print("7.  View pending items")
    print("8.  Calculate course grade")
    print("9.  Customize category weights")
    print("10. Exit")


def prompt_course_code(manager):
    """
    Display all current courses, then prompt the user to enter a course code.

    Steps:
        1. Print a header: "Current courses:"
        2. Print each string returned by manager.display_courses(), indented with "  ".
        3. Prompt: "Enter course code: "
        4. Call manager.find_course_by_code() with the entered code.
        5. If not found, print "Course not found." and return None.
        6. Return the matching Course object.

    Parameters:
        manager (CourseManager): The active course manager.

    Returns:
        Course or None.
    """
    # TODO: Implement this helper following the steps above
    print("\nCurrent courses:")
    for course in manager.display_courses():
        print(course, end=" ")
    code = input("\nEnter course code:")
    if manager.find_course_by_code(code) != None:
        return manager.find_course_by_code(code)
    else:
        print("Course not found.")
        return None


def main():
    manager = CourseManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # TODO: Prompt for course name, course code, and instructor name
            # Create a Course object and add it to manager via manager.add_course()
            # Print "Course added successfully."
            course_name = input("Enter course name: ")
            course_code = input("Enter course code: ")
            instructor = input("Enter instructor: ")
            manager.add_course(course_name, course_code, instructor)
            print("Course added successfully.")

        elif choice == "2":
            # TODO: Print each string returned by manager.display_courses()
            courses = manager.display_courses()
            for course in courses:
                print(course)

        elif choice == "3":
            # TODO: Call prompt_course_code(manager) to get the course
            # If None, use 'continue' to go back to the menu
            # Otherwise, prompt for item title, category, due date, and points possible
            # Create a CourseItem and add it to the course via course.add_item()
            # Print "Item added successfully."
            if prompt_course_code(manager) == None:
                continue
            else:
                item_title = input("Enter course item title: ")
                course_category = input("Enter course category: ")
                due_date = input("Enter due date: ")
                possible_points = input("Enter possible points: ")
                CourseItem(item_title, course_category, due_date, possible_points)
                print("Item added successfully.")


        elif choice == "4":
            # TODO: Call prompt_course_code(manager) to get the course
            # If None, use 'continue'
            # Otherwise, print each string returned by course.display_items()
            if prompt_course_code(manager) == None:
                continue
            else:
                for item in course.display_items():
                    print(item)

        elif choice == "5":
            # TODO: Call prompt_course_code(manager) to get the course
            # If None, use 'continue'
            # Prompt for item title, call course.find_item()
            # If None, print "Item not found."
            # Otherwise, call item.mark_complete() and print "Item marked as completed."
            if prompt_course_code(manager) == None:
                continue
            else:
                item_title = input("Enter course item title: ")
                if course.find_item(item_title) == None:
                    print("Item not found.")
                else:
                    item.mark_complete()
                    print("Item marked as completed.")

        elif choice == "6":
            # TODO: Call prompt_course_code(manager) to get the course
            # If None, use 'continue'
            # Prompt for item title, call course.find_item()
            # If None, print "Item not found."
            # Otherwise, prompt for score (float), call item.update_score()
            # Print "Score updated successfully."
            pass

        elif choice == "7":
            # TODO: Call prompt_course_code(manager) to get the course
            # If None, use 'continue'
            # Print each string returned by course.display_pending_items()
            pass

        elif choice == "8":
            # TODO: Call prompt_course_code(manager) to get the course
            # If None, use 'continue'
            # Call course.calculate_grade()
            # If None, print "No graded items yet."
            # Otherwise:
            #   Print "Course Grade for <course_code>: <course_name>"
            #   Print "  Weighted average : <percentage:.2f>%"
            #   Print "  Letter grade     : <letter>"
            #   Print a per-category breakdown (see project spec for format)
            pass

        elif choice == "9":
            # TODO: Call prompt_course_code(manager) to get the course
            # If None, use 'continue'
            # Print "Current weights for <course_code>:"
            # Print each string from course.display_weights()
            # Print instructions, then prompt the user for a new weight per category
            #   (pressing Enter keeps the current value)
            # Validate that the new weights sum to ~100
            # If valid, call course.set_weights() and print "Weights updated successfully."
            # If invalid, print "Weights must sum to 100 (got <total:.2f>). No changes made."
            pass

        elif choice == "10":
            # TODO: Print "Exiting program." and break out of the loop
            pass

        else:
            # TODO: Print "Invalid choice. Please try again."
            pass


if __name__ == "__main__":
    main()
