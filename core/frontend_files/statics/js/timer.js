const b1 = document.getElementById("b1");
const b2 = document.getElementById("b2");
const time_label = document.getElementById("time");

let hour = 0;
let min = 0;
let sec = 0;

function timer() {
    sec++;
    time_label.innerText = `${('00'+hour).slice(-2)}:${('00'+min).slice(-2)}:${('00'+sec).slice(-2)}`;
    
    if (sec == 59 && min != 59) {
        sec = -1;
        min++;
    }
    if (sec == 59 && min == 59) {
        hour++;
        min = 0;
        sec = -1;
    }
}

let interval = null;
let stopped = false;

b1.addEventListener("click", () => {
    if (interval == null || stopped) {
        interval = setInterval(timer, 1000);
        stopped = false;
    }
});

b2.addEventListener("click", () => {
    clearInterval(interval);
    stopped = true;
});
