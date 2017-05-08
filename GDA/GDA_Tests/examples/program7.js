// This program is executed in once batch
var thumbnails = $(".GoProUIMediaThumbnail img");
thumbnails.each(function( index ) {
    var fullPath = $( this ).attr("src");
    var fileName = fullPath.replace(/^.*[\\\/]/, '');
    qgoproapp.showTestMessage("Media Thumbnail " + index.toString() + " " + fileName);
});


