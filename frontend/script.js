document.getElementById('toggleButton').addEventListener('click', () => {
    const images = document.querySelectorAll('.image');
    images.forEach(image => {
        image.classList.toggle('hidden'); // Toggle visibility
    });
});

document.getElementById('send-button').addEventListener('click',() => {
    let msgbox = document.getElementById('message-box')
    let msgtxt = msgbox.value

    console.log(msgtxt)
    fetch('http://127.0.0.1:5000', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json', 
        }, 
        body: JSON.stringify({ msgtxt: msgtxt }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('HTTP error! Status: $(response.status}');
        }
        return response.json();
    })
    .then(data => {
        console.log('Message sent successfully:', data);
        let chat= document.getElementById("chat-container")
        chat.innerHTML = chat.innerHTML+`<div class="bubble right">${data.gusReply}</div>`
    })
    .catch(error => {
        console.error('Error sending message:', error);
    });
});