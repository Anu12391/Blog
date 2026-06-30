function toggleTopic(element) {
    // 1. Toggle our custom 'active-selected' tracking marker
//    element.classList.toggle('active-selected');

    // 2. Toggle Bootstrap classes to swap the colors instantly
    element.classList.toggle('selected');
    element.classList.toggle('text-white');
    element.classList.toggle('text-danger');
    const topicId = element.getAttribute('data-topic-id');
     // Removes the initial red text color
}



async function fetchSearchedTopic(event) {
    // Prevent standard form tracking from firing if it behaves like a submit button
    if (event) event.preventDefault();

    const searchInput = document.getElementById('search-input');
    if (!searchInput) return;

    const searchQuery = searchInput.value;
    console.log("Searching for:", searchQuery);

    try {
        const response = await fetch(`${myTopicsUrl}?query=${encodeURIComponent(searchQuery)}`, {
            method: "GET",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "x-requested-with": "XMLHttpRequest"
            }
        });

        if (!response.ok) throw new Error("Network response was not OK");

        const htmlData = await response.text();
        document.getElementById("topics-container").innerHTML = htmlData;

    } catch (error) {
        console.error("AJAX Fetch failed:", error);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const searchBtn = document.getElementById("button-search");
    if (searchBtn) {
        // Pass the event argument automatically
        searchBtn.addEventListener("click", fetchSearchedTopic);
    }
});