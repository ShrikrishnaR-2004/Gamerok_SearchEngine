// static/js/voice.js

window.onload = () => {
    const micBtn = document.getElementById('mic-btn');
    const inputField = document.getElementById('search-input');

    if (!micBtn || !inputField || !('webkitSpeechRecognition' in window)) return;

    const recognition = new webkitSpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    micBtn.onclick = () => {
        recognition.start();
    };

    recognition.onresult = (event) => {
        const speechResult = event.results[0][0].transcript;
        inputField.value = speechResult;
    };

    recognition.onerror = (event) => {
        alert('Speech recognition error: ' + event.error);
    };
};
