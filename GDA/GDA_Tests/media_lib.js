//media lib tests


qgoproapp.showTestMessage("Playback Frame Testing ...starting...");
var pf=0
pf+=frametest("/Users/keithfisher/Pictures/GDATest/GDATestVideosForAutomation/a1-4.mp4");
pf+=frametest("/Users/keithfisher/Pictures/GDATest/GDATestVideosForAutomation/b5-8.mp4");
pf+=frametest("/Users/keithfisher/Pictures/GDATest/GDATestVideosForAutomation/c9-12.mp4");
pf+=frametest("/Users/keithfisher/Pictures/GDATest/GDATestVideosForAutomation/d13-16.mp4");
$('main-content main-content--with-sidebar main-content-wrapper thumbnail-grid-container GoProUIMediaGrid2 GoProUIMediaThumbnail').index($('span.current')[0]);
$('div.GoProUIMediaGrid2').each(function(i) {
	if($(this).hasClass('GoProUIMediaThumbnail')){
		div.GoProUIMediaGrid2.click(this);
	}}
);
$.each($('div.GoProUIMediaGrid2')[0].childNodes,function(i,val){
	if($(val).hasClass('GoProUIMediaThumbnail')){
		sout=i;
		sout+='-'+val.id
		
		console.log(sout);
	}
	else{
		//console.log('Not found');
	}
});return nil
$.each($('div.GoProUIMediaGrid2')[0].childNodes,function(i,val){
	if($(val).hasClass('GoProUIMediaThumbnail') && !($(val).hasClass('GoProUIMediaSectionTitle'))){
		sout=i;
		//sout+='-'+val.figure.figcaption
		console.log(val.figure);
	}
	else{
		//console.log('Not found');
	}
})

$.each($('div.GoProUIMediaGrid2')[0].childNodes,function(i,val){
	if($(val).hasClass("GoProUIMediaThumbnail")){
		sout=i;
		//sout+='-'+ $(val).figure
		console.log(val);
	}
});console.log("--------------");


#if(pf<1){qgoproapp.quitApp();}

function selectmedia

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
	if(numDrops < 10){return 0;}else{return 1}
}
