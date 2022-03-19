from datetime import datetime 
from flask import jsonify 
import pytz
"""time = [
        ['9:30AM','10:15AM'],
        ['10:15AM','11:00AM'],
        ['11:15AM','11:45AM'],
        ['11:45AM','12:30pm'],     
      ]"""
s8_timetable = {
  1 : ["ES" , "CC" ,"NDE" , "PROJECT", "PROJECT", "PROJECT" ],
  2 : ["DMW" , "CC" ,"ES" , "PROJECT", "PROJECT", "PROJECT" ],
  3 : ["CC", "NDE", "DMW","PROJECT", "PROJECT", "PROJECT"],
  4 : ["PROJECT", "PROJECT", "PROJECT" , "PROJECT", "PROJECT", "PROJECT" ],
  5 : ["NDE" , "ES" ,"DMW" , "PROJECT", "PROJECT", "PROJECT" ],
}
def getIST():
  tz_NY = pytz.timezone('Asia/Kolkata')  
  #datetime_NY.strftime("%I:%M%p")) 
  return datetime.now(tz_NY) 
def getSubIndex():
  now = datetime.strptime(getIST().strftime("%I:%M%p"),"%I:%M%p")
  if now < datetime.strptime("08:30AM","%I:%M%p"):
    return 0
  elif now < datetime.strptime("09:30AM","%I:%M%p"):
    return 1
  elif now < datetime.strptime("10:30AM","%I:%M%p"):
    return 2
  elif now < datetime.strptime("01:30PM","%I:%M%p"):
    return 3
  elif now < datetime.strptime("02:30PM","%I:%M%p"):
    return 4
  elif now < datetime.strptime("03:30PM","%I:%M%p"):
    return 5
  else:
    return -1 
  
def getSUB(day,index):
    return s8_timetable[day][index]

def main(request):
    day = getIST().isoweekday()
    if day > 5:
      day = 1
      current_index = 0
    current_index = int(getSubIndex())
    if current_index < 0 :
        day = (day%5)+1
        current_index = 0
    current = getSUB(day,current_index )
    print(current_index,current , day)
    next_sub = getSUB(day,current_index + 1) if current_index < 5  else getSUB((day%5)+1,0)
    next_next = getSUB(day , current_index + 2) if current_index < 4 else getSUB((day%5 )+1,1)
    json_data = {
      'current' : current,
      'next_sub' : next_sub,
      'next_next':next_next
    }
    return jsonify(json_data)