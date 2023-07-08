const toggleButton = document.querySelector(".dark-light");

toggleButton.addEventListener("click", () => {
 document.body.classList.toggle("dark-mode");
 // Store dark mode preference in a cookie
 const isDarkMode = body.classList.contains('dark-mode');
 document.cookie = `darkModePreference=${isDarkMode}; path=/`;
});

// Initialize dark mode preference based on the stored cookie value
const cookie = document.cookie;
const darkModeCookie = cookie.split(';').find(cookie => cookie.trim().startsWith('darkModePreference='));
const darkModePreference = darkModeCookie ? darkModeCookie.split('=')[1] : '';
const body = document.querySelector('body');
body.classList.toggle('dark-mode', darkModePreference === 'true');