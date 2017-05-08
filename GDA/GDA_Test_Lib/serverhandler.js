
function eval_cmd(cmd){
    log('eval_cmd>');
    var evaljs="";
    if(cmd.length>0){
        var cmd=cmd.split(':');
        if(cmd.length>=2){
            cmd.shift();
            evaljs=cmd.join(":");
        }
    }
    log('eval_cmd<'+evaljs.length.toString());
    return evaljs;
}
eval_js="";
try{
    log('serverhandler>');
    if(cmdlist.length>0) {
        timecount = timeout;
        eval_js=eval_cmd(cmdlist.shift());
        if(eval_js.length>10) {
            var rc = eval(eval_js);
            connection.send('RESULT:' + rc);

        }
        else{
            log('No EVAL:serverhandler< evaljs.length>10');
        }
    }
    else{
        log('No TESTS to EVAL:serverhandler< cmdlist.length');
   }
    connection.send('NEXT_TEST:');
    log('serverhandler<');
}
catch(err1){
    connection.send("ERROR:serverhandler\n"+err1.message+"\nSCRIPT="+eval_js);
    connection.send('NEXT_TEST:');
    log('serverhandler<error');
}
