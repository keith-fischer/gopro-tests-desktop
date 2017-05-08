qgoproapp.showTestMessage("Testing ... starting...");
safeQuery(".GoProUILoginBypass").trigger("click"); // Switch to Media Browser
safeQuery(".GoProUISettingsButton").trigger("click");
qgoproapp.setTestWatchFolder("/Users/sukendeepsamra/Desktop/Media/Time Lapse 2/Burst Image Sets/moving/bike1");
safeQuery("#userSetWatchFolderButton").trigger("click");
safeQuery(".backToMediaLibrary").trigger("click"); // Go to Media Library
#qgoproapp.quitApp();




