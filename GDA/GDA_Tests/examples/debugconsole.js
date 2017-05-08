/**
 * Created by keithfisher on 1/17/17.
 */


/** NOTES
 *
 *
 *
 *
 *
 *
 *
 * @param _msg
 */



function showit(_msg){qgoproapp.showTestMessage(_msg);}
function getinfo(_elem,_info){var txt = $(_elem).attr(_info);showit("BUTTON..."+txt);return txt};
function loadmp4(_file){showit("Load..."+_file);qgoproapp.setTestMediaSourceFile(_file);};
function showattributes(_this){var rc="";$(_this).each(function() {$.each(this.attributes, function() {if(this.specified) {console.log(this.name, this.value);rc+=this.name+"="+ this.value+"|\n";}});});showit(rc);return rc;}


function resethilites(){
    $.each($('div.GoProUIMediaGrid2')[0].childNodes,function(i,val){
        if($(val).hasClass("GoProUIMediaThumbnail")){
            $(".thumbnail").css( "border", "");
            $(val).css( "border", "");
            $(".thumbnail-duration").css( "border", "");
            $(".thumbnail--icon-mediatype").css( "border", "");
            $(".GoProUIMediaThumbnail").css( "border", "");
        }
    });
}

function init(qgoproapp){
    var quikinfo={};
    qgoproapp.logMessage("============== automation init==================");
    console.log("============== automation init==================");

    qgoproapp.windowTitle="Quik AUTOMATION";
    quikinfo["wintitle"]="Quik AUTOMATION";

    quikinfo["Ver"]=qgoproapp.getAppVersion();
    qgoproapp.logMessage("Ver:"+quikinfo["Ver"]);
    console.log("Ver:"+quikinfo["Ver"]);

    quikinfo["AnalyticsGUID"]=qgoproapp.getAnalyticSessionID();
    console.log("AnalyticsGUID:"+quikinfo["AnalyticsGUID"]);
    qgoproapp.logMessage("AnalyticsGUID:"+quikinfo["AnalyticsGUID"]);

    quikinfo["SettingsOffloadFolder"]=qgoproapp.getSettingsOffloadFolder();
    console.log("SettingsOffloadFolder:"+quikinfo["SettingsOffloadFolder"]);
    qgoproapp.logMessage("SettingsOffloadFolder:"+quikinfo["SettingsOffloadFolder"]);

    quikinfo["isNetworkAvailable"]=qgoproapp.isNetworkAvailable();
    console.log("isNetworkAvailable:"+quikinfo["isNetworkAvailable"]);
    qgoproapp.logMessage("isNetworkAvailable:"+quikinfo["isNetworkAvailable"]);

    quikinfo["isOnline"]=qgoproapp.isOnline();
    console.log("isOnline:"+quikinfo["isOnline"]);
    qgoproapp.logMessage("isOnline:"+quikinfo["isOnline"]);
    //alert("test alert");
    qgoproapp.setEnabled(true);
    qgoproapp.setFocus();
    return quikinfo;
}


var quikinfo=init(qgoproapp);
console.log(quikinfo);

$.each($('div.GoProUIMediaGrid2')[0].childNodes,function(i,val){
    if($(val).hasClass("GoProUIMediaThumbnail")){
        $(".thumbnail").css( "border", "");
        $(val).css( "border", "");
        $(".thumbnail-duration").css( "border", "");
        $(".thumbnail--icon-mediatype").css( "border", "");
        $(".GoProUIMediaThumbnail").css( "border", "");
    }
});

var scanmedia=[];$.each($('div.GoProUIMediaGrid2')[0].childNodes,function(i,val){
    if($(val).hasClass("GoProUIMediaThumbnail")){
        //console.log('pos:'+$(val).position());
        //console.log('W:'+$(val).width());
        //console.log('H:'+$(val).height());
        //console.log($(val).$(.thumbnail-duration).text());
        $(".thumbnail").css( "border", "1px solid red");
        $(val).css( "border", "1px solid green");
        $(".thumbnail-duration").css( "border", "1px solid red");
        $(".thumbnail").css( "border", "1px solid red");
        $(".thumbnail--icon-mediatype").css( "border", "1px solid red");
        console.log($(".thumbnail--icon-mediatype").html());

        //console.log($(".thumbnail-duration").html());
        //console.log($(".thumbnail--icon-hilight").html());
        $(".GoProUIMediaThumbnail").css( "border", "1px solid green");
        //console.log($(val).html());
        //$(val).trigger("click");
        //var iit = {"duration":$(val).$("thumbnail-duration").html()};
        //scanmedia.push({"duration":$(".thumbnail-duration").html()});
        console.log(val);

    }
});console.log("--------------");
