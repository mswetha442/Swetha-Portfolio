/* =========================================================
   SWETHA PORTFOLIO
   SCROLL REVEAL
========================================================= */

const revealElements = document.querySelectorAll(
    ".about-content, .skills-heading, .skill-item, .projects-heading, .project-card, .contact-section"
);

const observer = new IntersectionObserver(
    (entries) => {

        entries.forEach((entry) => {

            if (entry.isIntersecting) {
                entry.target.classList.add("show");
            }

        });

    },
    {
        threshold: 0.15
    }
);

revealElements.forEach((element) => {
    element.classList.add("reveal");
    observer.observe(element);
});


/* =========================================================
   AVATAR SCROLL EFFECT
========================================================= */

const avatar = document.getElementById("avatar");

window.addEventListener("scroll", () => {

    if (!avatar) return;

    const scrollPosition = window.scrollY;

    const rotation = Math.min(scrollPosition * 0.015, 8);

    const movement = Math.min(scrollPosition * 0.08, 35);

    avatar.style.transform =
        `translateY(${movement}px) rotate(${rotation}deg)`;

});


/* =========================================================
   HERO MOUSE PARALLAX
========================================================= */

const hero = document.querySelector(".hero");
const avatarContainer = document.querySelector(".avatar-container");

if (hero && avatarContainer) {

    hero.addEventListener("mousemove", (event) => {

        const rect = hero.getBoundingClientRect();

        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const moveX = (x - centerX) / 35;
        const moveY = (y - centerY) / 35;

        avatarContainer.style.transform =
            `translate(${moveX}px, ${moveY}px)`;
    });

    hero.addEventListener("mouseleave", () => {

        avatarContainer.style.transform =
            "translate(0, 0)";
    });
}


/* =========================================================
   ACTIVE NAVIGATION
========================================================= */

const sections = document.querySelectorAll(
    "#about, #skills, #education, #projects, #contact"
);

const navLinks = document.querySelectorAll(".nav-link");

const navObserver = new IntersectionObserver(
    (entries) => {

        entries.forEach((entry) => {

            if (entry.isIntersecting) {

                navLinks.forEach((link) => {
                    link.classList.remove("active");
                });

                const activeLink = document.querySelector(
                    `.nav-link[href="#${entry.target.id}"]`
                );

                if (activeLink) {
                    activeLink.classList.add("active");
                }

            }

        });

    },
    {
        threshold: 0.45
    }
);

sections.forEach((section) => {
    navObserver.observe(section);
});


/* =========================================================
   E-COMMERCE PROFESSIONAL CAROUSEL
========================================================= */

document.addEventListener("DOMContentLoaded", () => {

    const slides = document.querySelectorAll(".ecommerce-slide");
    const dots = document.querySelectorAll(".carousel-dot");
    const previousButton = document.querySelector(".carousel-prev");
    const nextButton = document.querySelector(".carousel-next");

    if (!slides.length) return;

    let currentSlide = 0;
    let autoSlide;


    function showSlide(index) {

        slides.forEach((slide) => {
            slide.classList.remove("active");
        });

        dots.forEach((dot) => {
            dot.classList.remove("active");
        });

        currentSlide = (index + slides.length) % slides.length;

        slides[currentSlide].classList.add("active");

        if (dots[currentSlide]) {
            dots[currentSlide].classList.add("active");
        }
    }


    function nextSlide() {
        showSlide(currentSlide + 1);
    }


    function previousSlide() {
        showSlide(currentSlide - 1);
    }


    function startAutoSlide() {

        clearInterval(autoSlide);

        autoSlide = setInterval(() => {
            nextSlide();
        }, 4000);

    }


    /* NEXT */

    nextButton.addEventListener("click", () => {

        nextSlide();
        startAutoSlide();

    });


    /* PREVIOUS */

    previousButton.addEventListener("click", () => {

        previousSlide();
        startAutoSlide();

    });


    /* DOTS */

    dots.forEach((dot, index) => {

        dot.addEventListener("click", () => {

            showSlide(index);
            startAutoSlide();

        });

    });


    /* START */

    showSlide(0);
    startAutoSlide();

});