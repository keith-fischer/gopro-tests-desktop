/**
 * Created by keithfisher on 1/12/16.
 */


var testmgr= {
    testsuite:Object,
    testlist:[],
    resultlist:[],
    testindex:-1,
    currenttest:{},
    status:'start',
    test:false,
    nexttest:function(){
        this.test=false;
        if(this.status=='start'){this.testindex=0;}else{this.testindex++;}
        if(this.testindex>=this.testlist.length){this.status='done';return;}
        this.currenttest=this.testlist[this.testindex];
        this.status='run';
        this.test=true;
        this.resultlist[this.testindex]="";
        return this.currenttest;
    },
    setresult:function(result){
        this.resultlist[this.testindex]=result.replace('RESULT:','');
    },
    settest:function(testjs){
        this.reset();
        console.log("settest:"+testjs);
        this.testlist[0]=testjs;
        this.status='start';
    },
    loadsampletests:function(){
        this.reset();
        this.status='start';
        for (var i = 0; i < 3; i++) {
            this.testlist[i]="var rc;qgoproapp.saveWindowPositionSettings();rc='Normal:W='+window.innerWidth.toString()+' H='+window.innerHeight.toString();qgoproapp.windowMaximize();rc+=' Max:W='+window.innerWidth.toString()+' H='+window.innerHeight.toString();qgoproapp.restoreWindowPositionSettings();rc+=' Normal2:W='+window.innerWidth.toString()+' H='+window.innerHeight.toString();";
            //return 'TEST RESULT="+ i.toString()+"';
            //qgoproapp.showTestMessage('RUNNING_TEST:"+ i.toString()+"-'+rc.toString());

        }
    },
    loadtestfromjson:function(_path){
        this.reset();
        this.testsuite = require(_path);
        if(!this.testsuite)return;
        if(this.testsuite.suitename && this.testsuite.testlist) {
            if(this.testsuite.testlist.length>0){
                for (var i = 0; i < this.testsuite.testlist.length; i++) {
                    this.testlist[i]=this.testsuite.testlist[i].js;
                }
            }
        }

    },
    gettestrun:function(){
        var rc=[];
        for (var i = 0; i < this.testlist.length; i++) {
            rc[i]="TEST "+ (i+1).toString()+":"+this.testlist[i]+"\nRESULT "+ (i+1).toString()+":"+this.resultlist[i];
        }
        return rc.join("\n\n");
    },
    reset: function(){
        this.status="";
        this.test=false;
        this.testlist=[];
        this.currenttest=[];
        this.testindex=-1;
    }
}

exports.testmgr = testmgr;

