// Slideshow & Carousel Logic for Projects
const slideshowState = {};

function initSlideshow(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const slides = container.querySelectorAll('.slide');
    const thumbs = container.querySelectorAll('.thumb');
    const counter = container.querySelector('.current-slide');

    slideshowState[containerId] = {
        currentIndex: 0,
        slides: slides,
        thumbs: thumbs,
        counter: counter
    };
}

function showSlide(index, containerId) {
    if (!slideshowState[containerId]) {
        initSlideshow(containerId);
    }

    const state = slideshowState[containerId];
    if (!state || state.slides.length === 0) return;

    // Wrap around index
    if (index >= state.slides.length) {
        state.currentIndex = 0;
    } else if (index < 0) {
        state.currentIndex = state.slides.length - 1;
    } else {
        state.currentIndex = index;
    }

    // Update slide visibility
    state.slides.forEach((slide, i) => {
        if (i === state.currentIndex) {
            slide.classList.add('active');
        } else {
            slide.classList.remove('active');
        }
    });

    // Update thumbnail highlights
    state.thumbs.forEach((thumb, i) => {
        if (i === state.currentIndex) {
            thumb.classList.add('active');
        } else {
            thumb.classList.remove('active');
        }
    });

    // Update Counter
    if (state.counter) {
        state.counter.textContent = state.currentIndex + 1;
    }
}

function moveSlide(direction, containerId) {
    if (!slideshowState[containerId]) {
        initSlideshow(containerId);
    }
    const state = slideshowState[containerId];
    showSlide(state.currentIndex + direction, containerId);
}

function setSlide(index, containerId) {
    showSlide(index, containerId);
}

// Initialize slideshows on page load
document.addEventListener('DOMContentLoaded', () => {
    const containers = document.querySelectorAll('.slideshow-container');
    containers.forEach(container => {
        initSlideshow(container.id);
    });
});
