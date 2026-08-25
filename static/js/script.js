document.addEventListener("DOMContentLoaded", function () {

    const passwordInputs = document.querySelectorAll(
        'input[type="password"]'
    );

    passwordInputs.forEach(function (input) {

        const wrapper = document.createElement("div");

        wrapper.className = "password-wrapper";

        input.parentNode.insertBefore(wrapper, input);

        wrapper.appendChild(input);

        const button = document.createElement("button");

        button.type = "button";

        button.className = "password-toggle";

        button.textContent = "Show";

        wrapper.appendChild(button);

        button.addEventListener("click", function () {

            if (input.type === "password") {

                input.type = "text";

                button.textContent = "Hide";

            } else {

                input.type = "password";

                button.textContent = "Show";

            }

        });

    });

});

// Auto-hide flash messages
const messages = document.querySelectorAll(".message");

messages.forEach(function (message) {

    setTimeout(function () {

        message.style.opacity = "0";

        setTimeout(function () {
            message.remove();
        }, 500);

    }, 3000);

});
// Application form validation
const applicationForm = document.getElementById("application-form");

if (applicationForm) {

    applicationForm.addEventListener("submit", function (event) {

        const company = document
            .getElementById("company")
            .value
            .trim();

        const role = document
            .getElementById("role")
            .value
            .trim();

        if (company.length < 2) {

            event.preventDefault();

            alert("Please enter a valid company name.");

            return;
        }

        if (role.length < 2) {

            event.preventDefault();

            alert("Please enter a valid job role.");

            return;
        }

    });

}
// Delete confirmation modal
const deleteModal = document.getElementById("delete-modal");

const deleteTriggers = document.querySelectorAll(".delete-trigger");

const cancelDelete = document.getElementById("cancel-delete");

const closeModal = document.getElementById("modal-close");

const confirmDelete = document.getElementById("confirm-delete");

let selectedDeleteForm = null;


// Open modal
deleteTriggers.forEach(function (button) {

    button.addEventListener("click", function () {

        selectedDeleteForm = button.closest(".delete-form");

        deleteModal.classList.add("active");

    });

});


// Close modal
function closeDeleteModal() {

    deleteModal.classList.remove("active");

    selectedDeleteForm = null;

}


cancelDelete.addEventListener(
    "click",
    closeDeleteModal
);


closeModal.addEventListener(
    "click",
    closeDeleteModal
);


// Confirm deletion
confirmDelete.addEventListener("click", function () {

    if (selectedDeleteForm) {

        selectedDeleteForm.submit();

    }

});


// Close when clicking outside modal
deleteModal.addEventListener("click", function (event) {

    if (event.target === deleteModal) {

        closeDeleteModal();

    }

});


// Close with Escape key
document.addEventListener("keydown", function (event) {

    if (event.key === "Escape") {

        closeDeleteModal();

    }

});

// Mobile navigation
const menuToggle = document.getElementById("menu-toggle");
const navLinks = document.getElementById("nav-links");

if (menuToggle && navLinks) {

    menuToggle.addEventListener("click", function () {

        navLinks.classList.toggle("mobile-active");

        if (navLinks.classList.contains("mobile-active")) {
            menuToggle.textContent = "✕";
        } else {
            menuToggle.textContent = "☰";
        }

    });

}