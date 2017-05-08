qgoproapp.showTestMessage("Testing ... starting...");
safeQuery(".GoProUILoginBypass").trigger("click"); // Switch to Media Browser
var thumbnails = $(".GoProUIMediaThumbnail");
if(thumbnails.length == 0) {qgoproapp.setTestResult(false, "", "No media"); qgoproapp.quitApp();}
var thumbnail_index = 0;
thumbnail_start:
$(thumbnails[thumbnail_index]).contextmenu();
safeQuery(".GoProJSMenuAutoComp").trigger("click");
safeQuery("#AutoCompProcess").trigger("click");
qgoproapp.waitTest(1000); // Wait 1 seconds
safeQuery(".GoProUIAutoCompBackButton").trigger("click"); // Back to Media Browser
thumbnail_index++;
if(thumbnail_index<thumbnails.length) qgoproapp.gotoTestLabel("thumbnail_start");
#qgoproapp.quitApp();



