const mobileMenuButton =
    document.getElementById("mobile-menu-btn");

const mobileNav =
    document.getElementById("mobile-nav");


if (mobileMenuButton && mobileNav) {

    mobileMenuButton.addEventListener("click", () => {

        mobileNav.classList.toggle("active");

        const icon =
            mobileMenuButton.querySelector("i");

        if (mobileNav.classList.contains("active")) {

            icon.classList.remove("fa-bars");
            icon.classList.add("fa-xmark");

        } else {

            icon.classList.remove("fa-xmark");
            icon.classList.add("fa-bars");

        }

    });


    const mobileLinks =
        mobileNav.querySelectorAll("a");


    mobileLinks.forEach(link => {

        link.addEventListener("click", () => {

            mobileNav.classList.remove("active");

            const icon =
                mobileMenuButton.querySelector("i");

            icon.classList.remove("fa-xmark");
            icon.classList.add("fa-bars");

        });

    });

}