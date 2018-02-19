import json

class Course(object):
    def __init__(self, year, section, spec):
        self.course_name = str(year) + section.lower() + spec[0].lower() #course name is composed of the year, the lower-case section identification letter, and the lower-case first specialization letter
        self.spec = spec
        self.pupils = []

    def __str__(self):
        return "-Course: %s\n-Specialization: %s\n" % (self.course_name, self.spec)

    def view_pupils(self):
        print("=== Course Members ===\n")
        for pupil in self.pupils:
            print(pupil)
        print("=== === === === ===\n\n")

        
class Pupil(object):
    def __init__(self, course, name, surname, dob):
        self.course = course #course attended by the pupil
        self.name = name
        self.surname = surname
        self.dob = dob #date of birth

    def __str__(self):
        return "-Name: %s\n-Surname: %s\n-Date of Birth: %s\n-Course: %s\n" % (self.name, self.surname, self.dob, self.course)

    
def main():
    with open("data.json", "r") as file:
        raw_data = json.load(file)
    file.close()

    course_objs = {} #dict that acts as a obj_name : obj map

    #split the JSON content into its 2 main sections (the first for the various courses, the second for the pupils pertaining to each course)
    courses = raw_data["Course"] 
    roster = raw_data["Pupils"]

    for course in courses:
        new_course = Course(**courses[course]) #create a new Course object which takes an unpacked inner dict from the JSON raw data as parameter for its constructor
        course_objs[new_course.course_name] = new_course #map obj name to obj reference

    for course in roster:
        for pupil in roster.get(course):
            new_pupil = Pupil(course, **pupil) #create a new pupil object
            course_objs[course].pupils.append(new_pupil) #add pupil to his respective course object's pupils list, utilizing the course name as parameter

    #print the representation of the created objects
    for course in list(course_objs.values()):
        print(course)
        course.view_pupils()
    

if __name__ == "__main__":
    main()
