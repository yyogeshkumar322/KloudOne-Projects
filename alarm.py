import time
import winsound
def myAlarm():
    try:
          Time=list(map(int,input('enter the time in the format HR:MIN:SEC:').split(':')))
          if len(Time)==3:
              total_Time= Time[0]*60*60+Time[1]*60+Time[2]
              time.sleep(total_Time)
              frequency=2500
              duration=1500
              winsound.Beep(frequency ,duration )
          else:
             print('please write the correct format as mentioned EX:00:00:01 i.e:1 SEC \n')
             myAlarm()
    except Exception as e:
        print('this is the exception',e,'please enter correct details')
        myAlarm()
myAlarm()
