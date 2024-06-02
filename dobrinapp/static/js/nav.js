document.addEventListener('DOMContentLoaded', () => {
    const burgerMenu = document.querySelector('.burger-menu');
    if (location.pathname == '/shopping_cart/') {
      burgerMenu.classList.add('header-dark');
    } else {
      burgerMenu.classList.remove('header-dark');
    }

  if ($(window).width() < 800) {
    $('#img-link-3').hide();
    $('#img-link-4').hide();
  } else {
    $('#img-link-3').show();
    $('#img-link-4').show();
  }

});
