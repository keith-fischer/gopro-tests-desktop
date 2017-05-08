
var utils= {
    shell:require('shelljs/global'),
    runApp:function(app_path,args){
        console.log('Run App');
        var spawn = require('child_process').spawn;
        prc = spawn(app_path,  args);
        prc.stdout.setEncoding('utf8');
        var is_done = false;
        is_done=prc.stdout.on('data', function (data) {
            var str = data.toString()
            var lines = str.split(/(\r?\n)/g);
            console.log(lines.join(""));
            is_done =true;
            //return is_done;
        });

        prc.on('close', function (code) {
            console.log('process exit code ' + code);
        });
        for (var i = 0; i < 30; i++) {
            console.log('wait Start App===================================================');
            if(is_done){

                console.log('running App==================================================');
                break;
            }
            else{
                setTimeout(function() {
                    console.log('wait Start App==============================================');
                }, 1000);
            }
        }
        return is_done;
    },

    runGDA:function(){
        //prc = spawn('/Applications/GoPro.app/Contents/MacOS/GoPro',  ['GoProPlayerPlugin', '-testscript', '/Automation/gopro-tests-desktop/GDA/GDA_Test_Lib/servermsgloop.js', '-testinterval', '2000']);
        var apppath = '/Applications/GoPro.app/Contents/MacOS/GoPro';
        var args=['GoProPlayerPlugin', '-testscript', '/Automation/gopro-tests-desktop/GDA/GDA_Test_Lib/servermsgloop.js', '-testinterval', '2000'];
        if(this.runApp(apppath,args)){
            console.log("APP GDA STARTED");
        }
        else{
            console.log("FAILED:: APP GDA NOT STARTED");
        }
    },

    installTestapp:function(path){
        var sh="";
        var ismac;
        if(path.index(".dmg")>0){
            sh="sudo installpkg -i " + path; // read the notes file to setup installpkg
            console.log("installTestapp:dmg: "+sh);
            ismac=true;
        }
        else if(path.index(".exe")>0){
            sh="win_exe" + path;
            console.log("installTestapp:exe: "+sh);
            ismac=false;
        }
        if (sh.length>5){

            // Run external tool synchronously
            if (this.shell.exec(sh).code !== 0) {
                this.shell.echo('Error: '+sh);
                this.shell.exit(1);
                console.log("installTestapp:Error: "+sh);
            }
            else{
                console.log("installTestapp:OK: "+sh);
            }
        }
        else{
            console.log("installTestapp:Error: Invalid installer path");
        }

    },

    WhatPlatformMacOrWin: function () {
        var p = process.platform;//darwin(osx),linux,windows
        if(p=="darwin"){p="osx";}
        return p;
    },

    getEnvironment: function(){
        var platform = this.WhatPlatformMacOrWin();
        console.log("Node Env Variable: " + platform+ +" "+ process.env.NODE_ENV);
        switch(platform){
            case "osx":
                return {
                    platform: 'osx', //should be mac/win
                    websocket: 1234,
                    webapi: 3000
                };
                break;
            case "windows":
                return {
                    platform: 'windows', //should be mac/win
                    websocket: 1234,
                    webapi: 3000
                };
                break;
            case "linux":
                return {
                    platform: 'linux', //should be mac/win
                    websocket: 1234,
                    webapi: 3000
                };
                break;
            default:
                throw new Error("platform Not Recognized");
                break;
        }
    }
}
exports.utils = utils;