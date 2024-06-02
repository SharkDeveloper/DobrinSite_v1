$(document).ready(function() {
  const breadcrumbs = $('.breadcrumb__item');
  let focusedItem;

  breadcrumbs.each(function() {
    $(this).on('click', function() {
      if (focusedItem) {
        focusedItem.removeClass('focused');
      }
      focusedItem = $(this);
      focusedItem.addClass('focused');
    });
  });

  $('#genre').val('0');
  $('#instock').val('1');

  $('#all-filter').click(function() {
    $('#genre').val('0');
  });
  $('#portraits-filter').click(function() {
    $('#genre').val('1');
  });
  $('#picture-filter').click(function() {
    $('#genre').val('2');
  });
  $('#abstract-filter').click(function() {
    $('#genre').val('3');
  });
  $('#graphics-filter').click(function() {
    $('#genre').val('4');
  });
  $('#lighting-filter').click(function() {
    $('#genre').val('5');
  });
  $('#checkbox_instock').change(function() {
    if ($('#checkbox_instock').is(':checked')) {
        $('#instock').val('1');
    }
    else {
        $('#instock').val('0');
    }
  });

  if ($(window).width() > 800) {
    $('#mobile_catalog').hide();
    $('#catalog').show();
  }
  else {
    $('#catalog').hide();
    $('#mobile_catalog').show();
  }

});