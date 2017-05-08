/**
 * Created by keithfisher on 12/29/15.
 */

/*

 Install (no previous version) and Launch
 C1036380	First Play window : Auto Launch


 Prerequisites
 Windows:

 Latest .exe of GoPro for desktop
 Purge all files from C:\Users(username)\AppData\Local\GoPro
 Task Manager open - End Task for GoPro Detection and GoPro System Tray
 This PC\system\program files\GoPro\GoPro Desktop App
 Make sure to click under view - Show Hidden Files
 Mac

 Delete GoPro and GoPro Studio from your Applications Folder.
 Delete the "GoPro" folder from macHD/Users/[your user]/Pictures/
 Delete all "com.gopro.xxx" files from macHD/Users/[your user]/library/preferences
 Delete all "com.gopro.xxx" folders from macHD/Users/[your user]/library/Application Support
 Open Terminal and type the following command: killall cfprefsd
 Press enter.
 Empty Trash.
 Steps
 Windows:

 Open the OS Task Manager tot he processes tab.

 Verify that there are no GoPro processes running in Task Manager.
 Run installer to completeness with Task Manager open.

 Verify that after is finished, two process are running: "GoProDesktopSystemTray" and "GoProDeviceDetection".
 Launch The GoPro App via shortcut.

 Verify that the GoPro App window opens.
 Launch GoPro Studio via shortcut.

 Verify that GoPro Studio opens.
 Close both apps.

 Verify both close without crashing
 Mac

 Open Activity Monitor from Applications/Utilities/ and type GoPro in the search box.

 Verify that there are no GoPro processes running in Task Manager.
 Run installer to completion with Task Manager open.

 Verify that after is finished, One process should be running. goproapp.devicedetection.
 Launch The GoPro App via Applications.

 Verify that the GoPro App window opens.
 Launch GoPro Studio via shortcut.

 Verify that GoPro Studio opens.
 Close both apps.

 Verify both close without crashing
 Expected Result
 No crash or hang
 Installation completes without errors
 Program launches successfully


Prerequisites
GDA installed
Hero PTP Cam (edition non-specific) w/ recorded GoPro media
USB transfer cable
Steps
Launch GDA.

    Verify that the First Play window opens.
    Verify that the "Automatically launch GoPro when I connect my camera" checkbox is checked by default.

Click the Continue button.

    Verify that you are taken to the CREATE ACCOUNT window.
    Close the CREATE ACCOUNT window. Plug In and Power On a camera.

    Verify that the App reopens on camera Plug In.
    Expected Result
No crash or hang
Camera goes into PTP mode when connected
GDA launches when camera is connected on First Play
*/