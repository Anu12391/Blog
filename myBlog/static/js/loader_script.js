
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

            el.classList.add("show");
        } else {
            console.warn("Target element '#global-loader' not found to show.");
        }
    },


    hide() {
        const el = this.getElement();
        if (el) {

            el.classList.remove("show");


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