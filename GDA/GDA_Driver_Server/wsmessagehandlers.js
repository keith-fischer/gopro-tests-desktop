/**
 * Created by keithfisher on 12/29/15.
 */


wsmessagehandlers={

    startswith:function(txt,startswith){
        return(txt.indexOf(startswith) == 0);
    },
    on_text:function(conn, str){
        console.log("on_text:"+str);
        if(this.startswith(str,"REPORT:")){this.do_report(conn,str); return;}
        if(this.startswith(str,"STUFF:")){this.do_stuff(conn,str); return;}
        if(this.startswith(str,"SCREEN:")){this.do_screen(conn,str); return;}
        if(this.startswith(str,"ERROR:")){this.do_error(conn,str); return;}
        if(this.startswith(str,"GDA_START:")){this.do_gda_start(conn,str); return;}
        if(this.startswith(str,"MEDIA_LIST:")){this.do_medialist(conn,str); return;}
    },
    on_close : function(conn, code, reason){
        console.log("Connection closed");
    },
    do_report:function(conn, msg){
        console.log("do_report:"+msg);
        conn.sendText("do_report:"+msg);
    },
    do_stuff:function(conn,msg){
        console.log("do_stuff:"+msg);
        var m1 = msg.toUpperCase()+'!!!';
        var m2 = "qgoproapp.showTestMessage('"+m1+"');";
        var msg = "try{"+m2+"}catch(err){connection.send('EVAL ERROR'+err.message);}";
        console.log(msg);
        conn.sendText("do_stuff:"+msg);
    },
    do_screen:function(conn, msg){
        console.log("do_stuff:"+msg);
        conn.sendText("do_gda_start:"+msg);
    },
    do_error:function(conn, msg){
        console.log("do_error:"+msg);
        conn.sendText("do_gda_start:"+msg);
    },
    do_gda_start:function(conn, msg){
        console.log("do_gda_start:"+msg);
        conn.sendText("do_gda_start:"+msg);
    },
    do_medialist:function(conn, msg){
        console.log("do_gda_start:"+msg);
        conn.sendText("do_gda_start:"+msg);
    }
}

exports.wsmessagehandlers = wsmessagehandlers;
