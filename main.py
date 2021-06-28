# This is a sample Python script.
import zivid
import cv2

from datetime import date, timedelta
from os import mkdir

if __name__ == '__main__':
    app = zivid.Application()
    camera = app.connect_camera()
    capture_assistant_params = zivid.capture_assistant.SuggestSettingsParameters(max_capture_time=timedelta(milliseconds=10000))
    settings = zivid.capture_assistant.suggest_settings(camera, capture_assistant_params)

    capture_number = 0
    position_number = 1
    folder = date.today().strftime("%Y%m%d")

    try:
        mkdir(f"./{folder}")
    except FileExistsError:
        print(f"File {folder} exists.")

    while True:
        inp_option = input("Enter input (type \"h\" for help): ")
        if inp_option == "q":
            exit(0)

        elif inp_option == "p":
            print(f"Position: {str(position_number)}\nCapture: {str(capture_number)}")

        elif inp_option == "s":
            try:
                capture_number = int(input("Capture number: "))
                position_number = int(input("Position number: "))
                print("Successfully changed.")
            except ValueError:
                print("Error parsing values, must be an integer.")
                print(f"Position set to {str(position_number)} and Capture set to {str(capture_number)}")

        elif inp_option == "c":
            frame = camera.capture(settings)
            # frame.save("./sample.zdf")
            pc = frame.point_cloud()
            rgba = pc.copy_data("rgba")
            bgr = cv2.cvtColor(rgba, cv2.COLOR_RGBA2BGR)
            cv2.imwrite(f"./{folder}/sample.png", bgr)

            confirm = input("Save data? (y/n): ")
            if confirm == "y":
                fileName = "position_" + str(position_number) + "capture_" + str(capture_number)
                frame.save(f"./{folder}/{fileName}.zdf")
                cv2.imwrite(f"./{folder}/{fileName}.png", bgr)

                position_change = input("Next position? (y/n): ")
                if position_change == "y":
                    capture_number = 0
                    position_number = position_number + 1

                elif position_change == "n":
                    capture_number = capture_number + 1

                print(f"Current position: {str(position_number)} and capture: {str(capture_number)}")

        elif inp_option == "h":
            print("c: Capture data.")
            print("p: Preview current position and capture.")
            print("s: Set position and capture.\n")
            print("q: Quit the application")

        else:
            print("Invalid input.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
