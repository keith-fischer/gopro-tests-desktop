qgoproapp.showTestMessage("Maximize Window Testing ... starting...");
qgoproapp.setTestMediaSourceFile("/Users/sukendeepsamra/Desktop/Media/LemonsHD.mp4");
safeQuery(".GoProUIPlayerSourceButton").trigger("click");
safeQuery(".GoProUIPlayerPlayButton").trigger("click"); // Play
qgoproapp.saveWindowPositionSettings();
qgoproapp.windowMaximize();
qgoproapp.restoreWindowPositionSettings();
qgoproapp.windowMaximize();
qgoproapp.restoreWindowPositionSettings();
qgoproapp.windowMaximize();
qgoproapp.restoreWindowPositionSettings();
safeQuery(".GoProUIPlayerPlayButton").trigger("click"); // Stop
safeQuery(".GoProUIPlayerBackButton").trigger("click"); // Go to Media Library
qgoproapp.windowMaximize();
qgoproapp.restoreWindowPositionSettings();
qgoproapp.windowMaximize();
qgoproapp.restoreWindowPositionSettings();
qgoproapp.windowMaximize();
qgoproapp.restoreWindowPositionSettings();
safeQuery(".GoProUILoginButton").trigger("click"); // Go to Login
qgoproapp.windowMaximize();
qgoproapp.restoreWindowPositionSettings();
qgoproapp.windowMaximize();
qgoproapp.restoreWindowPositionSettings();
qgoproapp.windowMaximize();
qgoproapp.restoreWindowPositionSettings();
qgoproapp.showTestMessage("Maximize Window Testing ... analysing results...");
qgoproapp.testResult(true, "not crashed", "");
//qgoproapp.quitApp();
