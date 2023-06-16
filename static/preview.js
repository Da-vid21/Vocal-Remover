const instrumentLink = document.currentScript.getAttribute("instrumental-link");
const vocalsLink = document.currentScript.getAttribute("vocal-link");
console.log("From JS side");
console.log(instrumentLink);
console.log(vocalsLink);
const instrumentalAudio = WaveSurfer.create({
    container: "#waveform",
    waveColor: "violet",
    progressColor: "purple"
});

const vocalsAudio = WaveSurfer.create({
    container: "#waveform1",
    waveColor: "violet",
    progressColor: "purple"
});


instrumentalAudio.load(instrumentLink);
vocalsAudio.load(vocalsLink);


// Rest of your code...




const playButton = document.getElementById('play-button');
const pauseButton = document.getElementById('pause-button');
const instrumentVolumeSlider = document.getElementById('instrumental-volume-slider');
const vocalVolumeSlider = document.getElementById('vocals-volume-slider');
const timeSlider = document.getElementById('time-slider');
const fileInput = document.getElementById('file-input');

timeSlider.min = 0;
timeSlider.value = 0;
//Setting start volume for vocal to 0 and 1 to instrumental
        


let isSeeking = false; // Variable to track if the time slider is being actively dragged
let maxDuration = 0; // Variable to keep track of the maximum duration
let isPlaying = false;
playButton.addEventListener('click', function() {
    instrumentalAudio.play();
    vocalsAudio.play();
    isPlaying = true;
});

pauseButton.addEventListener('click', function() {
    instrumentalAudio.pause();
    vocalsAudio.pause();
    isPlaying = false;
});

vocalVolumeSlider.addEventListener('input', function() {
    vocalsAudio.setVolume(vocalVolumeSlider.value / 100);
});
instrumentVolumeSlider.addEventListener('input', function() {
    instrumentalAudio.setVolume(instrumentVolumeSlider.value / 100);
    
});

timeSlider.addEventListener('input', function() {
    if (isSeeking) {
        const sliderValue = parseFloat(timeSlider.value);
        const normalizedValue = sliderValue / maxDuration;
        instrumentalAudio.seekTo(normalizedValue);
        vocalsAudio.seekTo(normalizedValue);
    }
});

timeSlider.addEventListener('mousedown', function() {
    isSeeking = true;
});

timeSlider.addEventListener('mouseup', function() {
    isSeeking = false;
});
// Spacebar function to pause and play
document.body.onkeyup = function(e) {
    if (e.key == " " ||
        e.code == "Space" ||      
        e.keyCode == 32      
    ) {
      if(isPlaying){
        instrumentalAudio.pause();
        vocalsAudio.pause();
        isPlaying = false;
      }
      else{
        instrumentalAudio.play();
        vocalsAudio.play();
        isPlaying = true;
      }
    }
}


        

instrumentalAudio.on('ready', function() {
    maxDuration = Math.max(instrumentalAudio.getDuration(), vocalsAudio.getDuration());
    timeSlider.max = maxDuration;
    // Setting Instrumental volume to full
    instrumentalAudio.setVolume(1);
});

vocalsAudio.on('ready', function() {
    maxDuration = Math.max(instrumentalAudio.getDuration(), vocalsAudio.getDuration());
    timeSlider.max = maxDuration;
    // Setting vocals volume to 0
    vocalsAudio.setVolume(0);
});

instrumentalAudio.on('audioprocess', function() {
    if (!isSeeking) {
        const currentTime = instrumentalAudio.getCurrentTime();
        timeSlider.value = currentTime;
    }
});

vocalsAudio.on('audioprocess', function() {
    if (!isSeeking) {
        const currentTime = vocalsAudio.getCurrentTime();
        if (currentTime > instrumentalAudio.getCurrentTime()) {
            timeSlider.value = currentTime;
        }
    }
});

