qgoproapp.showTestMessage("Testing ... starting...");
safeQuery(".GoProUILoginBypass").trigger("click"); // Switch to Media Browser
var thumbnails = $(".GoProUIMediaThumbnail");
if(thumbnails.length == 0) {qgoproapp.setTestResult(false, "", "No media"); qgoproapp.quitApp();}
$(thumbnails[0]).contextmenu();
safeQuery(".GoProJSMenuView").trigger("click");
qgoproapp.waitTest(5000); // Wait 5 seconds
safeQuery(".GoProUIPlayerBackButton").trigger("click"); // Back to Media Browser
#qgoproapp.quitApp();
