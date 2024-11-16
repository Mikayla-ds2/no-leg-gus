document.getElementById('toggleButton').addEventListener('click', () => {
    const images = document.querySelectorAll('.image');
    images.forEach(image => {
        image.classList.toggle('hidden'); // Toggle visibility
    });
});
