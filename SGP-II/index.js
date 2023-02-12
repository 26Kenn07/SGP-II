let month = 1;
let week = 1;
let date = 1;
let day = 1;

const startmonth = 1;
const startdate = 1;
const startday = 1;

const endmonth = 6;
const enddate = 20;

while (month != endmonth + 1) {
    let classmonth = "m" + month;
    while (week <= 6) {
        const box = document.createElement("div");
        let cl = "week" + month + week;
        box.id = (cl);
        box.className="weeks"
        document.getElementById(classmonth).appendChild(box)
        week++;
    }
    week = 1;
    month++;
}

month = 1;

let curday = 7;
while (month <= endmonth) {
    let curweek = 1;
    let max = 0;
    if (month % 2 != 0) {
        max = 31;
    }
    else {
        max = 30
    }
    let tmp=1;
        while(tmp<curday)
        {
            let classmonth2 = "week" + month + curweek;
            const box = document.createElement("span");
            let cl = "day" + month + curweek + date;
            box.id = (cl);
            box.className = "dates";
            box.innerHTML = "᠎᠎ ᠎ ";
            box.style.paddingRight="12.6px"
            console.log("week" + month + curweek + date)
            document.getElementById(classmonth2).appendChild(box)
            tmp++;
        }
    while (date <= max) {
        let classmonth2 = "week" + month + curweek;
        const box = document.createElement("span");
        let cl = "day" + month + curweek + date;
        box.id = (cl);
        box.className = "dates";
        if(date<10)
        {
            box.innerHTML = "0"+date
        }
        else
        {
            box.innerHTML = date;
        }
        console.log("week" + month + curweek + date)
        document.getElementById(classmonth2).appendChild(box)
        if (month == endmonth && date == enddate) {
            break;
        }
        curday++;
        date++;
        if (curday > 7) {
            curday = 1;
            curweek++;
        }
        if (curweek > 6) {
            curweek = 1;
        }
    }
    curweek = 1;
    date = 1;
    month++;
}


// parent = document.getElementsByClassName('m1')[0];
// children = parent.lastElementChild;
// console.log(children)

