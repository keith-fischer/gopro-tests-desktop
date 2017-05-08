qgoproapp.showTestMessage("Playback Frame Testing ... starting...");
qgoproapp.setTestMediaSourceFile("/Users/sukendeepsamra/Desktop/Media/LemonsHD.mp4");
safeQuery(".GoProUIPlayerSourceButton").trigger("click");
var numDrops = GoProEditPlayer.getNumDroppedFrames();
safeQuery(".GoProUIPlayerPlayButton").trigger("click"); // Play
qgoproapp.pauseTest(GoProEditPlayer.GetNormalizedPlayheadLocation()<0.5);
safeQuery(".GoProUIPlayerPlayButton").trigger("click"); // Stop
qgoproapp.showTestMessage("Playback Testing ... analysing results...");
numDrops = GoProEditPlayer.getNumDroppedFrames() - numDrops;
qgoproapp.testResult(numDrops < 10, "Dropped frames = " + numDrops.toString() + " < 10", "Dropped frames = " + numDrops.toString());
safeQuery(".GoProUIPlayerBackButton").trigger("click"); // Go to Media Library
#qgoproapp.quitApp();



