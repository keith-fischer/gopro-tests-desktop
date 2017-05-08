function dowait(_wait){qgoproapp.waitTest(_wait);}
function showit(_msg){qgoproapp.showTestMessage(_msg);}
function getinfo(_elem,_info){var txt = $(_elem).attr(_info);showit("BUTTON..."+txt);return txt};
function loadmp4(_file){showit("Load..."+_file);qgoproapp.setTestMediaSourceFile(_file);};

function showattributesx(_this){var rc="";$(_this).each(function() {$.each(_this.attributes, function() {if(_this.specified) {console.log(_this.name, _this.value);rc+=_this.name+"="+ _this.value+"|\n";}});});showit(rc);return rc;}
function showattributes(_this){var rc="";$(_this).each(function() {$.each(this.attributes, function() {if(this.specified) {console.log(this.name, this.value);rc+=this.name+"="+ this.value+"|\n";}});});showit(rc);return rc;}


var rc = getinfo(".GoProUIPlayerPlayButton","id");
showit(rc);
var _this = $("."+rc);

var attt = showattributes(_this);


dowait(30000);
qgoproapp.showTestMessage("Playback Frame Testing ... starting...");
loadmp4("/Automation/gda/imports/LemonsHD.mp4");
safeQuery(".GoProUIPlayerSourceButton").trigger("click");
var numDrops = GoProEditPlayer.getNumDroppedFrames();
var txt = safeQuery(".GoProUIPlayerPlayButton").attr("text");
qgoproapp.showTestMessage("BUTTON..."+txt);
//safeQuery(".GoProUIPlayerPlayButton").trigger("click"); // Play
txt = safeQuery(".GoProUIPlayerPlayButton").attr("text");
qgoproapp.showTestMessage("BUTTON..."+txt);
dowait(20000); // Wait 20 seconds
txt = safeQuery(".GoProUIPlayerPlayButton").attr("value");
qgoproapp.showTestMessage("BUTTON..."+txt);
safeQuery(".GoProUIPlayerPlayButton").trigger("click"); // Stop
txt = safeQuery(".GoProUIPlayerPlayButton").attr("value");
qgoproapp.showTestMessage("BUTTON..."+txt);
qgoproapp.showTestMessage("Playback Testing ... analysing results...");
numDrops = GoProEditPlayer.getNumDroppedFrames() - numDrops;
qgoproapp.testResult(numDrops < 10, "Dropped frames = " + numDrops.toString() + " < 10", "Dropped frames = " + numDrops.toString());
//safeQuery(".GoProUIPlayerBackButton").trigger("click"); // Go to Media Library
//qgoproapp.waitTest(20000); // Wait 20 seconds

//qgoproapp.quitApp();

// qgoproapp.executeTestProgram("/Automation/gda/GDATests/maximize.js");
// qgoproapp.executeTestProgram("/Automation/gda/GDATests/example1.js");
// qgoproapp.executeTestProgram("/Automation/gda/GDATests/example2.js");
// qgoproapp.executeTestProgram("/Automation/gda/GDATests/example3.js");
// qgoproapp.executeTestProgram("/Automation/gda/GDATests/example4.js");
// qgoproapp.executeTestProgram("/Automation/gda/GDATests/example5.js");
// qgoproapp.executeTestProgram("/Automation/gda/GDATests/example6.js");
// qgoproapp.executeTestProgram("/Automation/gda/GDATests/example7.js");
// qgoproapp.executeTestProgram("/Automation/gda/GDATests/example8.js");
