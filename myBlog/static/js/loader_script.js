console.log("loader_script.js loaded");

const loader = {
    element: document.getElementById("global-loader"),

    show() {
        console.log("loader show called");
        this.element.classList.add("show");
    },

    hide() {
      console.log("loader hide called");
        this.element.classList.remove("show");
    }
};



window.closePage = function () {
    console.log("close clicked");
    window.history.back();
};