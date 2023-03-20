Start = 0
Time = 0

def on_logo_touched():
    global Start
    Start = input.running_time()
    basic.show_icon(IconNames.HAPPY)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_logo_released():
    global Time
    Time = input.running_time() - Start
    basic.show_number(Time)
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)
