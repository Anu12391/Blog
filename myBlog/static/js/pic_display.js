function previewImage(input,img_id) {
    const preview = document.getElementById('avatar-preview');

    // Check if a file was actually selected
    if (input.files && input.files[0]) {
        const reader = new FileReader();

        // When the file is done reading locally, swap the image src attribute
        reader.onload = function(e) {
            preview.src = e.target.result;
        }

        // Read the local file as a temporary Data URL
        reader.readAsDataURL(input.files[0]);
    }
}
