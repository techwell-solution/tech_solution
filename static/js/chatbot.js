document.addEventListener("DOMContentLoaded", function () {

    const chatbotButton = document.getElementById("chatbotButton");
    const chatbotWindow = document.getElementById("chatbotWindow");
    const chatbotClose = document.getElementById("chatbotClose");
    const chatbotForm = document.getElementById("chatbotForm");
    const chatbotInput = document.getElementById("chatbotInput");
    const chatbotMessages = document.getElementById("chatbotMessages");
    const chatbotTyping = document.getElementById("chatbotTyping");
    const quickActionButtons =
        document.querySelectorAll(".chatbot-quick-btn");


    // Open chatbot
    chatbotButton.addEventListener("click", function () {
        chatbotWindow.classList.add("active");
        chatbotInput.focus();
    });


    // Close chatbot
    chatbotClose.addEventListener("click", function () {
        chatbotWindow.classList.remove("active");
    });


    // Add message to chat
    function addMessage(message, sender) {

        const messageContainer = document.createElement("div");

        messageContainer.className =
            "chatbot-message " + sender;

        const bubble = document.createElement("div");

        bubble.className = "chatbot-bubble";

        bubble.textContent = message;

        messageContainer.appendChild(bubble);

        chatbotMessages.appendChild(messageContainer);

        chatbotMessages.scrollTop =
            chatbotMessages.scrollHeight;
    }


    // Send message
    chatbotForm.addEventListener("submit", async function (event) {

        event.preventDefault();

        const message = chatbotInput.value.trim();

        if (!message) {
            return;
        }


        // Display user's message
        addMessage(message, "user");

        chatbotInput.value = "";

        chatbotTyping.style.display = "block";


        try {

            const csrfToken =
                document.querySelector(
                    "[name=csrfmiddlewaretoken]"
                ).value;


            const formData = new FormData();

            formData.append("message", message);


            const response = await fetch(
                "/chatbot/chat/",
                {
                    method: "POST",
                    headers: {
                        "X-CSRFToken": csrfToken
                    },
                    body: formData
                }
            );


            const data = await response.json();

            chatbotTyping.style.display = "none";


            if (data.reply) {

                addMessage(
                    data.reply,
                    "bot"
                );

            } else {

                addMessage(
                    data.error ||
                    "Sorry, I couldn't process that message.",
                    "bot"
                );
            }


        } catch (error) {

            chatbotTyping.style.display = "none";

            addMessage(
                "Sorry, something went wrong. Please try again.",
                "bot"
            );

            console.error(error);
        }

    });


    // =========================================
    // QUICK ACTION BUTTONS
    // =========================================

    quickActionButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const message =
                button.getAttribute("data-message");

            if (!message) {
                return;
            }

            chatbotInput.value = message;

            chatbotForm.dispatchEvent(
                new Event("submit", {
                    bubbles: true,
                    cancelable: true
                })
            );

        });

    });

});