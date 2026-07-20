// =========================================================================
// 1. STATE & GLOBAL CONFIG
// =========================================================================
let activeSelectedIds = [];
let searchTimer;

// DOM Cache (evaluated after DOM loads)
let elements = {};

// =========================================================================
// 2. CORE ACTIONS / EVENT HANDLERS
// =========================================================================

/**
 * Toggles selection state of a topic element and manages the ID array
 */
function toggleTopic(element) {
    element.classList.toggle('selected');
    const topicId = Number(element.getAttribute('data-topic-id'));

    if (element.classList.contains('selected')) {
        if (!activeSelectedIds.includes(topicId)) {
            activeSelectedIds.push(topicId);
        }
    } else {
        activeSelectedIds = activeSelectedIds.filter(id => id !== topicId);
    }

    console.log("Current selected IDs:", activeSelectedIds);
}

/**
 * Ensures that newly fetched AJAX elements reflect currently selected IDs
 */
function applySelectionUIState() {
    if (!elements.container) return;

    const topicElements = elements.container.querySelectorAll('[data-topic-id]');
    topicElements.forEach(element => {
        const topicId = Number(element.getAttribute('data-topic-id'));
        if (activeSelectedIds.includes(topicId)) {
            element.classList.add('selected');
        }
    });
}

/**
 * Fetches topics matching the search query via AJAX
 */
async function fetchSearchedTopic(event) {
    if (!elements.input || !elements.container) return;

    const searchQuery = elements.input.value;
    console.log("Searching for:", searchQuery);

    if (typeof loader !== 'undefined') loader.show();

    try {
        const response = await fetch(`${myTopicsUrl}?query=${encodeURIComponent(searchQuery)}`, {
            method: "GET",
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        });

        if (!response.ok) throw new Error(`Network response was not OK: ${response.status}`);

        const htmlData = await response.text();
        elements.container.innerHTML = htmlData;

        // Re-sync selection classes onto the freshly downloaded HTML
        applySelectionUIState();

    } catch (error) {
        console.error("AJAX Fetch failed:", error);
    } finally {
        if (typeof loader !== 'undefined') loader.hide();
    }
}

/**
 * Posts the active selected IDs array back to the server
 */
async function postSelectedIds() {
    if (typeof loader !== 'undefined') loader.show();

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

        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

        const result = await response.json();
        console.log("Post Success:", result);

    } catch (error) {
        console.error("Error during POST request:", error);
    } finally {
        if (typeof loader !== 'undefined') loader.hide();
    }
}

// =========================================================================
// 3. UTILITY FUNCTIONS
// =========================================================================

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

// =========================================================================
// 4. INITIALIZATION & LISTENERS
// =========================================================================

function init() {
    // Cache DOM Elements safely
    elements.searchBtn = document.getElementById("button-search");
    elements.input = document.getElementById("search-input");
    elements.container = document.getElementById("topics-container");
    elements.dataInitialState = document.getElementById('selected_ids');

    // Parse Initial State from Server
    if (elements.dataInitialState && elements.dataInitialState.textContent) {
        try {
            activeSelectedIds = JSON.parse(elements.dataInitialState.textContent);
            console.log("Loaded initial selected IDs:", activeSelectedIds);
            applySelectionUIState();
        } catch (e) {
            console.error("Failed to parse initial IDs:", e);
        }
    }

    // Manual Search Button Listener
    if (elements.searchBtn) {
        elements.searchBtn.addEventListener("click", fetchSearchedTopic);
    }

    // Debounced Search Input Listener
    if (elements.input) {
        elements.input.addEventListener("input", function (event) {
            clearTimeout(searchTimer);
            const query = this.value.trim();

            if (query.length === 0) {
                fetchSearchedTopic(event);
                return;
            }

            // Don't trigger a new search for 1 or 2 characters to avoid messy partial results
            if (query.length < 3) {
                return;
            }

//            if (query.length < 3) {
//                if (elements.container) elements.container.innerHTML = "";
//                return;
//            }

            searchTimer = setTimeout(() => {
                fetchSearchedTopic(event);
            }, 300);
        });
    }
}

// Bind bootstrap lifecycle event
document.addEventListener("DOMContentLoaded", init);