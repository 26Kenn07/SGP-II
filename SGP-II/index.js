

let weeks = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"];
let months = ["January", "February", "March", "April", "May", "June", "July", "August", "Saptempber", "October", "November", "December"]



let month = 10;//starting month
let week = 1;
let date = 1;
let day = 1;



let tmpmonth = month;

const startmonth = 1;
const startdate = 1;
const startday = 1;
let curday = 7; //starting var

const endmonth = 1;
const enddate = 20;


//------------------------------------------------------------------------------------------------------------

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

//------------------------------------------------------------------------------------------------------------

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

//------------------------------------------------------------------------------------------------------------

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

//-----------------------------------------------------------------------------------------------------------

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

//-----------------------------------------------------------------------------------------------------------

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


// parent = document.getElementsByClassName('m1')[0];
// children = parent.lastElementChild;
// console.log(children)

