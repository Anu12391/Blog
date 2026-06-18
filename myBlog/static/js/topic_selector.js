function toggleTopic(element) {
    // 1. Toggle our custom 'active-selected' tracking marker
    element.classList.toggle('active-selected');

    // 2. Toggle Bootstrap classes to swap the colors instantly
    element.classList.toggle('bg-danger');
    element.classList.toggle('text-white');
    element.classList.toggle('text-danger'); // Removes the initial red text color
}