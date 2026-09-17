from django.http import JsonResponse
from django.views.decorators.http import require_POST


def get_bot_response(message):
    message = message.lower().strip()

    # -----------------------------------------
    # GREETINGS
    # -----------------------------------------
    if any(word in message for word in [
        "hello", "hi", "hey", "good morning",
        "good afternoon", "good evening"
    ]):
        return (
            "Hello! 👋 Welcome to TechWell Solution.\n\n"
            "I'm here to help you find the right service. "
            "You can ask me about our services, software development, "
            "business solutions, digital services, government services, "
            "or wellness and counselling."
        )

    # -----------------------------------------
    # ALL SERVICES
    # -----------------------------------------
    if (
        "what services" in message
        or "services do you offer" in message
        or "your services" in message
        or message == "services"
    ):
        return (
            "TechWell Solution provides:\n\n"
            "• Technology Solutions\n"
            "• Digital Services\n"
            "• Business Solutions\n"
            "• Government & Online Services\n"
            "• Software Development\n"
            "• Wellness & Counselling\n\n"
            "Which service would you like to know more about?"
        )

    # -----------------------------------------
    # WEBSITE DEVELOPMENT
    # -----------------------------------------
    if (
        "website" in message
        or "web development" in message
        or "web design" in message
        or "web site" in message
    ):
        return (
            "We can help with website and web-based solutions. 🌐\n\n"
            "To understand what you need, tell me:\n"
            "• What type of business or organization is it?\n"
            "• What should the website do?\n"
            "• Do you already have a website?\n\n"
            "You can describe your idea in a few words."
        )

    # -----------------------------------------
    # SOFTWARE DEVELOPMENT
    # -----------------------------------------
    if (
        "software" in message
        or "custom system" in message
        or "system development" in message
        or "application" in message
        or "app development" in message
    ):
        return (
            "Our Software Development service focuses on building "
            "software and digital solutions around your needs. 💻\n\n"
            "If you have an idea for a system or application, "
            "tell me what problem you want it to solve and "
            "we can help you identify the right approach."
        )

    # -----------------------------------------
    # BUSINESS SOLUTIONS
    # -----------------------------------------
    if (
        "business solution" in message
        or "business solutions" in message
        or "help my business" in message
        or "business help" in message
        or "business technology" in message
    ):
        return (
            "Our Business Solutions help businesses use technology "
            "and digital tools more effectively. 📊\n\n"
            "Tell me about your business and the challenge you "
            "would like technology to help you solve."
        )

    # -----------------------------------------
    # DIGITAL SERVICES
    # -----------------------------------------
    if (
        "digital service" in message
        or "digital services" in message
        or "digital help" in message
        or "digital solution" in message
    ):
        return (
            "Our Digital Services help individuals and businesses "
            "access and use digital solutions more effectively.\n\n"
            "Tell me what digital service you need and I'll help "
            "you identify the appropriate area."
        )

    # -----------------------------------------
    # GOVERNMENT & ONLINE SERVICES
    # -----------------------------------------
    if (
        "government" in message
        or "government service" in message
        or "online service" in message
        or "online services" in message
        or "online application" in message
    ):
        return (
            "We provide assistance with Government & Online Services. "
            "If you're trying to access or complete an online service, "
            "tell me what you need help with and I'll guide you."
        )

    # -----------------------------------------
    # TECHNOLOGY SOLUTIONS
    # -----------------------------------------
    if (
        "technology" in message
        or "technology solution" in message
        or "technology solutions" in message
        or "tech support" in message
    ):
        return (
            "Our Technology Solutions are designed to help individuals "
            "and businesses make better use of technology.\n\n"
            "Tell me what technology challenge you're facing and "
            "I'll help you identify the right service."
        )

    # -----------------------------------------
    # WELLNESS & COUNSELLING
    # -----------------------------------------
    if (
        "wellness" in message
        or "counselling" in message
        or "counseling" in message
        or "mental wellbeing" in message
    ):
        return (
            "TechWell Solution also provides Wellness & Counselling "
            "services.\n\n"
            "If you'd like to learn more about the available support, "
            "please visit our Wellness & Counselling section or "
            "contact us for more information."
        )

    # -----------------------------------------
    # PRICING / QUOTATION
    # -----------------------------------------
    if (
        "price" in message
        or "pricing" in message
        or "cost" in message
        or "how much" in message
        or "quotation" in message
        or "quote" in message
        or "budget" in message
    ):
        return (
            "We provide quotations based on the specific service "
            "and requirements.\n\n"
            "To request a quotation, tell us what you need and "
            "we can help you identify the appropriate service."
        )

    # -----------------------------------------
    # CONTACT
    # -----------------------------------------
    if (
        "contact" in message
        or "email" in message
        or "phone" in message
        or "telephone" in message
        or "reach you" in message
    ):
        return (
            "You can contact TechWell Solution through the contact "
            "information available on our website.\n\n"
            "If you tell me what service you need, I can also help "
            "you identify the right service area."
        )

    # -----------------------------------------
    # THANK YOU
    # -----------------------------------------
    if (
        "thank you" in message
        or "thanks" in message
        or "thank" in message
    ):
        return (
            "You're welcome! 😊\n\n"
            "If you need anything else, I'm here to help."
        )

    # -----------------------------------------
    # GOODBYE
    # -----------------------------------------
    if (
        "bye" in message
        or "goodbye" in message
    ):
        return (
            "Thank you for visiting TechWell Solution. "
            "Have a great day! 👋"
        )

    # -----------------------------------------
    # DEFAULT RESPONSE
    # -----------------------------------------
    return (
        "I'd be happy to help you with TechWell Solution. 😊\n\n"
        "You can ask me about:\n"
        "• Our services\n"
        "• Website development\n"
        "• Software development\n"
        "• Business solutions\n"
        "• Digital services\n"
        "• Government & Online Services\n"
        "• Technology Solutions\n"
        "• Wellness & Counselling\n\n"
        "What would you like to know?"
    )


@require_POST
def chat(request):
    user_message = request.POST.get("message", "").strip()

    if not user_message:
        return JsonResponse(
            {"error": "Please enter a message."},
            status=400
        )

    response = get_bot_response(user_message)

    return JsonResponse({"reply": response})