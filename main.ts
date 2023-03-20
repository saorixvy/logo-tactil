let Start = 0
let Time = 0
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    Start = input.runningTime()
    basic.showIcon(IconNames.Ghost)
})
input.onLogoEvent(TouchButtonEvent.Released, function () {
    basic.clearScreen()
    Time = input.runningTime() - Start
    basic.showNumber(Time)
})
