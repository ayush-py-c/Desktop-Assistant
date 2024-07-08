import datetime
import winsound


def alarm(timing):

    alarm_time = str(datetime.datetime.now().strptime(timing, "%I:%M %p"))
    alarm_time = alarm_time[11:-3]
    print(alarm_time)
    Horeal = alarm_time[:2]
    Horeal = int(Horeal)
    Mireal = alarm_time[3:5]
    Mireal = int(Mireal)
    print(f"Done, alarm is set for {timing}")


    while True:
        if Horeal == datetime.datetime.now().hour:
            if Mireal == datetime.datetime.now().minute:
                print('Alarm is running')
                winsound.PlaySound('abc',winsound.SND_LOOP)

            elif Mireal<datetime.datetime.now().minute:
                break

if __name__ == "__main__":
    alarm("9:00 PM")
