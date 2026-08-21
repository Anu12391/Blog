// Open the hidden file picker
function triggerFileInput(fieldId) {
    document.getElementById(fieldId).click();
}

// When a user selects a file to upload
function handleImageUpload(input, fieldId) {
    if (input.files && input.files[0]) {
        // 1. Uncheck the clear/delete box if it was previously checked
        document.getElementById(fieldId + '-clear').checked = false;

        // 2. Generate and update preview image
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('avatar-preview').src = e.target.result;
        }
        reader.readAsDataURL(input.files[0]);
    }
}

// When a user clicks "Remove Photo"
function handleImageDeletion(fieldId, defaultUrl) {
    // 1. Check Django's hidden clear field checkbox
    document.getElementById(fieldId + '-clear').checked = true;

    // 2. Clear any staged files in the file input file path
    document.getElementById(fieldId).value = '';

    // 3. Revert preview immediately to the default static avatar
    document.getElementById('avatar-preview').src = defaultUrl;
}

function previewImage(input, previewId) {
    const preview = document.getElementById(previewId);

    if (input.files && input.files[0]) {
        const reader = new FileReader();

        reader.onload = function (e) {
            preview.src = e.target.result;
            preview.classList.remove("d-none");
            preview.style.display = "block";
        };

        reader.readAsDataURL(input.files[0]);
    } else {
        preview.src = "";
        preview.classList.add("d-none");
        preview.style.display = "none";
    }
}