from app import file
from ImageDecoder import getData
from ImageDecoder import TimeBlock


class SharedBreaks:
  myName = None
  mySchedule = None
  friendsSchedules = None
  sharedBreaks = None
  def __init__(self, myName, mySchedule, friendsSchedules):
    self.myName = myName
    self.mySchedule = mySchedule
    self.friendsSchedules = friendsSchedules
    self.sharedBreaks = self.getSharedBreaks()
  def getSharedBreaks(self):
    allSharedBreaks = []
    for friend, friendSchedule in enumerate(self.friendsSchedules):
      sharedBreaks = []
      for theirTimeBlock in friendSchedule.availabilities:
        for myTimeBlock in self.mySchedule:
          sharedBreak = theirTimeBlock.sharedAvailability(myTimeBlock)
          if sharedBreak == None:
            continue
          else:
            sharedBreaks.append(sharedBreak)
      allSharedBreaks.append(sharedBreaks)
    return allSharedBreaks

class Schedule:
  name = None
  courses = None
  availabilities = None
  def __init__(self, name, courses):
    self.name = name
    self.courses = courses
    self.availabilities = self.getAvailableTimes()
  def getAvailableTimes(self):
    coursesByDay = [[],[],[],[],[]]
    availabilities = []
    coursesSorted = []
    #sorting courses by day
    for course in self.courses:
      coursesByDay[course.day].append(course)
    #generating availabilities day by day
    for dayIndex, coursesInADay in enumerate(coursesByDay):
      #if no classes in a day: unavailable that day
      if coursesInADay == []:
        continue
      #Sorting the courses by time
      coursesInADay.sort(key= lambda TimeBlock : TimeBlock.end)
      coursesSorted = coursesInADay
      #generating availabilities for one day
      if len(coursesSorted) == 1:
        availabilities.append(TimeBlock(dayIndex, coursesSorted[0].end, 1440))
      else:
        for i in range(len(coursesSorted)-1):
          availabilities.append(TimeBlock(dayIndex, coursesSorted[i].end, coursesSorted[i+1].start))
        availabilities.append(TimeBlock(dayIndex, coursesSorted[-1].end, 1440))
    return availabilities


def getSharedBreaks(mySchedule, friendSchedule):
  sharedBreaks = []
  for theirTimeBlock in friendSchedule.availabilities:
    for myTimeBlock in mySchedule.availabilities:
      sharedBreak = theirTimeBlock.sharedAvailability(myTimeBlock)
      if sharedBreak != None:
        sharedBreaks.append(sharedBreak)
  return sharedBreaks

imageNames = ["ScheduleSample1.png", "ScheduleSample3.png", "ScheduleSample4.png", "ScheduleSample7.png", "ScheduleSample8.png", "ScheduleSample4JPG.jpg"]
startingTimes = [705, 600, 525, 705, 705]

#For MY schedule: ------------------

myName = "Franco"                             #I need this
myScheduleImagePath = "ScheduleSample3.png"   #I need this
myStartTime = 525                               #and I need this
mySchedule = Schedule(myName, getData(myScheduleImagePath, myStartTime))
myCourses = mySchedule.courses
myCourses2DArray = []
for course in myCourses:
  myCourses2DArray.append([course.day, course.start, course.end])

#I will return you this:
print(myCourses2DArray)

#-----------------------------------

#For FRIEND schedule: --------------

friendName = "Ali"                                #I will need this
friendScheduleImagePath = file.filename   #This
friendStartTime = 600                             #and this
friendSchedule = Schedule(friendName, getData(friendScheduleImagePath, friendStartTime))
friendCourses = mySchedule.courses
friendCourses2DArray = []
sharedBreaks = getSharedBreaks(mySchedule, friendSchedule)
for sharedBreak in sharedBreaks:
  friendCourses2DArray.append([sharedBreak.day, sharedBreak.start, sharedBreak.end])

#I will return you this:
print(friendCourses2DArray)

#p----------------------------------




