mode con width=120
mode con lines=9999
set userpath="C:\Users\%USERNAME%"
::cd userpath
set jenkins=C:\Automation\gopro-tests-desktop
::set gdapath="%userpath%\workspace\Win_GDA-Studio_3a_BAT\gopro-tests-desktop\GDA"
set gdapath="%jenkins%\GDA"
cd %gdapath%
GDASetAppWindow.exe
::installerversioncleanup64.exe

::GDAinstaller64.exe
::%SIKULI_HOME%
cd C:\Automation\gopro-tests-desktop\GDA\sikuli\gda_music_tests.sikuli
java -jar "C:\Program Files (x86)\sikuli\sikulix.jar" -r C:\Automation\gopro-tests-desktop\GDA\sikuli\gda.sikuli --args gda_music_tests-capture
::java -jar "C:\Program Files (x86)\sikuli\sikulix.jar" -r C:\Automation\gopro-tests-desktop\GDA\sikuli\gda.sikuli --args gda_music_tests-regression
::java -jar "C:\Program Files (x86)\sikuli\sikulix.jar" -r C:\Automation\gopro-tests-desktop\GDA\sikuli\gda.sikuli --args gda_view_tests

::java -Djava.awt.headless=false -jar "C:\Program Files (x86)\sikuli\runsikulix.cmd" -r "%gdapath%\gda\"

::START /DC:\Sikulix /WAIT /B "C:\Program Files (x86)\sikuli\runsikulix.cmd" -d 3 -r "%gdapath%\gda\sikuli\gda.sikuli" -f "%userpath%\workspace\log.txt" -d "%userpath%\workspace\userlog.txt"
::java -jar %SIKULI_HOME%\sikuli-script.jar path-to-your-script\yourScript.sikuli
pause