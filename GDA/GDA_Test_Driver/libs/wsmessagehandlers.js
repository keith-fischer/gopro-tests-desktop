/**
 * Created by keithfisher on 12/29/15.
 */


wsmessagehandlers={
    wapi: Object,
    Test_Count: 0,
    Test_Name:'',
    Test_Script:'',
    Results: [],
    js_script:'',
    server_state:'',
    callback_status:'',
    testmgr: Object,
    startswith:function(txt,startswith){
        return(txt.indexOf(startswith) === 0);
    },

    do_gda_wait:function(wait,status, msg){
        var rc;
        console.log(' wait Start GDA===================================================');
        for (var i = 0; i < wait; i++) {

            if(status===this.callback_status){
                rc=status;
                this.server_state=status;
                res.render('gdajstest', { title: 'GDA Javascript DOM Tester',testresults: _results , GDA_status: 'running'});
                console.log('running Start GDA==================================================');
                break;
            }
            else{
                setTimeout(function() {
                    //console.log(i.toString()+' wait '+msg+'==============================================');
                }, 1000);
            }
        }
        return status;
    },

    evalmodes:function(mode){
        switch (mode) {
            case 'RESULT':

                return 'TEST';
                break;

            case 'NEXT_TEST':
                return 'RESULT';
                break;

            case 'START':
                return 'TEST';

                break;

            default:
                //Statements executed when none of the values match the value of the expression
                break;
        }
    },

    on_text:function(conn, str){
        //console.log("on_text:"+str);
        //if(this.startswith(str,"DEBUG_TEST:")){this.debug_test(conn,str); return;}
        //if(this.startswith(str,"DEBUG_REPORT:")){this.debug_report(conn,str); return;}
        //if(this.startswith(str,"TEST:")){this.do_test(conn,str); return;}
        if(this.startswith(str,"NEXT_TEST:")){this.do_test(conn,str); return;}
        if(this.startswith(str,"RESULT:")){this.do_result(conn,str); return;}
        if(this.startswith(str,"REPORT:")){this.do_report(conn,str); return;}
        if(this.startswith(str,"LOG:")){this.do_log(conn,str); return;}
        //if(this.startswith(str,"STUFF:")){this.do_stuff(conn,str); return;}
        //if(this.startswith(str,"SCREEN:")){this.do_screen(conn,str); return;}
        if(this.startswith(str,"ERROR:")){this.do_error(conn,str); return;}
        if(this.startswith(str,"GDA_START:")){this.do_gda_start(conn,str); return;}
        if(this.startswith(str,"GDA_STOP:")){this.do_gda_stop(conn,str);}
    },

    on_close : function(conn, code, reason){
        console.log("===================================");
        console.log("NODE WebSocket is closed");
        console.log("===================================");
    },

    do_result:function(conn, msg){
        //console.timeEnd('Run Test');
        console.log("--------------------------");
        console.log("do_result:"+msg);
        console.log("--------------------------");
        this.testmgr.setresult(msg);
        //conn.sendText("do_report:"+msg);
    },
    do_report:function(conn, msg){
        console.log("--------------------------");
        console.log("do_report:"+msg);
        console.log("--------------------------");
        console.log(this.testmgr.gettestrun());
        //conn.sendText("do_report:"+msg);
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
        console.log("do_screen:"+msg);
        //conn.sendText("do_screen:"+msg);
    },

    do_error:function(conn, msg){
        console.log("--------------------------");
        console.log("do_error:"+msg);
        console.log("--------------------------");
        this.testmgr.setresult(msg);
    },
    do_log:function(conn, msg){
        //console.log("--------------------------");
        console.log(">>>"+msg);
        //console.log("--------------------------");
    },

    do_gda_start:function(conn, msg){
        console.log("do_gda_start:"+msg);
        //conn.sendText("do_gda_start:"+msg);
        this.do_gda_wait(15,"GDA_START","");
    },
    do_gda_stop:function(conn, msg){
        console.log("do_gda_stop:"+msg);
        //conn.sendText("do_gda_start:"+msg);
        console.log(this.testmgr.gettestrun());
    },
    do_test:function(conn, msg){
        console.log("do_test:"+msg);
        var m1 = this.Test_Script;
        var m2 = this.testmgr.nexttest(); //  "qgoproapp.showTestMessage('"+m1+"');";
        if(m2) {
            var msg = m2;  //"try{"+m2+m1+"}catch(err){connection.send('EVAL ERROR'+err.message);}";
            console.log(msg);
            //console.time('Run Test');
            conn.sendText("NEXT_TEST:" + msg);
        }
        else{
            console.log("=================");
            console.log("TESTS RUN DONE");
            console.log("=================");
            console.log(this.testmgr.gettestrun());
        }

    },

    debug_test:function(conn, msg){
        console.log("debug_test:"+msg);
        var m1 = this.js_script;
        //var m2 = "qgoproapp.showTestMessage('"+this.js_script+"');";
        var msg = "try{"+m1+"}catch(err){return 'DEBUG_REPORT:EVAL ERROR'+err.message;}";
        console.log('debug_test:'+msg);
        conn.sendText(msg);
    },

    debug_report:function(conn, msg){
        console.log("debug_report:"+msg);
        var m1 = this.Test_Script;
        var m2 = "qgoproapp.showTestMessage('"+m1+"');";
        var msg = "try{"+m2+m1+"}catch(err){connection.send('EVAL ERROR'+err.message);}";
        console.log(msg);
        conn.sendText("debug_report:"+msg);
    }
}

exports.wsmessagehandlers = wsmessagehandlers;
