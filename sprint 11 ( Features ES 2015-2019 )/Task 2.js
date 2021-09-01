

const howMuchSec = (sec = 0, min = 0, hour = 0, day = 0, week = 0, month = 0, year = 0 ) => {
    return sec +  min * 60 + hour * 3600 + day * 86400 + week * 604800 + month * 2592000 + year * 31536000
}
console.log(howMuchSec(0,0,0,6757));

