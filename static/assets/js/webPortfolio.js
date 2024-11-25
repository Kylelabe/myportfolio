 const ctx = document.getElementById("skillChart").getContext('2d');
    const skillChart = new Chart(ctx, {
            type: 'line',
            data: {
               labels: ["2020", "2021", "2022", "2023", "2024"],
               datasets: [{
                label: 'Skill Growth',
                data: [10, 20, 30, 40, 50],
                borderColor: 'rgba(75,192,192,0.2)',
                borderWidth: 2,
                pointRadius: 4,
                pointBackgroundColor: '#007bff',
            }]
        },
        options: {
           responsive: true,
           scales: {
             y: {
               beginAtZero: true,
               max: 100
             }
           }
        }
    });

   document.addEventListener('DOMContentLoaded', () => {
    const track = document.querySelector('.bd-best-list');
    const slides = document.querySelectorAll('.bd-tw, .bd-screenshot');
    const totalSlides = slides.length;

    // Clone slides for seamless scrolling
    for (let i = 0; i < totalSlides; i++) {
        const clone = slides[i].cloneNode(true);
        track.appendChild(clone);
    }
});

   document.addEventListener('DOMContentLoaded', () => {
    const toggleSwitch = document.querySelector('#theme-toggle');

    // Check for previously saved theme setting
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme) {
        document.body.classList.add(currentTheme);
    }

    toggleSwitch.addEventListener('click', () => {
        if (document.body.classList.contains('light-mode')) {
            document.body.classList.remove('light-mode');
            document.body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark-mode');
        } else {
            document.body.classList.remove('dark-mode');
            document.body.classList.add('light-mode');
            localStorage.setItem('theme', 'light-mode');
        }
    });
});