

let weeks = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"];
let months = ["January", "February", "March", "April", "May", "June", "July", "August", "Saptempber", "October", "November", "December"]
let dbmsday = [1,1,1,1,0,0,0];
let dsaday = [0,1.1,0,1,0,0];


let month = 1;//starting month
let week = 1;
let date = 1;
let day = 1;



let tmpmonth = month;

const startmonth = 1;
const startdate = 1;
const startday = 1;
let curday = 7; //starting var

const endmonth = 6;
const enddate = 19;


//--------------------------------------------------------------------------------------------------------------

//start adding month

while (month != endmonth + 1) {
    let classmonth = "m" + month;
    const box = document.createElement("div");
    box.id = (classmonth);
    box.className = "month" + " " + "col"
    document.getElementById("main-cal").appendChild(box)
    month++;
    if (month > 12) {
        month = 1;
    }
}

//end adding month

//--------------------------------------------------------------------------------------------------------------

//starting printing month name

month = tmpmonth;

while (month != endmonth + 1) {
    let classmonth = "m" + month;
    const box = document.createElement("div");
    box.id = "monthname" + classmonth;
    let tmpweeks = "monthname" + classmonth;
    box.className = "monthname";
    box.innerHTML = months[month - 1]
    document.getElementById(classmonth).appendChild(box);
    month++;
    if (month > 12) {
        month = 1;
    }
}

//end printing monthname

//--------------------------------------------------------------------------------------------------------------

//start printing weeks name

month = tmpmonth;

while (month != endmonth + 1) {
    let classmonth = "m" + month;
    const box = document.createElement("div");
    box.id = "weeksname" + classmonth;
    let tmpweeks = "weeksname" + classmonth;
    box.className = "weeksname";
    document.getElementById(classmonth).appendChild(box);
    for (let a = 0; a < 7; a++) {
        const box1 = document.createElement("span");
        box1.innerHTML = weeks[a];
        box1.className = "weeksnameindi";
        document.getElementById(tmpweeks).appendChild(box1)
    }
    month++;
    if (month > 12) {
        month = 1;
    }
}

//end printing weeks name

//--------------------------------------------------------------------------------------------------------------

//start adding weeks

month = tmpmonth;

while (month != endmonth + 1) {
    let classmonth = "m" + month;
    while (week <= 6) {
        const box = document.createElement("div");
        let cl = "week" + week + "m" + month;
        box.id = (cl);
        box.className = "weeks"
        document.getElementById(classmonth).appendChild(box)
        week++;
    }
    week = 1;
    month++;
    if (month > 12) {
        month = 1;
    }
}

//end adding weeks

//--------------------------------------------------------------------------------------------------------------

//start adding dates

month = tmpmonth;

while (month != endmonth + 1) {
    let week = 1;
    let max = 0;
    if (month == 2) {
        max = 28;
    }
    else if (month == 7 || month == 8) {
        max = 31;
    }
    else if (month % 2 != 0) {
        max = 31;
    }
    else {
        max = 30
    }
    let tmp = 1;
    while (tmp < curday) {
        let classmonth2 = "week" + week + "m" + month;
        const box = document.createElement("span");
        box.id = ("trash");
        box.className = "dates";
        box.innerHTML = "᠎᠎ ᠎ ";
        box.style.paddingRight = "12.6px"
        document.getElementById(classmonth2).appendChild(box)
        tmp++;
    }
    while (date <= max) {
        let classmonth2 = "week" + week + "m" + month;
        const box = document.createElement("span");
        let cl = "day" + month + date;
        box.id = (cl);
        box.className = "dates";
        if (date < 10) {
            box.innerHTML = "0" + date
        }
        else {
            box.innerHTML = date;
        }
        document.getElementById(classmonth2).appendChild(box)
        if (month == endmonth && date == enddate) {
            break;
        }
        curday++;
        date++;
        if (curday > 7) {
            curday = 1;
            week++;
        }
        if (week > 6) {
            week = 1;
        }
    }
    week = 1;
    date = 1;
    month++;
    if (month > 12) {
        month = 1;
    }
}

//end adding dates

//--------------------------------------------------------------------------------------------------------------

//start for dbms static data oprations

let dbmst = 30;
let dbmsn = 21;
let tmpdbmsn = dbmsn;

while ((dbmsn / dbmst) * 100 < 80) {
    dbmst++;
    dbmsn++;
}

let itrdbms = dbmsn - tmpdbmsn;
console.log(itrdbms);
let startingd = 15; // today's date
let startingm = 2;  //today's month

let tmpd = startdate
let tmpm = startmonth
let tmpvar = curday

// let conformvar = 0;
// let datecur = new Date().toDateString();
// let datecurvar = datecur.slice(0, 3)
// if (datecurvar === "Mon") conformvar = 0;
// else if (datecurvar === "Tue") conformvar = 1;
// else if (datecurvar === "Wed") conformvar = 2;
// else if (datecurvar === "The") conformvar = 3;
// else if (datecurvar === "Fri") conformvar = 4;
// else if (datecurvar === "Sat") conformvar = 5;
// else if (datecurvar === "Sun") conformvar = 6;
// conformvar++;
// console.log(conformvar);

let conformvar = 2;

let tmpitr = 0;
while (tmpitr < itrdbms) {
    while (startingm != endmonth && tmpitr < itrdbms) {
        let max = 0;
        if (startingm == 2) {
            max = 28;
        }
        else if (startingm == 7 || month == 8) {
            max = 31;
        }
        else if (startingm % 2 != 0) {
            max = 31;
        }
        else {
            max = 30
        }
        while (startingd <= max && tmpitr < itrdbms) {
            let idnamedbms = "day" + startingm + startingd;
            // console.log(idnamedbms);
            if(dbmsday[conformvar]!=0)
            {
                console.log(idnamedbms);
                // console.log(dbmsday[conformvar]);
                tmpitr+=dbmsday[conformvar];
                document.getElementById(idnamedbms).style.color = "red";
            }
            // console.log(conformvar)
            // tmpitr++;
            conformvar++;
            if(conformvar>6)conformvar=0;
            startingd++;
        }
        startingd=1;
        startingm++;
        if (startingm > 12) startingm = 1;
    }

}

//end dbms static data opration

//--------------------------------------------------------------------------------------------------------------




// parent = document.getElementsByClassName('m1')[0];
// children = parent.lastElementChild;
// console.log(children)

