/**
 * Created by keithfisher on 1/19/17.
 * Report all media items
 * 1. Set Filter All
 * 2. Iterate items top to bottom, left to right
 * 3. Report media type
 * 4. Report media duration
 * 5. Report import date
 * 6. Report Tagged and count
 * 7. Report thumbnail coordinate in container x,y,w,h
 * 8. Report Visible in container [true|false]
 */

var logverbose=true;
function LOG(label,printinfo){
    if(logverbose){
        console.log(label);
        console.log(printinfo);
        var sr=JSON.stringify(printinfo);
        console.log(label+sr);
        qgoproapp.logMessage(label+sr);
    }
}

function showit(_msg){qgoproapp.showTestMessage(_msg);}
function getinfo(_elem,_info){
    rc="INFO-"+_info+":";
    try {
        var txt = $(_elem).attr(_info);
        if (txt !== undefined){
            rc+=txt.toString();
        }
    }
    catch(err){rc+=err.message;}
    return rc;
};

function loadmp4(_file){showit("Load..."+_file);qgoproapp.setTestMediaSourceFile(_file);};
function showattributes(_this){var rc="";$(_this).each(function() {$.each(this.attributes, function() {if(this.specified) {console.log(this.name, this.value);rc+=this.name+"="+ this.value+"|\n";}});});showit(rc);return rc;}




function init(qgoproapp){
    var quikinfo={};

    LOG("","============== automation init==================");

    quikinfo["wintitle"]=qgoproapp.windowTitle;
    LOG("Quik_Title",quikinfo["wintitle"]);
    qgoproapp.windowTitle="Quik AUTOMATION";


    quikinfo["Ver"]=qgoproapp.getAppVersion();
    LOG("Ver:",quikinfo["Ver"]);

    quikinfo["AnalyticsGUID"]=qgoproapp.getAnalyticSessionID();
    LOG("AnalyticsGUID:",quikinfo["AnalyticsGUID"]);

    quikinfo["SettingsOffloadFolder"]=qgoproapp.getSettingsOffloadFolder();
    LOG("SettingsOffloadFolder:",quikinfo["SettingsOffloadFolder"]);

    quikinfo["isNetworkAvailable"]=qgoproapp.isNetworkAvailable();
    LOG("isNetworkAvailable:",quikinfo["isNetworkAvailable"]);

    quikinfo["isOnline"]=qgoproapp.isOnline();
    LOG("isOnline:",quikinfo["isOnline"]);
    //alert("test alert");
    qgoproapp.setEnabled(true);
    qgoproapp.setFocus();
    return quikinfo;
}

function resethilites(){
    $.each($('div.GoProUIMediaGrid2')[0].childNodes,function(i,val){
        if($(val).hasClass("GoProUIMediaThumbnail")){
            $(".autotest").remove();
            $(".thumbnail").css( "border", "");
            $(val).css( "border", "");
            $(".thumbnail-duration").css( "border", "");
            $(".thumbnail--icon-mediatype").css( "border", "");
            $(".GoProUIMediaThumbnail").css( "border", "");
        }
    });
}

function getMediaItemType(_item){
    try {
        var rc = $(_item).find(".thumbnail--icon-mediatype").children().attr('class').toString().replace("icon icon-", "");
        if (rc !== undefined) {
            return rc;
        }
    }
    catch(err){return err.message;}
    return "Not Found:thumbnail--icon-mediatype";
}

function getMediaItemHilight(_item){
    try {
        var rc = $(_item).find(".thumbnail-number-hilights").text();
        if (rc !== undefined) {
            if (rc.length===0){return "0";}else{return rc;}
        }
        else{
            return "Not Found:thumbnail-number-hilights";
        }
    }
    catch(err){return err.message;}
    return "Not Found:thumbnail-number-hilights";
}

function findClassText(_item,_class){
    try {
        var rc = $(_item).find(_class).text();
        if (rc !== undefined) {
            if (rc.length===0){return "0";}else{return rc;}
        }
        else{
            return "Not Found:"+_class;
        }
    }
    catch(err){return err.message;}
    return "Not Found:"+_class;
}

function getmediathumbinfo(thumbitem){
    thumbinfo={};
    thumbinfo.position=$(thumbitem).position();
    LOG("Position:",thumbinfo.position);
    thumbinfo.offset=$(thumbitem).offset();
    LOG("offset:",$(thumbitem).offset());
    thumbinfo.clientRect=thumbitem.getBoundingClientRect();
    LOG("Rect:",thumbinfo.clientRect);
    thumbinfo.thumbID=$(thumbitem).attr("id");
    LOG("id:",thumbinfo.thumbID);
    thumbinfo.filepath=$(thumbitem).find(".thumbnail").children().attr("src").replace("file:","");
    LOG("file:",thumbinfo.filepath);
    thumbinfo.mediaType=getMediaItemType($(thumbitem));
    LOG("MediaType:",thumbinfo.mediaType);
    thumbinfo.hilights=findClassText($(thumbitem),".thumbnail-number-hilights");
    LOG("Hilights:",thumbinfo.hilights);
    thumbinfo.duration=findClassText($(thumbitem),".thumbnail-duration");
    LOG("Duration:",thumbinfo.duration);

    return thumbinfo;
}

// function dowait(milliseconds,fn) {
//     var dt = new Date();
//     while ((new Date()) - dt <= milliseconds) { /* Do nothing */ }
//     fn();
// }





function testdowait(){
    var cnt=0;
    $.each($('div.GoProUIMediaGrid2')[0].childNodes,function(i,val){
        if($(val).hasClass("GoProUIMediaThumbnail")){
            console.log(val);
            //$(val).trigger("click");
            //window.setTimeout(function(){$(val).trigger("click");}, 5000);
            //dowait(5000,function(){$(val).trigger("click");console.log((cnt+=1)+"select media");});
            //dowait(5000,function(){$("a.context-menu--link.GoProJSMenuShowInfo").trigger("click");console.log((cnt+=1)+"show info");});
            //dowait(5000,function(){$("button.button.button-blue.GoProJSBaseModalClose").trigger("click");console.log((cnt+=1)+"close info");});
            //dowait(5000,function(){$("a.context-menu--link.GoProJSMenuShowInfo").trigger("click");console.log((cnt+=1)+"show info");});
            //window.setTimeout(function(){$("a.context-menu--link.GoProJSMenuShowInfo").trigger("click");}, 5000);
            //window.setTimeout(function(){$("button.button.button-blue.GoProJSBaseModalClose").trigger("click");}, 5000);
            //dowait(5000,function(){$("button.button.button-blue.GoProJSBaseModalClose").trigger("click");console.log((cnt+=1)+"close info");});
        }
    })
}

function dowait(milliseconds,fn){
    console.log("DOWAIT");
    console.log(fn);
    setTimeout(fn(),milliseconds);
}


function getdt(){
    var currentdate = new Date();
    return "" + currentdate.getDate() + "/"
        + (currentdate.getMonth()+1)  + "/"
        + currentdate.getFullYear() + " @ "
        + currentdate.getHours() + ":"
        + currentdate.getMinutes() + ":"
        + currentdate.getSeconds()+"."
        +currentdate.getMilliseconds();
}


var proc_ctrl={
    eval_count: 0,
    loop_element: "'div.GoProUIMediaGrid2')[0].childNodes",
    loop_len: 0,
    loop_count: 0,
    fn_count: 0,
    media_item: null,
    fn_list: [{id:-1,name:"media item click",js:"$(this.media_item).trigger('click');",delay:5000,result:""},
        {id:-1,name:"media_info_popup",js:"$('a.context-menu--link.GoProJSMenuShowInfo').trigger('click');",delay:5000,result:""},
        {id:-1,name:"media popup close",js:"$('button.button.button-blue.GoProJSBaseModalClose').trigger('click');",delay:5000,result:""}],

    fn_len: 0,
    fn_js: "",
    init: function(media_container){
        console.log("INIT>>>"+ getdt());
        this.loop_element=media_container;
        this.loop_len=this.loop_element.length;
        this.loop_count=0;
        this.fn_count=0;
        this.fn_len=this.fn_list.length;
        window.setTimeout(this.start(this),1000);
        console.log("INIT<<<"+ getdt());
        return "INIT<<<"+ getdt();
    },

    start: function(proc_ctrl){
        console.log("START>>>"+ getdt());
        //console.log(JSON.stringify(this));
        console.log("loop_element");
        console.log(proc_ctrl.loop_element);
        console.log("this");
        console.log(this);
        console.log("loop_len:"+proc_ctrl.loop_len);
        console.log("fn_len:"+proc_ctrl.fn_len);
        window.setTimeout(proc_ctrl.event_eval(proc_ctrl),1000);
        console.log("START<<<"+ getdt());
        return "START<<<"+ getdt();
    },

    event_eval: function(proc_ctrl){
        try {
            console.log((proc_ctrl.eval_count+=1)+".EVAL>>>"+ getdt());
            console.log("this");
            console.log(this);
            console.log("proc_ctrl");
            console.log(proc_ctrl);
            console.log("loop_count:" + proc_ctrl.loop_count + "   fn_count" + proc_ctrl.fn_count);
            if (proc_ctrl.fn_count < proc_ctrl.fn_len) {
                console.log("fn_list");
                //do fn_list index item then setTimeout for next
                proc_ctrl.media_item = proc_ctrl.loop_element[proc_ctrl.loop_count];
                console.log(proc_ctrl.media_item);

                proc_ctrl.fn_list[proc_ctrl.fn_count].id = proc_ctrl.loop_count;
                proc_ctrl.fn_js = proc_ctrl.fn_list[proc_ctrl.fn_count];
                proc_ctrl.fn_js.result = "result:" + proc_ctrl.fn_js.id;
                console.log(proc_ctrl.fn_js);

                //console.log(JSON.stringify(proc_ctrl.fn_list[proc_ctrl.fn_count].id));
                proc_ctrl.fn_list[proc_ctrl.fn_count] = proc_ctrl.fn_js;
                //console.log(proc_ctrl.fn_js);
                //eval(proc_ctrl.fn_js);

                proc_ctrl.fn_count += 1;
                window.setTimeout(proc_ctrl.event_eval(proc_ctrl), 6000);
                console.log(proc_ctrl.eval_count+".EVAL fn list<<<"+ getdt());
                //return proc_ctrl.eval_count+"EVAL fn list<<<"+ getdt();
            }
            else { //do next media item
                proc_ctrl.fn_count = 0;
                console.log("media list"+ getdt());
                if (proc_ctrl.loop_count < proc_ctrl.loop_len) {

                    proc_ctrl.loop_count += 1;
                    proc_ctrl.fn_count = 0;
                    console.log("next media list");
                    window.setTimeout(proc_ctrl.event_eval(proc_ctrl), 1000);
                    console.log(proc_ctrl.eval_count+".EVAL medialist<<<"+ getdt());
                    //return proc_ctrl.eval_count+".EVAL medialist<<<"+ getdt();
                }
                else {
                    console.log("DONE"+ getdt());

                }
            }
        }
        catch(err){
            console.log(proc_ctrl.eval_count+".ERROR:"+err.message+ getdt());
            console.log(err);
        }
    }

};

rc=proc_ctrl.init($('div.GoProUIMediaGrid2')[0].childNodes);
console.log(rc);

//proc_ctrl=proc_ctrl.start;

//proc_ctrl.start();


testdowait();

function iteratemedia(){
    var mediaList=[];
    var mediadate;
    $.each($('div.GoProUIMediaGrid2')[0].childNodes,function(i,val){
        var mediaitem;
        if($(val).hasClass("GoProUIMediaThumbnail")){
            //console.log(val);
            mediaitem=getmediathumbinfo(val);
            mediaitem.date_time=mediadate;

            dowait(5000,function(){$(val).trigger("click");});

            dowait(5000,function(){$("a.context-menu--link.GoProJSMenuShowInfo").trigger("click");});

            dowait(5000,function(){$("button.button.button-blue.GoProJSBaseModalClose").trigger("click");});
            mediaList.push(mediaitem);

            //$(val).find(".thumbnail-duration").append("<span class='autotest'> PASSED</span>");
            //$(".thumbnail").css( "border", "2px solid green"); //Hilight the thumbnail PASSED
            //$(".thumbnail").css( "border", "2px solid red"); //Hilight the thumbnail FAILED

            // $(val).css( "border", "1px solid green");
            // $(".thumbnail-duration").css( "border", "1px solid red");
            // $(".thumbnail").css( "border", "1px solid red");
            // $(".thumbnail--icon-mediatype").css( "border", "1px solid red");
            // console.log($(".thumbnail--icon-mediatype").html());

            //console.log($(".thumbnail-duration").html());
            //console.log($(".thumbnail--icon-hilight").html());
            //$(".GoProUIMediaThumbnail").css( "border", "1px solid green");
            //console.log($(val).html());
            //$(val).trigger("click");
            //var iit = {"duration":$(val).$("thumbnail-duration").html()};
            //scanmedia.push({"duration":$(".thumbnail-duration").html()});


        }
        else if($(val).hasClass("GoProUIMediaSectionTitle")){
            mediadate = val.innerText;
            //LOG("DATE-TIME:",mediadate);
        }
    })
    return mediaList;
}

//var quikinfo=init(qgoproapp);
//LOG("",quikinfo);
//resethilites();
testdowait();
// mediaList=iteratemedia();
// LOG("MediaList",mediaList);
//console.log("--------------");
