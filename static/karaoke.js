
// Get the video player element
const videoPlayer = document.getElementById('video-player');
const videoLink = document.currentScript.getAttribute("video-link");
const instrumentLink = document.currentScript.getAttribute("instrumental-link");
const vocalsLink = document.currentScript.getAttribute("vocal-link");
let isSeeking = false; // Variable to track if the time slider is being actively dragged
let maxDuration = 0; // Variable to keep track of the maximum duration
let isPlaying = false;
console.log("From JS side");
console.log(videoLink)
console.log(instrumentLink);
console.log(vocalsLink);

videoPlayer.addEventListener('loadedmetadata', function() {
    // Set the video source to the dynamically loaded link is in the html
    // Mute the video
    videoPlayer.volume = 0;
    videoPlayer.pause();
    // Set the maximum duration and update the time slider's max value
    maxDuration = videoPlayer.duration;
    timeSlider.max = maxDuration;
});
 
 

const instrumentalAudio = WaveSurfer.create({
    container: "#waveform",
    waveColor: "#b828b8",
    progressColor: "#7500d5",
    interact : false
});

const vocalsAudio = WaveSurfer.create({
    container: "#waveform1",
    waveColor: "#b312b3",
    progressColor: "#7500d5",
    interact : false
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
const startTimeElement = document.getElementById('start-time');
const endTimeElement = document.getElementById('end-time');


const playPauseButton = document.getElementById('play-pause-button');


function togglePlayPause() {
  if (isPlaying) {
    pause();
  } else {
    play();
  }
}

function play() {
    instrumentalAudio.play();
    vocalsAudio.play();
    videoPlayer.play();
    isPlaying = true;
    playIcon.style.display = 'none';
    pauseIcon.style.display = 'inline';
  }
  
  function pause() {
    instrumentalAudio.pause();
    vocalsAudio.pause();
    videoPlayer.pause();
    isPlaying = false;
    playIcon.style.display = 'inline';
    pauseIcon.style.display = 'none';
  }

playPauseButton.addEventListener('click', togglePlayPause);


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
        var seekTime = (normalizedValue*videoPlayer.duration);
        videoPlayer.currentTime = seekTime;
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
        pause();
        isPlaying = false;
      }
      else{
        play();
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

// Add event listener for 'play' event of the video player
videoPlayer.addEventListener('play', function() {
    instrumentalAudio.play();
    vocalsAudio.play();
    isPlaying = true;
    playIcon.style.display = 'none';
    pauseIcon.style.display = 'inline';
});
  
// Add event listener for 'pause' event of the video player
videoPlayer.addEventListener('pause', function() {
    instrumentalAudio.pause();
    vocalsAudio.pause();
    isPlaying = false;
    playIcon.style.display = 'inline';
    pauseIcon.style.display = 'none';
});


// Function to convert seconds to HH:MM format
function formatTime(time) {
  const minutes = Math.floor(time / 60);
  const seconds = Math.floor(time % 60);
  return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

// Update start and end time elements
function updateStartEndTime() {
  const currentTime = videoPlayer.currentTime;
  const duration = videoPlayer.duration;

  startTimeElement.textContent = formatTime(currentTime);
  endTimeElement.textContent = formatTime(duration);
}

// Add event listener for time update event of the video player
videoPlayer.addEventListener('timeupdate', updateStartEndTime);

let lastTimeUpdate = 0;

videoPlayer.addEventListener('timeupdate', function() {
    if (!isSeeking) {
        const currentTime = videoPlayer.currentTime;
        if(Math.abs(currentTime - lastTimeUpdate) > 0.5) {
            const normalizedValue = currentTime / videoPlayer.duration;
            instrumentalAudio.seekTo(normalizedValue);
            vocalsAudio.seekTo(normalizedValue);
        }
        lastTimeUpdate = currentTime;
    }
    updateStartEndTime();
});