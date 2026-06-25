function toggleTopic(element) {
    // 1. Toggle our custom 'active-selected' tracking marker
    element.classList.toggle('active-selected');

    // 2. Toggle Bootstrap classes to swap the colors instantly
    element.classList.toggle('bg-danger');
    element.classList.toggle('text-white');
    element.classList.toggle('text-danger');
     // Removes the initial red text color
}



function fetchSearchedTopic(){
console.log("JS LOADED");
    document.getElementById('button-search').addEventListener('click',async () => {

     console.log("BUTTON:", document.getElementById('button-search'));

    const searchQuery = document.getElementById('search-input').value
    console.log(searchQuery)

    console.log(searchQuery.value);
    const response = await fetch(`${myTopicsUrl}?query=${encodeURIComponent(searchQuery)}`);
    const data = await response.json();

    console.log(data);
//update Ui here
    }
    )

    }
  document.addEventListener('DOMContentLoaded', fetchSearchedTopic);