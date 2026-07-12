window.addEventListener("DOMContentLoaded", () => {

    lucide.createIcons();

    gsap.from("nav", {
        y: -80,
        opacity: 0,
        duration: 0.8,
        ease: "power3.out"
    });

    gsap.from(".hero-title", {
        y: 40,
        opacity: 0,
        duration: 1,
        ease: "power3.out"
    });

    gsap.from(".hero-subtitle", {
        y: 30,
        opacity: 0,
        duration: 1,
        delay: 0.2,
        ease: "power3.out"
    });

    gsap.from(".hero-button", {
        y: 20,
        opacity: 0,
        duration: 0.8,
        delay: 0.4,
        stagger: 0.1,
        ease: "power3.out"
    });
    gsap.fromTo(
    ".bento-card",
    {
        y: 40,
        opacity: 0
    },
    {
        y: 0,
        opacity: 1,
        duration: 0.8,
        stagger: 0.08,
        delay: 0.5,
        ease: "power3.out"
    }
);
   gsap.to(".hero-car", {
    y: -8,
    duration: 2,
    repeat: -1,
    yoyo: true,
    ease: "sine.inOut"
});
});