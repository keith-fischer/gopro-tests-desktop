/**
 * Created by keithfisher on 1/24/17.
 */
function LOG(label,printinfo){
    if(logverbose){
        console.log(label);
        console.log(printinfo);
        var sr=JSON.stringify(printinfo);
        console.log(label+sr);
        qgoproapp.logMessage(label+sr);
    }
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


function init(qgoproapp){
    var quikinfo={};
    qgoproapp.logMessage("============== automation init==================");
    console.log("============== automation init==================");

    qgoproapp.windowTitle="Quik AUTOMATION";
    quikinfo.wintitle="Quik AUTOMATION";

    quikinfo.Ver=qgoproapp.getAppVersion();
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

var testListMedia={
    media_container: null,
    media_item: null,
    webconnect: null,
    media_index: -1,
    media_dom: null,
    media_info: {},
    media_list: [],
    findClassText: function (_item,_class){
        try {
            var rc = $(_item).find(_class).text();
            if (rc !== undefined) {
                if (rc.length===0){return "0";}else{return rc;}
            }
            else{
                return "class text Not Found:"+_class;
            }
        }
        catch(err){return err.message;}

    },

    getMediaItemType: function (_item){
        try {
            var rc = $(_item).find(".thumbnail--icon-mediatype").children().attr('class').toString().replace("icon icon-", "");
            if (rc !== undefined) {
                return rc;
            }
            else{
                return "Not Found:thumbnail--icon-mediatype";
            }
        }
        catch(err){return err.message;}

    },

    getMediaItemHilight: function (_item){
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

    },

    getmediathumbinfo: function (_testListMedia){
        mediainfo={};
        try {
            mediainfo.position = JSON.stringify($(this.media_item).position());
            //LOG("Position:",thumbinfo.position);
            mediainfo.offset = JSON.stringify($(this.media_item).offset());
            //LOG("offset:",$(this.media_item).offset());
            mediainfo.clientRect = JSON.stringify(_testListMedia.media_item.getBoundingClientRect());
            //LOG("Rect:",thumbinfo.clientRect);
            mediainfo.thumbID = $(this.media_item).attr("id");
            //LOG("id:",thumbinfo.thumbID);
            mediainfo.thumbpath = $(this.media_item).find(".thumbnail").children().attr("src").replace("file:", "");
            //LOG("file:",thumbinfo.filepath);
            mediainfo.mediaType = this.getMediaItemType(this.media_item);
            //LOG("MediaType:",thumbinfo.mediaType);
            mediainfo.hilights = this.findClassText($(this.media_item), ".thumbnail-number-hilights");
            //LOG("Hilights:",thumbinfo.hilights);
            mediainfo.duration = this.findClassText($(this.media_item), ".thumbnail-duration");
            //LOG("Duration:",thumbinfo.duration);
        }
        catch(err){
            console.log("getmediathumbinfo:"+err.message);
        }
        return mediainfo;
    },

    getMediaItemInfoDetails: function(mediainfo){
        mediainfo.file=$("span.show-info-url").text();
        mediainfo.type=$("div.show-info-item--detail#show-info-type").text();
        mediainfo.created=$("div.show-info-item--detail#show-info-date-created").text();
        mediainfo.size=$("div.show-info-item--detail#show-info-file-size").text();
        mediainfo.length=$("div.show-info-item--detail#show-info-duration").text();

        mediainfo.resolution=$("div.show-info-item--detail#show-info-resolution").text();

        mediainfo.bitrate=$("div.show-info-item--detail#show-info-bitrate").text();
        //photo
        mediainfo.photoresolution=$("div.show-info-item--detail#show-info-megapixel").text();
        mediainfo.framerate=$("div.show-info-item--detail#show-info-item_count").text();

        return mediainfo;
    },

    testInitStart: function(Quik_Info,webclient){
        this.media_dom=this;
        this.webconnect=webclient;
        this.webconnect.init();
        this.quikInfo=Quik_Info;
        //this.media_list.push(this.quikInfo);
        this.media_index=-1;
        this.media_container=$('div.GoProUIMediaGrid2')[0].childNodes;
        this.iterateMediaItems(this);
    },

    setMediaItem: function(_testListMedia){
        if (this.isMedia(this.media_container[_testListMedia.media_index])) {
            this.media_item=this.media_container[_testListMedia.media_index];
            return true;
        }
        return false;
    },

    isMedia: function(_media) {
        //console.log(_media);
        return $(_media).hasClass("GoProUIMediaThumbnail");
    },

    iterateMediaItems: function(_testListMedia){
        _testListMedia.media_index+=1;
        console.log("==================================");
        console.log(_testListMedia.media_index + ". Media Items Count=" + this.media_container.length);
        console.log("==================================");
        //if (_testListMedia.media_index<this.media_container.length) {
        if (_testListMedia.media_index<10) {
            _testListMedia.selectMediaItem(_testListMedia);
        }
        else{
            console.log(JSON.stringify(_testListMedia.media_list));
            var fname = "MediaItemsVer";//+_testListMedia.quikInfo.Ver+".json";//+"_"+_testListMedia.quikInfo.AnalyticsGUID+".json";
            console.log("Save file to localStorage:"+fname);
            _testListMedia.webconnect.connection.send("{'message':'media_list','info':"+JSON.stringify(_testListMedia.media_list))
            //localStorage.setItem(fname, JSON.stringify(_testListMedia.media_list));
            console.log("DONE");
        }

    },

    selectMediaItem: function(_testListMedia){ //select highlight,popup,close
        console.log("selectMediaItem>>>");

        if(_testListMedia.setMediaItem(_testListMedia)==true){
            console.log("setTimeout>>>");
            setTimeout(function(){
                console.log("setTimeout<<<");
                console.log(_testListMedia.media_index);
                console.log(_testListMedia.media_item);

                try {
                    _testListMedia.media_info = _testListMedia.getmediathumbinfo(_testListMedia);

                    console.log(JSON.stringify(_testListMedia.media_info));
                    $(_testListMedia.media_item).trigger("click");
                    //$(_testListMedia.media_item).trigger('click');
                    var id="#"+$(_testListMedia.media_item).attr('id');
                    console.log(id);
                    $(id).trigger('contextmenu');
                    //$($(_testListMedia.media_item).attr('id')).trigger('contextmenu');
                    //$('#GoProUIMediaGrid2Thumb-0000000003').trigger('contextmenu');
                }
                catch(err){
                    console.log("ERROR setTimeout<<<" + err.message);
                }

                _testListMedia.MediaInfo_open(_testListMedia);
            },2000)
        }
        else {
            console.log("SKIPPED: not media item");
            _testListMedia.iterateMediaItems(_testListMedia); //skip to next
        }
        console.log("selectMediaItem<<<");
    },

    MediaInfo_open: function(_testListMedia){
        setTimeout(function(){
            $("a.context-menu--link.GoProJSMenuShowInfo").trigger("click"); //works but invalid data, need context menu
            _testListMedia.media_info=_testListMedia.getMediaItemInfoDetails(_testListMedia.media_info);
            console.log(JSON.stringify(_testListMedia.media_info));
            _testListMedia.media_list.push(_testListMedia.media_info);
            _testListMedia.MediaInfo_close(_testListMedia);
        },1000)
    },

    MediaInfo_close: function(_testListMedia){
        setTimeout(function(){
            $("button.button.button-blue.GoProJSBaseModalClose").trigger("click");
            _testListMedia.iterateMediaItems(_testListMedia);
        },500)
    }
};





var logverbose=true;
var quikinfo=init(qgoproapp);
LOG("",quikinfo);
//testListMedia.testInitStart(quikinfo,webclient);


// var webclient= {
//     connection: NaN,
//
//     init: function () {
//         try{this.connection.close();}catch(err){}
//         this.connection  = new WebSocket('ws://localhost:1234');
//
//         this.connection.onopen = function () {
//             console.log('onopen:');
//             //this.connection.send('GDA_WebSocket_Start');
//
//         };
//
//         this.connection.onerror = function (err) {
//             console.log('onerror:' + err.message);
//             //this.connection.send('onerror:WebSocket Error ' + err.message);
//         };
//
//         this.connection.onmessage = function (e) {
//             console.log("onmessage:"+JSON.stringify(e.data));
//
//         };
//
//         this.connection.onclose = function () {
//             console.log('onclose:');
//
//         }
//     },
//
//     send: function (_data){
//         if(this.connection.readyState == 1){
//             this.connection.send(_data);
//         }
//         else{
//             this.connection.onopen = function( e) {
//                 console.log("onmessage:"+JSON.stringify(e.data));
//                 e.send(_data);
//             }
//         }
//     }
// };

var _connection = new window.WebSocket('ws://localhost:1234');

_connection.onopen = function () {
    console.log("onopen");
};
_connection.onerror = function (err) {
    console.log('onerror ' + err.message);
};
_connection.onmessage = function (e) {
    console.log("onmessage "+JSON.stringify(e.data));
};
_connection.onclose = function(){
    console.log("onclose");
};


console.log(_connection);

_connection.send('1MEDIA_LIST:');
_connection.send
_connection.send('2MEDIA_LIST:');
_connection.close();
