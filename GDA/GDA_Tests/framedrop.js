//Frame drop tests


qgoproapp.showTestMessage("Playback Frame Testing ...starting...");
var pf=0
pf+=frametest("/Users/keithfisher/Pictures/GDATest/GDATestVideosForAutomation/a1-4.mp4");
pf+=frametest("/Users/keithfisher/Pictures/GDATest/GDATestVideosForAutomation/b5-8.mp4");
pf+=frametest("/Users/keithfisher/Pictures/GDATest/GDATestVideosForAutomation/c9-12.mp4");
pf+=frametest("/Users/keithfisher/Pictures/GDATest/GDATestVideosForAutomation/d13-16.mp4");

<<<<<<< HEAD
#if(pf<1){qgoproapp.quitApp();}
=======
>>>>>>> Quik-2.2-dev

function frametest(path){
	qgoproapp.showTestMessage("starting..."+path);
	qgoproapp.setTestMediaSourceFile(path);
	safeQuery(".GoProUIPlayerSourceButton").trigger("click");
	var numDrops = GoProEditPlayer.getNumDroppedFrames();
	safeQuery(".GoProUIPlayerPlayButton").trigger("click"); //Play
	qgoproapp.waitTest(20000); // Wait 20 seconds
	safeQuery(".GoProUIPlayerPlayButton").trigger("click"); //Stop
	qgoproapp.showTestMessage("Playback Testing ... analysingresults...");
	numDrops = GoProEditPlayer.getNumDroppedFrames() -numDrops;
	qgoproapp.testResult(numDrops < 10, "PASSED: Dropped frames = " +
	numDrops.toString() + " < 10", "FAILED: Dropped frames = " +
	numDrops.toString());
	safeQuery(".GoProUIPlayerBackButton").trigger("click"); //Go to Media Library
<<<<<<< HEAD
	if(numDrops < 10){return 0;}else{return 1}
=======

>>>>>>> Quik-2.2-dev
}
