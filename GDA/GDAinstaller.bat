
set userpath="C:\Users\%USERNAME%"
::cd userpath
set jenkins="C:\Win_GDA-Studio_3a_BAT"
::set gdapath="%userpath%\workspace\Win_GDA-Studio_3a_BAT\gopro-tests-desktop\GDA"
set gdapath=%jenkins%\GDA"
%gdapath%\GDACleanup.exe

cd %gdapath%\GDAInstaller

C:\Python27\python.exe %gdapath%\GDAInstaller\gdainstaller.py
::installerversioncleanup64.exe
::cd %gdapath%
::GDAinstaller64.exe
::%SIKULI_HOME%
::cd %gdapath%\sikuli\gda.sikuli
::java -jar "C:\Program Files (x86)\sikuli\sikulix.jar" -r C:\Win_GDA-Studio_3a_BAT\GDA\sikuli\gda.sikuli
::java -Djava.awt.headless=false -jar "C:\Program Files (x86)\sikuli\runsikulix.cmd" -r "%gdapath%\gda\"

::START /DC:\Sikulix /WAIT /B "C:\Program Files (x86)\sikuli\runsikulix.cmd" -d 3 -r "%gdapath%\gda\sikuli\gda.sikuli" -f "%userpath%\workspace\log.txt" -d "%userpath%\workspace\userlog.txt"
::java -jar %SIKULI_HOME%\sikuli-script.jar path-to-your-script\yourScript.sikuli

::pause