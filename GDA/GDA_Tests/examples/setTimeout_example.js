/**
 * Created by keithfisher on 1/24/17.
 */

/* this works */

console.log('before ' + new Date(Date.now()).toLocaleTimeString());

var d={
    count:0,
    st:function(){
        this.count+=1;
        if (this.count>5){return;}
        this.dowait(this);
    },
    dowait:function(_d){
        setTimeout(function() {
            _d.doshow(_d.count+". ");
            _d.st();
        }, 5000)
    },
    doshow: function(info){
        console.log(info + new Date(Date.now()).toLocaleTimeString());
    }
};

d.st();

/*
 setTimeout(function() {
 doshow("1st ");
 setTimeout(function() {
 doshow("2nd  ");
 setTimeout(function() {
 doshow("3rd ");
 }, 5000)
 }, 5000)
 }, 5000)
 */

