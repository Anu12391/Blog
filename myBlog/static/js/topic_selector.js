
let activeSelectedIds = [];
function toggleTopic(element) {

     element.classList.toggle('selected');
     const topicId = element.getAttribute('data-topic-id');
     // Check if the element IS selected after the toggle
    if (element.classList.contains('selected')) {
        // If it was just selected, add the ID to our list if it's not already there
        if (!activeSelectedIds.includes(topicId)) {
            activeSelectedIds.push(topicId);
        }
    } else {
        // If it was unselected, remove the ID from our list
        activeSelectedIds = activeSelectedIds.filter(id => id !== topicId);
    }

    console.log("Current selected IDs:", activeSelectedIds);

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


fun updateTopicSelection()
{



}


document.addEventListener("DOMContentLoaded", () => {
    const searchBtn = document.getElementById("button-search");
    if (searchBtn) {
        // Pass the event argument automatically
        searchBtn.addEventListener("click", fetchSearchedTopic);
    }
    document.getElementById("updateTopic-btn").addEventListener("click", updateTopicSelection);
});