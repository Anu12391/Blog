
let activeSelectedIds = [];
function toggleTopic(element) {

    // 2. Toggle Bootstrap classes to swap the colors instantly
    element.classList.toggle('selected');
//    element.classList.toggle('text-white');
//    element.classList.toggle('text-danger');
    const topicId = Number(element.getAttribute('data-topic-id'));
     // Removes the initial red text color


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




document.addEventListener("DOMContentLoaded", () => {
    const searchBtn = document.getElementById("button-search");
    if (searchBtn) {
        // Pass the event argument automatically
        searchBtn.addEventListener("click", fetchSearchedTopic);
        }
        const dataElement = document.getElementById('selected_ids');
        if (dataElement) {
        activeSelectedIds = JSON.parse(dataElement.textContent);
         console.log("selected ids", activeSelectedIds);
    }

});

function getCookie(name) {
    const cookies = document.cookie.split(";");

    for (let cookie of cookies) {
        cookie = cookie.trim();

        if (cookie.startsWith(name + "=")) {
            return decodeURIComponent(cookie.substring(name.length + 1));
        }
    }

    return null;
}

async function postSelectedIds() {


    try {
        const response = await fetch("/my-settings/topics/update/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify({
                'selectedTopicIds': activeSelectedIds
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const result = await response.json();
        console.log("Success:", result);

    } catch (error) {
        console.error("Error during POST request:", error);
    }
}