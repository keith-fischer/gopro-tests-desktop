qgoproapp.showTestMessage("Testing ... starting...");
safeQuery(".GoProUILoginBypass").trigger("click"); // Switch to Media Browser
var thumbnails = $(".GoProUIMediaThumbnail img");
if(thumbnails.length == 0) {qgoproapp.setTestResult(false, "", "No media"); qgoproapp.quitApp();}
$(thumbnails[0]).dblclick();
qgoproapp.waitTest(5000); // Wait 5 seconds
safeQuery(".GoProUIPlayerBackButton").trigger("click"); // Back to Media Browser
#qgoproapp.quitApp();


qgoproapp.showTestMessage("Testing ... starting...");
$(".GoProUILoginBypass").trigger("click"); // Switch to Media Browser
var thumbnails = $(".GoProUIMediaThumbnail img");
console.log(thumbnails);
//if(thumbnails.length == 0) {qgoproapp.setTestResult(false, "", "No media"); }//qgoproapp.quitApp();}
$(thumbnails[0]).dblclick();
qgoproapp.waitTest(5000); // Wait 5 seconds
$(".GoProUIPlayerBackButton").trigger("click"); // Back to Media Browser
//qgoproapp.quitApp();
