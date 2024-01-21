// Get all elements with the specified class
var elements = document.querySelectorAll(
  ".a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal"
);

// Create an array to store href values
var hrefValues = [];

// Loop through the elements and extract href values
elements.forEach(function (element) {
  var href = element.getAttribute("href");
  hrefValues.push(href);
});

// Print the array of href values
var arr = [...new Set(hrefValues.filter((href) => !href.includes("/sspa")))];

return arr;
