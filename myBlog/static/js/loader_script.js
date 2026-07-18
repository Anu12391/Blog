/**
 * Global UI Loader Controller
 */
const loader = {
    element: null,


    getElement() {
        if (!this.element) {
            this.element = document.getElementById("global-loader");
        }
        return this.element;
    },


    show() {
        const el = this.getElement();
        if (el) {
            // Remove the absolute hiding style if it was applied previously
            el.style.removeProperty("display");
            el.classList.add("show");
        } else {
            console.warn("Target element '#global-loader' not found to show.");
        }
    },


    hide() {
        const el = this.getElement();
        if (el) {
            // 1. Remove the active visibility class
            el.classList.remove("show");

//            // 2. Heavy fallback override: forces it away even if custom CSS rules collide
//            el.style.setProperty("display", "none", "important");
        } else {
            console.warn("Target element '#global-loader' not found to hide.");
        }
    }
};


if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => loader.hide());
} else {
    loader.hide();
}


window.closePage = function () {
    window.history.back();
};